from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as SIA
import speech_recognition as sr

rec = sr.Recognizer()
with sr.Microphone() as sound:
    rec.adjust_for_ambient_noise(sound, duration=1)
    print(f'Starting to listen')
    audio = rec.listen(sound)
    print('I have heard something.... analyzing...')

    try:
        text = rec.recognize_google(audio)  # ,language="sv-SE"
        text = text.lower()
        print(' ')
        print(f'Recognized: {text}')
    except Exception as ex:

        print(ex)

    Sentence = [str(text)]
    analyzer = SIA()
    for i in Sentence:
        v = analyzer.polarity_scores(i)
        print(v)
