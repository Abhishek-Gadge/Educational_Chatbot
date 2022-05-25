from tkinter import font
from matplotlib.pyplot import flag
from ChatbotUi import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import datetime
import sys
import subprocess
from PyQt5.QtCore import QTimer
import searching_query
from playsound import playsound



globals()["inputComm"] = "hey"


globals()["output"]='Hi'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        self.wishme()
        

    def run(self):
        self.taskExecution()
    
    def wishme(self):
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")

        elif hour>=12 and hour<18:
            speak("Good Afternoon!")   

        else:
            speak("Good Evening!")  

        speak("I am your Assistant. Please tell me how may I help you") 

    def takeCommand(self):
        r = sr.Recognizer()
        r.dynamic_energy_threshold = False
        r.energy_threshold = 4000
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 0.5
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            
            query = r.recognize_google(audio, language='en-in')
            
            globals()["inputComm"]=query
            print(f"User said: {query}\n")      
            
            

        except Exception as e:
            print(e)    
            print("Say that again please...")  
            return None

        return query

    def taskExecution(self):
        flag=0
        while True:
            try:
                query = self.takeCommand()
                if 'activate' == query:
                    flag=1
                    speak("Activated")
                    playsound('final_project\\chime.wav')
                    
                elif 'deactivate' == query:
                    flag=0
                    playsound('final_project\\chime.wav')
                    

                if flag==1: 
                    globals()["output"] = searching_query.SearchQuery().search(query)
                    speak(globals()["output"])

            except:
                self.taskExecution()


startFunction = MainThread()



class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        print("inside init GuiStart")
        self.chatbot_ui=Ui_MainWindow()
        cmd='python notes.py'
        self.chatbot_ui.setupUi(self)
        self.chatbot_ui.pushButton.clicked.connect(self.startFunc)
        self.chatbot_ui.pushButton_2.clicked.connect(self.close)
        #self.chatbot_ui.pushButton_.clicked(cmd)
        self.chatbot_ui.pushButton_3.clicked.connect(self.startNote)
        self.chatbot_ui.pushButton_4.clicked.connect(self.startChatbot)

    def startFunc(self):

        print("inside start fun")
        self.chatbot_ui.movies_label_2=QtGui.QMovie("final_project\\initial.gif")
        self.chatbot_ui.label_2.setMovie(self.chatbot_ui.movies_label_2)
        self.chatbot_ui.movies_label_2.start()

        self.chatbot_ui.movies_label_3=QtGui.QMovie("final_project\\Aqua.gif")
        self.chatbot_ui.label_3.setMovie(self.chatbot_ui.movies_label_3)
        self.chatbot_ui.movies_label_3.start()
        
        d_ate=QDate.currentDate()
        date=d_ate.toString()
        label_Date=date
        self.chatbot_ui.date.setText(label_Date)  


        self.i = 0
        self.qTimer = QTimer()
        # set interval to 1 s
        self.qTimer.setInterval(500) # 1000 ms = 1 s
        # connect timeout signal to signal handler
        self.qTimer.timeout.connect(self.updateUI)
        # start timer
        self.qTimer.start()      
        
        startFunction.start()
        
    
    def startNote(self):

        cmd='python final_project\\notes.py'
        subprocess.Popen(cmd,shell=True)

    def startChatbot(self):
        cmd='python final_project\\text_chatbot.py'
        subprocess.Popen(cmd,shell=True)

    def updateUI(self):
        input_text= globals()["inputComm"] 
        output_text=globals()["output"] 
        self.chatbot_ui.input_text.setText(str(input_text))
        self.chatbot_ui.output_text.setText(str(output_text))
        
    
    

Gui_App = QApplication(sys.argv)
Gui_Chatbot = Gui_Start()
Gui_Chatbot.show()
exit(Gui_App.exec_())