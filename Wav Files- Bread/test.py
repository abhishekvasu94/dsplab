
import wave
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt 
import abcd

# use a loop:

wav_list = ['pronunciation _en_bread(1).wav']
for wav_file in wav_list:
	wf = wave.open(wav_file)
	fs, data = wavfile.read(wav_file) # load the data
	# print(wf.getsampwidth())
	X = np.fft.fft(data,16384)
	# print()
	# abcd.plotstft(wav_file)
	plt.plot(abs(X)/max(abs(X)))
	plt.show()
	# print('File:', wav_file)
	# print(len(data))
	wf.close()
	
