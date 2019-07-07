import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

 
#os audios foram gerados pela ferramenta abaxi
#https://www.audiocheck.net/audiofrequencysignalgenerator_sinetone.php

file1 = "audiocheck.net_sin_50Hz_0dBFS_3s.wav"
file2 = "audiocheck.net_sin_1000Hz_0dBFS_3s.wav"

#deve ser proporcional ao sample rate utilizado no audio
#nos arquivos acima eu usei um sample rate de 48, por isso leva esse valor
num_samples = 48000 

def openfile(file):
	wav_file = wave.open(file, 'r')
	data = wav_file.readframes(num_samples)#le o arquivo de fato
	wav_file.close()
	#unpack descodifica o conteudo do arquivo de audio que geralmente e gravado 
	#em blocos de numeros hexadecimais 
	data = struct.unpack('{n}h'.format(n=num_samples), data)
	data = np.array(data)
	return data

mix =  openfile(file1) + openfile(file2)

fourier_data = np.fft.fft(mix) #roda a transformada de fourier

#retorna um array com os valores absolutos dos numeros complexos de cada frequencia
frequencies = np.abs(fourier_data) 


plt.plot(frequencies)
plt.title("Frequencias encontradas")
plt.xlim(0,1500)
plt.show()