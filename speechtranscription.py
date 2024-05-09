import speech_recognition as sr

def transcribe_audio():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Dites quelque chose...")
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio, language='fr-FR')
        print("Vous avez dit :", text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition n'a pas pu comprendre l'audio.")
        return None
    except sr.RequestError as e:
        print("Erreur lors de la requête vers Google Speech Recognition : {0}".format(e))
        return None

# Exemple d'utilisation
transcribed_text = transcribe_audio()
if transcribed_text:
    # Vous pouvez utiliser le texte transcrit comme bon vous semble, par exemple l'afficher
    print("Texte transcrit :", transcribed_text)
