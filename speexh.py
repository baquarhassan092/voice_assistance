import speech_recognition  
import pyttsx3
import os
import webbrowser
import time
import wikipedia
import sms
import stoppingfun
import running
import all_youtube_link as link
from datetime import datetime 


current_date_time = datetime.now()   # create instance of now class

# Extract and print the date, day, and year
current_date = current_date_time.date()
day_of_week = current_date_time.strftime("%A")
year = current_date_time.year
  
try:
 r = speech_recognition.Recognizer()  # r know how to recognize the audio
 with speech_recognition.Microphone() as mymic:
     r.adjust_for_ambient_noise(mymic, duration=0.2) # avoid noise
     audio4 = r.listen(mymic)
     r.adjust_for_ambient_noise(mymic, duration=0.2) # avoid noise
     
     sound_1 = r.recognize_google(audio4) 
     sound_1 = sound_1.lower()
     if( running.run(sound_1) == True):
          engine = pyttsx3.init() # create an instance of pyttsx3_module of class init() to acess it's members and methods

          engine.setProperty('rate' , 135)  # set_rate 
          engine.say('How can I help you today?')
          engine.runAndWait()  
          time.sleep(0.1)  # make some delay
          print("Say something:")
          time.sleep(0.2)
          engine.say('Say something')  # engine tell the speaker to speak
          engine.runAndWait()

          while( True):
               try:
               
                  with speech_recognition.Microphone() as mymic:
                    r.adjust_for_ambient_noise(mymic, duration=0.2) # avoid noise
                    audio3 = r.listen(mymic)
                    r.adjust_for_ambient_noise(mymic, duration=0.2) # avoid noise
                    
                    sound_ = r.recognize_google(audio3) 
                    sound_ = sound_.lower()
                    
                    with open('speech.wav', mode='a+', encoding='utf-8') as file:   
                              file.write(str(sound_) + ' '+str(time.strftime('%H:%M:%S')) + ' ' + str(current_date) + ' ' + str(day_of_week) + ' '+ str(year) +  '\n')
                    if(stoppingfun.stop(sound_)):
                         break     
                    elif(True) :                         
                         text = r.recognize_google(audio3)     
                         
                         # convert all text into lower cases
                         text = text.lower() 
                         # To display on the screen what I inquired using a recognizer
                         # saving all point we say or asked

                        
                              
                        
                         print(f"Recognized: {text}")  

                         
                         if  'chrome' in text : 
                              engine.say('opening chromebrowser')
                              engine.runAndWait()
                              webbrowser.open('https://www.google.com/intl/en_in/chrome/')
                         elif 'channel' in text or 'youtubechannel' in text or 'channelname' in text or 'channel name' in text or 'youtube channel' in text:
                              engine.say('searching in progress')
                              engine.runAndWait()
                              time.sleep(2)
                              engine.say( 'here is your result') 
                              engine.runAndWait()
                              # go into web and and search what i asked
                              webbrowser.open(link.search_(text))

                         elif 'youtube' in text:
                              engine.say('opening youtube.com')
                              engine.runAndWait()
                              webbrowser.open('https://youtube.com/')  
                              

                         elif 'google' in text:
                              engine.say('opening google.com')   
                              engine.runAndWait()
                              webbrowser.open("https://www.google.co.in/")
                                                            

                              
                         elif 'message' in text or 'whatsappmessage' in text:
                              no_ = input( 'enter a number to be sms using whatsapp')
                              engine.say('what do you want to sms')
                              engine.runAndWait()
                              audio2 = r.listen(mymic)
                              r.adjust_for_ambient_noise(mymic, duration=0.2)
                              qut= r.recognize_google(audio2)
                              
                              time.sleep(0.2)
                              engine.say('your sms is being  sending')
                              engine.runAndWait()
                              sms.mess_(qut , no_)
                              with open('speech.wav', mode='a+') as file:
                                   file.write(qut+ ' ' + str(time.strftime('%H:%M:%S')) +' ' + str(current_date) +" "+str(day_of_week) + " " +str( year) + '\n')
                              
                              print("sms is sended " )

                         elif 'whatsapp' in text:
                              engine.say('opening whatsapp ')
                              engine.runAndWait() 
                              webbrowser.open('https://web.whatsapp.com/send=link')
                         elif 'linkedin' in text :
                              engine.say('opening  linkedin ')
                              engine.runAndWait() 
                              webbrowser.open("https://www.linkedin.com/help/linkedin/answer/a522735/find-your-linkedin-public-profile-url?lang=en ")  
                         elif 'notepad' in text :
                              # provide the file name
                              engine.say('Could you please provide the file name?')
                              engine.runAndWait()
                              audio1 = r.listen(mymic)
                              r.adjust_for_ambient_noise(mymic, duration=0.2)
                              file_name = r.recognize_google(audio1)
                              engine.say('file is being opening ')
                              engine.runAndWait()
                              # To open Notepad with a specific file
                              os.system('notepad ' + str(file_name))
                              
                         
                         elif 'what' in text or 'when' in text or 'why' in text:
                              #  look up the information related to my query on Wikipedia?
                              result = wikipedia.summary(text , sentences = 2)
                              print(result)
                              engine.say(result)
                              engine.runAndWait()
                              time.sleep(1)
                              # go into web and and search what i asked
                              webbrowser.open( 'https://www.google.com/search?q=' + text)     
                              with open('speech.wav', mode='a+') as file:
                                   file.write(result+ ' ' + str(time.strftime('%H:%M:%S')) +' ' + str(current_date) +" "+str(day_of_week) + " " +str( year) + '\n')
                              


                                   
                         else:
                              engine.say('searching in progress')
                              engine.runAndWait()
                              time.sleep(2)
                              engine.say( 'here is your result') 
                              engine.runAndWait()
                              # go into web and and search what i asked
                              webbrowser.open( 'https://www.google.com/search?q=' + text)
                              
                      
                         
                         
                         
                         

               # exceptional handling : when exception will occurred
               except speech_recognition.UnknownValueError:
                     print("ohh! speech_recognition could not understand audio")

               except  :
                    print('unknown error')

except   speech_recognition.UnknownValueError:
        print("ohh! speech_recognition could not understand audio")           
