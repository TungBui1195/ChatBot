# Advance:  DrQA, DialogFlow, ChatScript

import pyttsx3
import speech_recognition

while (1):

    robot_ear = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print ("Robot: I'm Listening")
        audio = robot_ear.listen(mic)
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: " + you)



    if you == "":
        robot_brain = "I can't hear you, try again"
    elif you == "hello" or you == "hi":
        robot_brain = "Hello Tung Bui"
    elif "wife" in you:
        robot_brain = "Trang Le"
    elif "bye" in you:
        robot_brain = "Good bye, See you again"
        print(robot_brain)
        robot_mouth = pyttsx3.init()
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I'm good"

    print(robot_brain)
    robot_mouth = pyttsx3.init()
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()




