from DNN import DNN
import torch
import numpy as np
from scipy import signal
from scipy.fftpack import fft, ifft
import librosa
from os.path import dirname, join

#滤波器，一个信号处理函数。
def band_pass_filter(original_signal, order, fc1,fc2, fs):
    '''
    中值滤波器
    :param original_signal: 音频数据
    :param order: 滤波器阶数
    :param fc1: 截止频率
    :param fc2: 截止频率
    :param fs: 音频采样率
    :return: 滤波后的音频数据
    '''
    b, a = signal.butter(N=order, Wn=[2*fc1/fs,2*fc2/fs], btype='bandpass')
    new_signal = signal.lfilter(b, a, original_signal)
    return new_signal

def get_result(wav_path, model_name = None):
    #加载模型
    model = DNN()

    #这里我给了model_name(存有模型参数的文件)一个默认指，也就是None,这个是为了方便后面有训练新的模型参数的话方便更改位置。
    if model_name == None :
        model_name = join(dirname(__file__), "assets/F_dnn_512_withoutResample.pth")

    #使用cpu运行模型。
    device = torch.device("cpu")

    #把模型加载到cpu上面
    model.to(device)
    #读取模型的参数。
    model.load_state_dict(torch.load(model_name, map_location=torch.device('cpu')))

    #读取wav音频文件，并进行预处理。
    wav, sr = librosa.load(wav_path, sr=1600)
    audio_data = band_pass_filter(wav, 2, 25, 400, sr)
    audio_data = audio_data / np.max(np.abs(audio_data))
    audio_data = audio_data[:2500]

    if audio_data.shape[1]<2500:
        num = torch.zeros(audio_data.shape[0],2500)
        num[:,:audio_data.shape[1]] = audio_data
        num[:,audio_data.shape[1]:] = audio_data[:,:2500-audio_data.shape[1]]
        audio_data = num


    ffty = fft(audio_data)
    ffty = abs(ffty)
    ffty = torch.tensor(ffty)

    #送入模型，输出预测结果(就是output)
    output = model(ffty)
    output = output.data.cpu().numpy()
    output = output.tolist()

    i=0
    for j in range(len(output)):
        if output[j] > output[i]:
            i = j

    if i == 0:
        #返回一个字符串
        return "正常"
    #返回一个字符串
    return "异常"


















