import speech_recognition as sr

def speech_to_text():
    # promise...this is to recognize the voices
    recognizer = sr.Recognizer()

    #my microphone code
    with sr.Microphone() as source:
        print("Adjusting for noise. Please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening for speech. Speak now...")
        
        try:
            # Capture audio from the microphone
            audio_data = recognizer.listen(source, timeout=5)
            print("Recognizing speech...")

            # Recognize speech using Google's speech recognition api
            text = recognizer.recognize_google(audio_data)
            print("You said:", text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    speech_to_text()
