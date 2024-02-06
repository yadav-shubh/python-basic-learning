import io
import speech_recognition as sr
import os
import subprocess
from gtts import gTTS
import openai


def recognize_speech():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True

    # Use the default microphone as the source
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.phrase_threshold = 1
        audio = recognizer.listen(source, timeout=10)  # Listen for up to 5 seconds

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        speak_text(text)
        get_chat_gpt_response(text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")


def speak_text(text):
    tts = gTTS(text=text, lang='en')
    file_path = "output.mp3"
    tts.save(file_path)
    subprocess.run(["open", file_path])
    
    # Delete the file after playing
    # os.remove(file_path)


def get_chat_gpt_response(search):
    openai.api_key = "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"
    response = openai.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": search,
            },
        ],
        model="gpt-3.5-turbo",
    )

    response_msg = response.choices[0].message.content
    print(response_msg)
    speak_text(response_msg)


if __name__ == "__main__":
    recognize_speech()
