from ast import Str
import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import os
import sys
import webbrowser
import time
from PyQt5.QtCore import QTimer
from tkinter import *
from PIL import ImageTk,Image
import pyttsx3
import speech_recognition as sr
import datetime
import pytz
import wikipedia 
import webbrowser
import os
import pyautogui
import subprocess
import re
import requests
import time
import winapps
import winshell
import ctypes
import win32com.client as wincl
from tkinter import messagebox
import mysql.connector as sql
from bs4 import BeautifulSoup
import text_gui_chatbot


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def web_scraping(qs):
                global flag2
                global loading

                URL = 'https://www.google.com/search?q=' + qs
                page = requests.get(URL)

                soup = BeautifulSoup(page.content, 'html.parser')

                links = soup.findAll("a")
                all_links = []
                for link in links:
                        link_href = link.get('href')
                        if "url?q=" in link_href and not "webcache" in link_href:
                                all_links.append((link.get('href').split("?q=")[1].split("&sa=U")[0]))


                flag= False
                for link in all_links:
                        if 'https://en.wikipedia.org/wiki/' in link:
                                wiki = link
                                flag = True
                                break

                div0 = soup.find_all('div',class_="kvKEAb")
                div1 = soup.find_all("div", class_="Ap5OSd")
                div2 = soup.find_all("div", class_="nGphre")
                div3  = soup.find_all("div", class_="BNeawe iBp4i AP7Wnd")

                if len(div0)!=0:
                        answer = div0[0].text
                elif len(div1) != 0:
                        answer = div1[0].text+"\n"+div1[0].find_next_sibling("div").text
                elif len(div2) != 0:
                        answer = div2[0].find_next("span").text+"\n"+div2[0].find_next("div",class_="kCrYT").text
                elif len(div3)!=0:
                        answer = div3[1].text
                elif flag==True:
                        page2 = requests.get(wiki)
                        soup = BeautifulSoup(page2.text, 'html.parser')
                        title = soup.select("#firstHeading")[0].text

                        paragraphs = soup.select("p")
                        for para in paragraphs:
                                if bool(para.text.strip()):
                                        answer = title + "\n" + para.text
                                        break
                else:
                        answer = "Sorry. I could not find the desired results"
                return answer

def search_from_model(qs):
        res=text_gui_chatbot.chatbot_response(qs)
        #print(res)
        return res

