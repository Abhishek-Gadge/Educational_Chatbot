from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import pyttsx3
from PIL import ImageTk,Image



notes_ids = []
selected_index = 0

def speak():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(note_text.get('1.0', END))
    engine.runAndWait()
    

def onselect(evt):  
    global selected_index
    
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    selected_index = index

    display_note(index, value)

window = tk.Tk()
window.title("Note Writing")
window.overrideredirect()
window.geometry("1000x700")
window.configure(bg='#008080')


top_frame = tk.Frame(window)
scroll_list = tk.Scrollbar(top_frame)
scroll_list.pack(side=tk.RIGHT, fill=tk.Y)

list_notes = Listbox(top_frame, height=30, width=40)
list_notes.bind('<<ListboxSelect>>', onselect)
list_notes.pack(side=tk.LEFT, fill=tk.Y, padx=(10,10), pady=(10, 10))
top_frame.configure(bg='#C0C0C0')
top_frame.pack(padx=50 ,pady=10)


scroll_list.config(command=list_notes.yview)
list_notes.config(yscrollcommand=scroll_list.set, cursor="hand2", background="#FFFFFF", highlightbackground="grey", bd=0, selectbackground="black")
top_frame.pack(side=tk.TOP, padx=(0, 5))
top_frame.pack(side=LEFT)

text_frame = tk.Frame(window)
note_title = tk.Entry(text_frame, width=40, font = "Helvetica 13")
note_title.insert(tk.END, "Title")
note_title.config(background="#FFFFFF", highlightbackground="grey")
note_title.pack(side=tk.TOP, pady=(5, 5), padx=(0, 10))
text_frame.configure(bg="#C0C0C0")


scroll_text = tk.Scrollbar(text_frame)
scroll_text.pack(side=tk.RIGHT, fill=tk.Y)

note_text = tk.Text(text_frame, height=10, width=40, font = "Helvetica 13")
note_text.pack(side=tk.TOP, fill=tk.Y, padx=(10,10), pady=(10,10))
note_text.tag_config("tag_your_message", foreground="blue")
note_text.insert(tk.END, "Notes")

scroll_text.config(command=note_text.yview)
note_text.config(yscrollcommand=scroll_text.set, background="#FFFFFF", highlightbackground="grey")

text_frame.pack(side=tk.TOP,padx=(20,5),pady=(150,20))
text_frame.pack(side=LEFT)

button_frame = tk.Frame(window)
photo_add = PhotoImage(file="final_project\\add.gif")
photo_edit = PhotoImage(file="final_project\\edit.gif")
photo_delete = PhotoImage(file="final_project\\delete.gif")
photo_speaker=PhotoImage(file="final_project\\speaker.gif")

btn_save = tk.Button(button_frame, text="Add", command=lambda : save_note(), image=photo_add)
btn_edit = tk.Button(button_frame, text="Update", command=lambda : update_note(), state=tk.DISABLED, image=photo_edit)
btn_delete = tk.Button(button_frame, text="Delete", command=lambda : delete_note(), state=tk.DISABLED, image=photo_delete)
btn = Button(button_frame, text = "Speak",command =lambda:speak(),image=photo_speaker)

btn_save.grid(row=0, column=1)
btn_edit.grid(row=0, column=2)
btn_delete.grid(row=0, column=3)
btn.grid(row=0, column=4)

button_frame.pack(side=tk.TOP,fill=tk.Y,padx=(0,22),pady=(70,80))
button_frame.pack(side=BOTTOM)
button_frame.configure(bg="#C0C0C0")
#button_frame.pack(side=RIGHT)

label=Label(window,text="KEEP NOTING",font = "Helvetica 20",bg="#C0C0C0")
label.pack(side=TOP,pady=20)

but=tk.Button(window,text="QUIT",width=8,command=window.quit,bg="#C0C0C0")
but.pack(pady=3,side=TOP)

# DATABASE FUNCTIONS STARTS
conn = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="8805",auth_plugin="mysql_native_password")

def db_create_db(conn):
    mycursor = conn.cursor()
    query = "CREATE DATABASE IF NOT EXISTS db_notes"
    mycursor.execute(query)

