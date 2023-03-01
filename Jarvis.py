from Brain.AIBrain import ReplyBrain
from Brain.QnA import QuestionsReplier
from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait for some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
print(">>Starting The Jarvis : Wait for few seconds More")
from main import MainTaskExecution

def MainExecution():
    Speak("Hello Sir")
    Speak("I'am Jarvis. I'am Ready To Assist You Sir.")

    while True:

        Data = MicExecution()
        Data = str(Data)
        
        ValueReturn = MainTaskExecution(Data)

        if ValueReturn==True:
            pass

        elif len(Data)<3:
            pass

        elif "say something about me" in Data: # for specific command
            Speak("You are the most cultured person in your family. ")

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsReplier(Data)
        
        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">> Clap Detected!! >>")
        print("")
        MainExecution()

    else:
        pass

ClapDetect()
