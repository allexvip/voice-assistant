#!/usr/bin/env python3
import queue
import sounddevice as sd
import vosk
import sys
import json

q = queue.Queue()
model = vosk.Model('model_small')

device = sd.default.device = 2, 4  # sd.default.device = 1,3 ///input, output
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])


def callback(indata, frames, time, status):
    q.put(bytes(indata))


with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16',
                       channels=1, callback=callback):
    rec = vosk.KaldiRecognizer(model, samplerate)
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            # print(rec.Result())
            data = json.loads(rec.Result())['text']
            print(data)
        # else:
        #     print(rec.PartialResult())
