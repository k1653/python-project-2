from tkinter import *
from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry('500x300')
root.resizable(10,10)
root.config(bg = '#FFE873')
root.title('TECHARGE - TEXT TO SPEECH')
Label(root, text = 'TEXT TO VOICE ' , font='Verdana 30 bold' , bg ='white smoke').place(x=30,y=10)
Label(root, text ='PRERNA PRIYA' , font ='Verdana 15 bold', bg = 'white smoke').place(x=190,y=260)
Label(root, text ='Enter Text', font ='Verdana 15 bold', bg ='white smoke').place(x=30,y=70)


Msg = StringVar()


entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=30 , y=120)
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Techarge.mp3')
    playsound('Techarge.mp3')

def Exit():
    root.destroy()

def Exit():
    root.destroy()

Button(root, text = "PLAY" , font = 'Verdana 15 bold', command = Text_to_speech, width =4).place(x=30, y=150)
Button(root,text = 'EXIT',font = 'Verdana 15 bold' , command = Exit, bg = 'OrangeRed1').place(x=100,y=150)

root.mainloop()