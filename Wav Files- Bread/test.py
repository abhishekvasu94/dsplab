
import wave
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt 
import abcd

# use a loop:

wav_list = ['pronunciation_en_bread(1).wav', 'pronunciation_en_bread(2).wav']
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
	
