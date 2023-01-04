import speech_recognition
import pyttsx3


def listen():
    text_list = []
    recognizer = speech_recognition.Recognizer()
    # for index, name in enumerate(speech_recognition.Microphone.list_microphone_names()):
    #   print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    while True:

        try:

            with speech_recognition.Microphone() as sound:
                recognizer.adjust_for_ambient_noise(sound, duration=0.2)
                print(f'Starting to listen')
                audio = recognizer.listen(sound)

                text = recognizer.recognize_google(audio)  # ,language="sv-SE"
                print('I have heard something.... analyzing...')
                text = text.lower()
                print(' ')
                print(f'Recognized: {text}')
                text_list.append(str(text))
                return str(text_list)
        except speech_recognition.UnknownValueError():
            return str(text_list)


def main():
    text = listen()
    print(text)

if __name__ == "__main__":
    main()
