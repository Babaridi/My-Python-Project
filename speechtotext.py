import speech_recognition
import pyttsx3


def main():
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Say something... ")
        audio = r.listen(source, phrase_time_limit=300)

        print("Recognizing ... ")

        try:
            print("You have said : \n " + r.recognize_google(audio))
            print("Audio Recorded Successfully\n")
        except Exception as e:
            print("Error : " + str(e))

            with open("recoded audio.wav", "wb") as f:
                f.write(audio.get_wav_data())


if __name__ == "__main__":
    main()
