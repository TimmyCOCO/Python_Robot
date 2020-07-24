# Project Demo 
# gif gets from https://www.zcool.com.cn/work/ZMjc2ODQxOTY=/1.html

import time
import speech_recognition as sr
from selenium import webdriver

import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

from pyswip import Prolog
prolog = Prolog()

driver = webdriver.Chrome('chromedriver')

driver.get(r"https://media.giphy.com/media/JsKH3w5P7ITWxAqTKC/giphy.gif")
speak.Speak("Hello, what can I help you? You have four commands: deliver, testing, video, and goodbye.")
driver.get(r"https://media.giphy.com/media/hX0PcUSR19bcMWcw36/giphy.gif")


def robot():
    global driver
    r = sr.Recognizer()
    exit = False
    
    while not exit:
        try:    
            with sr.Microphone() as source:
                print("Listening... please speak a command(deliver,testing,video,goodbye)")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                
            answer = r.recognize_google(audio)
            answer=answer.lower()

            
            # deliver medicine to the sickroom
            if answer == "deliver":
               
                driver.get(r"https://media.giphy.com/media/YNE3dnqZrZtS7hOWTD/giphy.gif")
                    
                speak.Speak("Medicine is delivering, please wait.")
                    
                # delay for 2s"I am delivering."
                time.sleep(2)
                
                driver.get(r"https://media.giphy.com/media/hX0PcUSR19bcMWcw36/giphy.gif")
               
            # take temperature for the patient
            if answer == "testing":
                driver.get(r"https://media.giphy.com/media/lN3C0pl0dxjBh3jgav/giphy.gif")
                   
                speak.Speak("Please wait, I am taking your temperature.")
                
                # delay for 2s
                time.sleep(2)
                
                driver.get(r"https://media.giphy.com/media/hX0PcUSR19bcMWcw36/giphy.gif")
                
            
            # allow doctors and patients to have a remote communication
            if answer == "video":
                driver.get(r'https://media.giphy.com/media/KDtyKWjNlrpaCLWaAw/giphy.gif')
                
                speak.Speak("Connecting, video call is progressing...")
                
                # delay for 2s
                time.sleep(2)
                
                driver.get(r"https://media.giphy.com/media/hX0PcUSR19bcMWcw36/giphy.gif")


            # use command "goodbye" to end the interation
            if answer == "goodbye":
                driver.get(r"https://media.giphy.com/media/H54ZsVAct4GjR598b3/giphy.gif")
                
                speak.Speak("Happy to help you, see you.")
               
                # delay for 1s
                time.sleep(1)
                
                driver.get(r"https://upload.wikimedia.org/wikipedia/commons/7/71/Black.png")
                
                # quit the loop
                exit = True                
            
            if answer not in ("deliver","testing","video","goodbye"):
                 driver.get(r"https://media.giphy.com/media/Rhf2TbUfBXaFrRud5W/giphy.gif")
                 speak.Speak("I do not understand what you said, please give me a command")
                 driver.get(r"https://media.giphy.com/media/hX0PcUSR19bcMWcw36/giphy.gif")
                 
        except:
            driver.get(r"https://media3.giphy.com/media/8L0Pky6C83SzkzU55a/giphy.gif?cid=ecf05e47c5bc31c90e8373c59667199d000aeba8090a7c1c&rid=giphy.gif")
            speak.Speak("Attention, something wrongs.")
            exit = True
              
robot()