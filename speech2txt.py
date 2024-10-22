import speech_recognition as sr

r = sr.Recognizer() 

def record():
    audio = []
    with sr.Microphone() as source2:  
        r.adjust_for_ambient_noise(source2, duration=0.2)
        #listens for the user's input 
        audio2 = r.listen(source2)
        audio.append(audio2)
    return audio

def textify(audio):  
    # Using google to recognize audio
    for item in audio:
        MyText = r.recognize_google(item)
    MyText = MyText.lower()
    return MyText

def txt():
    while True:
        try:
            textOuput = textify(record())
            break
        except:
            pass
    return textOuput
