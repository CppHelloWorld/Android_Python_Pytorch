import os
import wave

def transfer(pcm_path, wav_path):
    #输入两个参数，一个是pcm音频的路径，一个是转成wav文件后的保存路径

    #打开pcm音频文件用‘r’也就是‘读’的模式
    pcmf = open(pcm_path, 'rb')
    #读到一个数组里面
    pcmdata = pcmf.read()
    #关闭pcm文件
    pcmf.close()
    #打开一个wav文件用‘w’也就是‘写’的模式，没有该文件会自动创建，有现成的文件会被覆盖。
    wavfile = wave.open(wav_path, 'wb')
    #加入一些wav文件重要的信息。
    wavfile.setnchannels(1)
    wavfile.setsampwidth(2)
    wavfile.setframerate(11025)
    #写进wav文件。
    wavfile.writeframes(pcmdata)
    #关闭。
    wavfile.close()
    #其实这个不需要返回值也行，因为不看数据。
    return 1