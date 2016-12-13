
import wave
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt 
# import abcd

# use a loop:

wav_list = ['pronunciation_en_bread (1).wav', 'pronunciation_en_bread (2).wav', 'pronunciation_en_bread (3).wav', 'pronunciation_en_bread (4).wav', 'pronunciation_en_bread (5).wav', 'pronunciation_en_bread (6).wav', 'pronunciation_en_bread (7).wav', 'pronunciation_en_bread (8).wav', 'pronunciation_en_bread (9).wav', 'pronunciation_en_bread (10).wav', 'pronunciation_en_bread (11).wav', 'pronunciation_en_bread (12).wav']
for wav_file in wav_list:
	wf = wave.open(wav_file)
	fs, data = wavfile.read(wav_file) # load the data
	# print(wf.getsampwidth())
	X = np.fft.fft(data,16384)
	print(len(data))
	# print()
	# abcd.plotstft(wav_file)
	plt.plot(abs(X)/max(abs(X)))
	plt.show()
	# print('File:', wav_file)
	# print(len(data))
	wf.close()
	
