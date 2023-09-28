import speech_recognition as sr

# Initialize the speech_to_text recognizer (only once)
recognizer = None

def get_recognizer():
    global recognizer
    if recognizer is None:
        # Initialize the recognizer
        recognizer = sr.Recognizer()
    return recognizer


def record_audio():
    recognizer = get_recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

    # Recognize the speech
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

    return text