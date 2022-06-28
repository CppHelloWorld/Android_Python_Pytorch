import numpy as np
import librosa
from scipy import signal

#输入参数是wav文件路径。
def get_period(wav_path):
    wav_data, sr = librosa.load(wav_path, sr=1000)
    top_one_value = wav_data.argmax(axis=0)
    num_peak_3 = signal.find_peaks(wav_data, distance=3)

    peak_result = wav_data[num_peak_3[0]]
    top_two_key = peak_result.argsort()[-2]
    top_two_value = num_peak_3[0][top_two_key]

    result = abs(top_one_value-top_two_value)*0.001
    i = 3
    while (result > 1.2 or result<0.1) and i<15 :
        result = abs(top_one_value-num_peak_3[0][peak_result.argsort()[-i]])*0.001
        i = i + 1

    #输出一个结果，单位是毫秒(ms)，意为一次心跳的周期。
    return result
