# 
import wave
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from bandpass import bpf1
from python_speech_features import mfcc
# from python_speech_features import delta
from python_speech_features import logfbank
# import abcd

# use a loop:

wav_list = ['pronunciation_en_bread (1).wav', 'pronunciation_en_bread (2).wav', 'pronunciation_en_bread (3).wav', 'pronunciation_en_bread (4).wav', 'pronunciation_en_bread (5).wav', 'pronunciation_en_bread (6).wav', 'pronunciation_en_bread (7).wav', 'pronunciation_en_bread (8).wav', 'pronunciation_en_bread (9).wav', 'pronunciation_en_bread (10).wav', 'pronunciation_en_bread (11).wav', 'pronunciation_en_bread (12).wav']
for wav_file in wav_list:
	wf = wave.open(wav_file)
	fs, data = wavfile.read(wav_file) # load the data
	mfcc_feat = mfcc(data,fs)
	# d_mfcc_feat = delta(mfcc_feat, 2)
	fbank_feat = logfbank(data,fs)
	# print(len(fbank_feat[0]))
	plt.plot(mfcc_feat)
	plt.show()
	# print(wf.getnchannels())
	# stuff = bpf1(wav_file)
	# X = np.fft.fft(data,16384)
	# Y = [0 for i in range(len(X))]
	# Y = [abs(X[i])/max(abs(X)) for i in range(len(X))]
	# for k in range(2000):
	# 	if X[k] == max(X[0:2000]):
	# 		point = k
	# 		break
	# y = np.mean(Y[point-10:point+10])*point
	# print(y)
	# abcd.plotstft(wav_file)
	# plt.plot(abs(X)/max(abs(X)))
	# plt.show()
	# print('File:', wav_file)
	# print(len(data))
	wf.close()
	
