"""
@Author:      Debanjan Saha
@Date:        18 Nov, 2021
@Description: This is an email automation service using voice command
"""
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
from multiprocessing import Process

listener = sr.Recognizer()

# Save your email contacts in the mailing list below:
mailing_list = {
    "triangle"   : "triangle@squidgame.com",
    "rectangle"  : "rectangle@squidgame.com"
}

class _TTS:
    engine = None
    rate = None
    voices = None
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)
        self.rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', self.rate+20)

    def talk(self, _text):
        self.engine.say(_text)
        self.engine.runAndWait()


def get_voice():
    try:
        with sr.Microphone() as source:
            print("Listening.....")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(from_email, email_pwd, receiver, email_subject, email_content):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(from_email, email_pwd)

    email = EmailMessage()
    email['From'] = from_email
    email['To'] = receiver
    email['Subject'] = email_subject
    email.set_content(email_content)
    server.send_message(email)
    # server.quit()

def get_email_info(tts, first_time=True):

    try:
        tts.talk('Hello User, can you please provide me your name?')
        from_name = get_voice()
        tts.talk('Can you please type in your email address?')
        from_email = input("Email Id: > ")
        tts.talk('Can you please type in your email password? We do not store any passwords')
        email_pwd = input("Password: > ")
        
        if from_name not in mailing_list:
            mailing_list[from_name] = from_email
        tts.talk('Whom do you want to send a email')
        to_name = get_voice()
        receiver = mailing_list[to_name]
        tts.talk('What is the subject of the email')
        email_subject = get_voice()
        tts.talk('What is the content of the email')
        email_content = get_voice()
        
        send_email(from_email, email_pwd, receiver, email_subject, email_content)
        tts.talk('The email has been sent successfully!')
        tts.talk('Do you want to send more email?')
        more_mail = get_voice()
        if more_mail == 'yes':
            get_email_info(tts, first_time=False)
        else:
            tts.talk('Thank you for using our mailing services. See you again!')

    except KeyError as e:
        tts.talk('We did not find the user in our mailing list. Do you want to enter the user?')
        resp = get_voice()
        if resp == 'yes':
            tts.talk('Please enter the name of the user')
            user_nm = input("Name: > ")
            tts.talk('Please enter the email address of the user')
            user_e = input("Email Id: > ")
            if user_nm not in mailing_list:
                mailing_list[user_nm] = user_e
            get_email_info(tts, first_time=False)
        else:
            tts.talk('Thank you for using our mailing services. See you again!')
                
if __name__ == "__main__":
    tts = _TTS()
    get_email_info(tts)
