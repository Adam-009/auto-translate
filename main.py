import os
import html
import time
import speech_recognition as sr
from google.cloud import translate_v2 as translate
from gtts import gTTS

# Configurez la variable d'environnement pour Google Cloud
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './credentials.json'

def translate_text(text, target_language='fr'):
    # Initialisez le client de traduction
    client = translate.Client()

    # Traduire le texte
    translation = client.translate(text, target_language=target_language)

    # Décoder les entités HTML
    translated_text = html.unescape(translation['translatedText'])

    # Retourner le texte traduit
    return translated_text

def speak_text(text, language='fr'):
    # Initialisez gTTS avec le texte et la langue
    tts = gTTS(text=text, lang=language)

    # Enregistrez l'audio dans un fichier temporaire
    tts.save("translation.mp3")

    # Jouez l'audio
    os.system("mpg123 translation.mp3")

def transcribe_audio():
    # Initialisez le recognizer
    recognizer = sr.Recognizer()

    # Capturez l'audio depuis le microphone
    with sr.Microphone() as source:
        print("Dites quelque chose...")
        audio = recognizer.listen(source)

    try:
        # Reconnaître la parole en utilisant la reconnaissance vocale de Google
        text = recognizer.recognize_google(audio, language='fr-FR')
        print("Vous avez dit :", text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition n'a pas pu comprendre l'audio.")
        return None
    except sr.RequestError as e:
        print("Erreur lors de la requête vers Google Speech Recognition : {0}".format(e))
        return None

# Fonction principale qui traduit, parle et transcrit le texte en continu
def translate_speak_transcribe():
    while True:
        # Transcrire l'audio
        transcribed_text = transcribe_audio()
        if transcribed_text:
            # Traduire le texte transcrit
            translated_text = translate_text(transcribed_text, target_language='fr')
            print("Texte traduit :", translated_text)

            # Parler le texte traduit
            speak_text(translated_text)

            # Pause pendant quelques minutes avant de reprendre l'écoute
            time.sleep(0)  # Attendre 5 minutes (300 secondes)

# Exemple d'utilisation
translate_speak_transcribe()
