import pyttsx3

while True:
    text = input("Type: ")

    if text.lower() == "exit":
        break

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

    del engine
