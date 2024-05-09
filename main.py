from google.cloud import translate_v2 as translate
from gtts import gTTS
import os
import html

# Configurez la variable d'environnement
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './credentials.json'

def translate_text(text, target_language='fr'):
    # Initialize the translation client
    client = translate.Client()

    # Translate the text
    translation = client.translate(text, target_language=target_language)

    # Decode HTML entities
    translated_text = html.unescape(translation['translatedText'])

    # Return the translated text
    return translated_text


def speak_text(text, language='fr'):
    # Initialize gTTS with the text and language
    tts = gTTS(text=text, lang=language)

    # Save the audio to a file
    tts.save("translation.mp3")

    # Play the audio
    os.system("mpg123 translation.mp3")

# Exemple d'utilisation
text_to_translate = "Er was eens een eend die in het gras dartelde"
translated_text = translate_text(text_to_translate, target_language='fr')
print(translated_text)

speak_text(translated_text)
