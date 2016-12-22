
import wave
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from python_speech_features import mfcc
from sklearn.ensemble import AdaBoostClassifier
import pyaudio
import wave
import struct

i = 0
j = 0

"""The following two loops calculate the MFCC coefficients for the audio signal, by looping over the wave files. The MFCC coeffs are plotted, and stored to use in the learning algorithm """


output_anything = [0 for k in range(12)]
output_bread = [0 for k in range(12)]
wav_list_anything = ['Wav files - Anything/pronunciation_en_anything (1).wav', 'Wav files - Anything/pronunciation_en_anything (2).wav', 'Wav files - Anything/pronunciation_en_anything (3).wav', 'Wav files - Anything/pronunciation_en_anything (4).wav', 'Wav files - Anything/pronunciation_en_anything (5).wav', 'Wav files - Anything/pronunciation_en_anything (6).wav', 'Wav files - Anything/pronunciation_en_anything (7).wav', 'Wav files - Anything/pronunciation_en_anything (8).wav', 'Wav files - Anything/pronunciation_en_anything (9).wav', 'Wav files - Anything/pronunciation_en_anything (10).wav', 'Wav files - Anything/pronunciation_en_anything (11).wav', 'Wav files - Anything/pronunciation_en_anything (12).wav']
for wav_file in wav_list_anything:
	wf = wave.open(wav_file)
	fs_anything, data_anything = wavfile.read(wav_file) # load the data
	mfcc_feat_anything = mfcc(data_anything,fs_anything)
	reshape_anything = mfcc_feat_anything.reshape(1,-1)
	# plt.plot(mfcc_feat_anything)
	# plt.title('Anything')
	# plt.show()
	output_anything[i] = reshape_anything
	i += 1
	wf.close()
np.array(output_anything)
wav_list_bread = ['Wav Files- Bread/pronunciation_en_bread (1).wav', 'Wav Files- Bread/pronunciation_en_bread (2).wav', 'Wav Files- Bread/pronunciation_en_bread (3).wav', 'Wav Files- Bread/pronunciation_en_bread (4).wav', 'Wav Files- Bread/pronunciation_en_bread (5).wav', 'Wav Files- Bread/pronunciation_en_bread (6).wav', 'Wav Files- Bread/pronunciation_en_bread (7).wav', 'Wav Files- Bread/pronunciation_en_bread (8).wav', 'Wav Files- Bread/pronunciation_en_bread (9).wav', 'Wav Files- Bread/pronunciation_en_bread (10).wav', 'Wav Files- Bread/pronunciation_en_bread (11).wav', 'Wav Files- Bread/pronunciation_en_bread (12).wav']
for wav_file in wav_list_bread:
	wf = wave.open(wav_file)
	fs_bread, data_bread = wavfile.read(wav_file) # load the data
	mfcc_feat_bread = mfcc(data_bread,fs_bread)
	reshape_bread = mfcc_feat_bread.reshape(1,-1)
	# d_mfcc_feat = delta(mfcc_feat, 2)
	# plt.plot(mfcc_feat_bread)
	# plt.title('Bread')
	# plt.show()
	output_bread[j] = reshape_bread
	j += 1
	wf.close()

np.array(output_bread)

output = [0 for k in range(len(output_anything)+len(output_bread))]

for j in range(len(output)):
	if j < len(output_anything):
		output[j] = output_anything[j]
	else:
		output[j] = output_bread[j-len(output_anything)]

y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]



temp_X_test = np.array([output[2*i] for i in range(int(len(output)/2))])
Y_test =  [y[2*i] for i in range(int(len(y)/2))]

temp_X_train = np.array([output[2*i+1] for i in range(int(len(output)/2))])
Y_train = [y[2*i+1] for i in range(int(len(y)/2))]

dataset_size_train = len(temp_X_train)
X_train = temp_X_train.reshape(dataset_size_train,-1)

dataset_size_test = len(temp_X_test)
X_test = temp_X_test.reshape(dataset_size_test,-1)

np.array(X_train)
np.array(X_test)
np.array(Y_train)
np.array(Y_test)



clf = AdaBoostClassifier(None,n_estimators=50, learning_rate=1.0, algorithm='SAMME.R')
clf.fit(X_train,Y_train)
a = clf.score(X_test,Y_test)

print("The accuracy of your test data is",a)

CHANNELS = 1
RATE = 16000
WIDTH = 2
DURATION = 4

N = DURATION*RATE

p = pyaudio.PyAudio()

stream = p.open(format = p.get_format_from_width(WIDTH),
                channels = CHANNELS,
                rate = RATE,
                input = True,
                output = False)

print("*******START********")

output_value = []

for n in range(0,N):

	input_string = stream.read(1)

	input_tuple = struct.unpack('h',input_string)

	input_value = input_tuple[0]

	output_value.append(input_value)

print("**** Done ****")

stream.stop_stream()
stream.close()
p.terminate()


for w in range(len(output_value)):
	if output_value[w] == max(output_value):
		value = w
		break


required_stuff = np.array(output_value[value-500:value+12300])


mfcc_required_stuff = mfcc(required_stuff,RATE)
reshape_required_stuff = mfcc_required_stuff.reshape(1,-1)
# plt.plot(mfcc_required_stuff)
# plt.title("MFCC plot of your speech signal")
# plt.show()

b = clf.predict(reshape_required_stuff)

if b == 1:
	print("The word spoken by you is - Bread")
else:
	print("The word spoken by you is - Anything")