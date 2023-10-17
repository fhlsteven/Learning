# -*- coding: utf-8 -*-
import os
from pydub import AudioSegment
import speech_recognition as sr

all_data = []
r = sr.Recognizer()
has_proc = []

def main_proc():
    for mp3 in all_data:
        if mp3 in has_proc:
            continue
        mp3_to_wav(mp3, mp3.split('_')[0])
        proc_single(mp3, mp3.split('_')[0])

def mp3_to_wav(file, name):
    song = AudioSegment.from_mp3('./file/'+file)
    song[16*1000:].export(f'./poc/'+file)

    first_15_secs = song[16*1000:20*1000]
    first_15_secs.export(f'./wav/'+name+'.wav', format='wav')

def proc_single(file, name):
    try:
        with sr.AudioFile('./wav/'+name+'.wav') as source:
            audio = r.record(source)
            text = r.recognize_google(audio, language='zh-cn')
            save_log(file, text)
    except Exception as ex:
        print(ex)
        print(file)
        save_log(file, ex)

def save_log(file, text):
    with open('./log/log.txt',"a+", encoding='utf-8') as f:
        f.writelines(f'\n{file}:{text}')

if __name__ == '__main__':
    all_data = os.listdir('./file')
    has_proc = os.listdir('./poc')
    main_proc()
