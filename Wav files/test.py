
import wave
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import abcd

# use a loop:

wav_list = ['pronunciation_en_anything (1).wav', 'pronunciation_en_anything (2).wav', 'pronunciation_en_anything (3).wav', 'pronunciation_en_anything (4).wav', 'pronunciation_en_anything (5).wav', 'pronunciation_en_anything (6).wav', 'pronunciation_en_anything (7).wav', 'pronunciation_en_anything (8).wav', 'pronunciation_en_anything (9).wav', 'pronunciation_en_anything (10).wav', 'pronunciation_en_anything (11).wav', 'pronunciation_en_anything (12).wav']
for wav_file in wav_list:
	wf = wave.open(wav_file)
	fs, data = wavfile.read(wav_file) # load the data
	X = np.fft.fft(data,16384)
	# abcd.plotstft(wav_file)
	plt.plot(abs(X)/max(abs(X)))
	plt.show()
	# print('File:', wav_file)
	# print(len(data))
	wf.close()
	
