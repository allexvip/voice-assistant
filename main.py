#!/usr/bin/env python3
import queue
import sounddevice as sd
import vosk
import sys
import json
import words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from skills import *

q = queue.Queue()
model = vosk.Model('model_small')

device = sd.default.device = 2, 4  # sd.default.device = 1,3 ///input, output
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])


def callback(indata, frames, time, status):
    q.put(bytes(indata))


def recognize(data, vectorizer, clf):
    trigger_word = words.TRIGGERS.intersection(data.split())
    if not trigger_word:
        # print(data)
        return
    data.replace(list(trigger_word)[0], '')
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]

    func_name = answer.split()[0]
    speaker(answer.replace(func_name,''))
    exec(func_name+'()')



def main():
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))

    del words.data_set

    speaker(f". Привет я голосовой ассистент. Зови меня {' или '.join(TRIGGERS)} ")
    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16',
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                # print(rec.Result())
                data = json.loads(rec.Result())['text']
                print(data)
                recognize(data, vectorizer, clf)
            # else:
            #     print(rec.PartialResult())


if __name__ == '__main__':
    main()
