
import wave
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from python_speech_features import mfcc

i = 0
j = 0

output_anything = [0 for k in range(13)]
output_bread = [0 for k in range(13)]
wav_list_anything = ['Wav files - Anything/pronunciation_en_anything (1).wav', 'Wav files - Anything/pronunciation_en_anything (2).wav', 'Wav files - Anything/pronunciation_en_anything (3).wav', 'Wav files - Anything/pronunciation_en_anything (4).wav', 'Wav files - Anything/pronunciation_en_anything (5).wav', 'Wav files - Anything/pronunciation_en_anything (6).wav', 'Wav files - Anything/pronunciation_en_anything (7).wav', 'Wav files - Anything/pronunciation_en_anything (8).wav', 'Wav files - Anything/pronunciation_en_anything (9).wav', 'Wav files - Anything/pronunciation_en_anything (10).wav', 'Wav files - Anything/pronunciation_en_anything (11).wav', 'Wav files - Anything/pronunciation_en_anything (12).wav']
for wav_file in wav_list_anything:
	wf = wave.open(wav_file)
	fs_anything, data_anything = wavfile.read(wav_file) # load the data
	mfcc_feat_anything = mfcc(data_anything,fs_anything)
	plt.plot(mfcc_feat_anything[0:79,:])
	plt.title('Anything')
	plt.show()
	output_anything[i] = mfcc_feat_anything[0:79,:]
	i += 1
	wf.close()

wav_list_bread = ['Wav Files- Bread/pronunciation_en_bread (1).wav', 'Wav Files- Bread/pronunciation_en_bread (2).wav', 'Wav Files- Bread/pronunciation_en_bread (3).wav', 'Wav Files- Bread/pronunciation_en_bread (4).wav', 'Wav Files- Bread/pronunciation_en_bread (5).wav', 'Wav Files- Bread/pronunciation_en_bread (6).wav', 'Wav Files- Bread/pronunciation_en_bread (7).wav', 'Wav Files- Bread/pronunciation_en_bread (8).wav', 'Wav Files- Bread/pronunciation_en_bread (9).wav', 'Wav Files- Bread/pronunciation_en_bread (10).wav', 'Wav Files- Bread/pronunciation_en_bread (11).wav', 'Wav Files- Bread/pronunciation_en_bread (12).wav']
for wav_file in wav_list_bread:
	wf = wave.open(wav_file)
	fs_bread, data_bread = wavfile.read(wav_file) # load the data
	mfcc_feat_bread = mfcc(data_bread,fs_bread)
	# d_mfcc_feat = delta(mfcc_feat, 2)
	plt.plot(mfcc_feat_bread[0:79,:])
	plt.title('Bread')
	plt.show()
	output_anything[j] = mfcc_feat_anything[0:79,:]
	j += 1
	wf.close()