def db_create_table(conn):
    db_create_db(conn)
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS tb_notes (" \
          "note_id INT AUTO_INCREMENT PRIMARY KEY, " \
          "title VARCHAR(255) NOT NULL, " \
          "note VARCHAR(2000) NOT NULL)"
    mycursor.execute(query)

def db_insert_note(conn, title, note):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "INSERT INTO tb_notes (title, note) VALUES (%s, %s)"
    val = (title, note)
    mycursor.execute(query, val)
    conn.commit()
    return mycursor.lastrowid

def db_select_all_notes(conn):
    conn.database = "db_notes"
    query = "SELECT * from tb_notes"
    mycursor = conn.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()

def db_select_specific_note(conn, note_id):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    mycursor.execute("SELECT title, note FROM tb_notes WHERE note_id = " + str(note_id))
    return mycursor.fetchone()

def db_update_note(conn, title, note, note_id):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "UPDATE tb_notes SET title = %s, note = %s WHERE note_id = %s"
    val = (title, note, note_id)
    mycursor.execute(query, val)
    conn.commit()

def db_delete_note(conn, note_id):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "DELETE FROM tb_notes WHERE note_id = %s"
    adr = (note_id,)
    mycursor.execute(query, adr)
    conn.commit()

def init(conn):
    db_create_db(conn)  # create database if not exist
    db_create_table(conn)  # create table if not exist

    # select data
    notes = db_select_all_notes(conn)

    for note in notes:
        list_notes.insert(tk.END, note[1])
        notes_ids.append(note[0])  # save the id

init(conn)

# BUTTON CLICK FUNCTION STARTS
def save_note():
    global conn
    title = note_title.get()

    if len(title) < 1:
        tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter the note title")
        return

    note = note_text.get("1.0", tk.END)
    if len(note.rstrip()) < 1:
        tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter the notes")
        return  

    # Check if title exist
    title_exist = False
    existing_titles = list_notes.get(0, tk.END)

    for t in existing_titles:
        if t == title:
            title_exist = True
            break

    if title_exist is True:
        tk.messagebox.showerror(title="ERROR!!!", message="Note title already exist. Please choose a new title")
        return

    # save in database
    inserted_id = db_insert_note(conn, title, note)
    print("Last inserted id is: " + str(inserted_id))

    # insert into the listbox
    list_notes.insert(tk.END, title)

    notes_ids.append(inserted_id)  # save notes id

    # clear UI
    note_title.delete(0, tk.END)
    note_text.delete('1.0', tk.END)


def update_note():
    global selected_index, conn

    title = note_title.get()

    if len(title) < 1:
        tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter the note title")
        return

    note = note_text.get("1.0", tk.END)
    if len(note.rstrip()) < 1:
        tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter the notes")
        return

    note_id = notes_ids[selected_index]  # get the id of the selected note

    # save in database
    db_update_note(conn, title, note, note_id)

    # update list_note
    list_notes.delete(selected_index)
    list_notes.insert(selected_index, title)

    # clear UI
    note_title.delete(0, tk.END)
    note_text.delete('1.0', tk.END)

def delete_note():
    global selected_index, conn, notes_ids
    title = note_title.get()
    notes = note_text.get("1.0", tk.END)

    print("Selected note is: " + str(selected_index))

    if len(title) < 1 or len(notes.rstrip()) < 1:
        tk.messagebox.showerror(title="ERROR!!!", message="Please select a note to delete")
        return

    result = tk.messagebox.askquestion("Delete", "Are you sure you want to delete?", icon='warning')

    if result == 'yes':
        # remove notes from db
        note_id = notes_ids[selected_index]
        db_delete_note(conn, note_id)
        del notes_ids[selected_index]

        # remove from UI
        note_title.delete(0, tk.END)
        note_text.delete('1.0', tk.END)
        list_notes.delete(selected_index)

def display_note(index, value):
    global notes_ids, conn
    # clear the fields
    note_title.delete(0, tk.END)
    note_text.delete('1.0', tk.END)

    note = db_select_specific_note(conn, notes_ids[index])

    # insert data
    note_title.insert(tk.END, note[0])
    note_text.insert(tk.END, note[1])

    btn_delete.config(state=tk.NORMAL)
    btn_edit.config(state=tk.NORMAL)

window.mainloop()