class SearchQuery:
        
                        

        def search(self,query):
                try:
                        if query:
                                query=query.lower()

                        result=search_from_model(query)

                        if result!=NONE:
                                return result 

                        else:
                                if 'activate' in query:
                                        result="activated"
                                        return result

                                elif 'wikipedia' in query:
                                        #speak('Searching Wikipedia...')
                                        query = query.replace("wikipedia", "")
                                        result = wikipedia.summary(query, sentences=2)
                                        speak("According to Wikipedia")
                                        print(result)
                                        return result

                                
                                elif 'open youtube' in query:
                                        webbrowser.open_new_tab("https://www.youtube.com")
                                        result="Youtube is opening now"
                                        print(result)
                                        time.sleep(2)
                                        return result

                                elif 'open google' in query:
                                        webbrowser.open("google.com")
                                        result="Google is opening now"
                                        time.sleep(2)
                                        return result



                                elif 'open gmail' in query:
                                        webbrowser.open_new_tab("https://bit.ly/3iOcR5z")
                                        result="Google Mail opening now"  
                                        time.sleep(2)
                                        return result

                                elif "weather" in query:
                                        api_key="8ef61edcf1c576d65d836254e11ea420"
                                        base_url="https://api.openweathermap.org/data/2.5/weather?"
                                        city_name=query
                                        complete_url=base_url+"appid="+api_key+"&q="+city_name
                                        response = requests.get(complete_url)
                                        x=response.json()
                                        if x["cod"]!="404":
                                                y=x["main"]
                                                current_temperature = y["temp"]
                                                current_temperature_celsius=(current_temperature-273.15)
                                                current_humidiy = y["humidity"]
                                                z = x["weather"]
                                                weather_description = z[0]["description"]
                                                speak(" Temperature in kelvin unit is " +
                                                        str(current_temperature) +
                                                        "\n humidity in percentage is " +
                                                        str(current_humidiy) +
                                                        "\n description  " +
                                                        str(weather_description))
                                                result=(" Temperature in kelvin unit = " +
                                                        str(current_temperature) +
                                                        "\n Temperature in celsius unit is="+
                                                        str(current_temperature_celsius)+
                                                        "\n humidity (in percentage) = " +
                                                        str(current_humidiy) +
                                                        "\n description = " +
                                                        str(weather_description))

                                        else:
                                                speak(" City Not Found ")
                                                result="City not Found"
                                        return result
                                
                                elif 'time' in query:
                                        current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
                                        speak(str(current_time.hour)+'hour'+str(current_time.minute)+'minutes')
                                        return current_time

                                elif 'open chrome' in query:
                                        chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome"
                                        os.startfile(chromePath)
                                        result="Chrome is opening"
                                        time.sleep(2)
                                        return result

                                elif 'change tab' in query:
                                        pyautogui.keyDown("alt")
                                        pyautogui.press("tab")
                                        pyautogui.keyUp("alt")
                                        result="Changing tab"
                                        return result

                                elif 'open calculator' in query:
                                        subprocess.Popen('C:\\Windows\\SysWOW64\\calc.exe')
                                        result="CALCULATOR IS OPENING"
                                        time.sleep(2)
                                        return result

                                elif 'open notepad' in query:
                                        subprocess.Popen('C:\Windows\SysWOW64\\notepad.exe')
                                        result="NOTEPAD IS OPENING"
                                        time.sleep(2)
                                        return result

                                elif "log off" in query or "sign out" in query:
                                        speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                                        subprocess.call(["shutdown", "/l"])


                                elif 'lock window' in query:
                                                speak("locking the device")
                                                ctypes.windll.user32.LockWorkStation()
                                
                                elif 'shutdown' in query:
                                                speak("Hold On a Sec ! Your system is on its way to shut down")
                                                subprocess.call('shutdown / p /f')
                                                
                                elif 'empty recycle bin' in query:
                                        winshell.recycle_bin().empty(confirm = False, show_progress = True, sound = True)
                                        result="Recycle Bin Recycled"
                                        return result
                                        
                                elif 'change background' in query:
                                        ctypes.windll.user32.SystemParametersInfoW(20, 
                                                                                0, 
                                                                                "Location of wallpaper",
                                                                                0)
                                        speak("Background changed succesfully")

                                

                                elif 'task manager' in query:
                                        pyautogui.hotkey('ctrl','shift','esc')
                                        results="opening task manager"
                                        time.sleep(2)
                                        return results

                                elif 'screenshot' in query:
                                        pyautogui.hotkey('win','shift','s')
                                        results="Taking screenshot"
                                        time.sleep(5)
                                        return results

                                
                                elif 'search' in query or 'play' in query:
                                        query = query.replace("search", "")           
                                        result=web_scraping(query)
                                        return result

                                
                                
                                elif 'settings' in query:
                                        subprocess.Popen([r"C:\\Windows\\SysWOW64\\DpiScaling.exe"])
                                        result="opening settings"
                                        return result

                                elif 'device manager' in query:
                                        subprocess.call("control /name Microsoft.DeviceManager")
                                        result="opening device manager"
                                        return result
                                
                                elif 'devices' in query:
                                        os.system('control /name Microsoft.DevicesAndPrinters')
                                        result="displaying devices list"
                                        return result

                                else:
                                        result=web_scraping(query)
                                        return result        
                except:
                        result="Say that again please"
                        return result                        
                                