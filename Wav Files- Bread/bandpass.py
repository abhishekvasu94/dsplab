# play_wav_mono.py
import pyaudio
import wave
import struct
import math

from myfunctions import clip16

def bpf1(filename):

    wavfile = filename
    # wavfile = 'sin01_mono.wav'

    # print("Play the wave file %s." % wavfile)

    # Open wave file (should be mono channel)
    wf = wave.open( wavfile, 'rb' )
    output_value = []

    # Read the wave file properties
    # num_channels = wf.getnchannels()       	# Number of channels
    # RATE = wf.getframerate()                # Sampling rate (frames/second)
    # signal_length  = wf.getnframes()       	# Signal length
    # width = wf.getsampwidth()       		# Number of bytes per sample

    # print("The file has %d channel(s)."            % num_channels)
    # print("The frame rate is %d frames/second."    % RATE)
    # print("The file has %d frames."                % signal_length)
    # print("There are %d bytes per sample."         % width)


    # Difference equation coefficients
    b0 =  0.0026
    b1 = -0.0181
    b2 =  0.0550
    b3 = -0.0906
    b4 =  0.0757
    b5 =  0.0
    b6 = -0.0757
    b7 =  0.0906
    b8 = -0.0550
    b9 =  0.0181
    b10= -0.0026

    # a0 =  1.000000000000000
    a1 = -8.7729
    a2 =  35.1359
    a3 = -84.5583
    a4 =  135.3749
    a5 = -150.6241
    a6 =  117.9497
    a7 = -64.1918
    a8 =  23.2409
    a9 = -5.0565
    a10=  0.5023

    # Initialization
    x1 = 0.0
    x2 = 0.0
    x3 = 0.0
    x4 = 0.0
    x5 = 0.0
    x6 = 0.0
    x7 = 0.0
    x8 = 0.0
    x9 = 0.0
    x10 = 0.0
    y1 = 0.0
    y2 = 0.0
    y3 = 0.0
    y4 = 0.0
    y5 = 0.0
    y6 = 0.0
    y7 = 0.0
    y8 = 0.0
    y9 = 0.0
    y10 = 0.0

    p = pyaudio.PyAudio()

    # Open audio stream
    # stream = p.open(format      = pyaudio.paInt16,
    #                 channels    = num_channels,
    #                 rate        = RATE,
    #                 input       = False,
    #                 output      = False )

    # Get first frame
    input_string = wf.readframes(1)

    while input_string != '':

        # Convert string to number
        input_tuple = struct.unpack('h', input_string)  # One-element tuple
        input_value = input_tuple[0]                    # Number

        # Set input to difference equation
        x0 = input_value

        # Difference equation
        y0 = b0*x0 + b1*x1 + b2*x2 + b3*x3 + b4*x4 + b5*x5 + b6*x6 + b7*x7 + b8*x8 + b9*x9 + b10*x10 - a1*y1 - a2*y2 - a3*y3 - a4*y4 -a5*y5 - a6*y6 - a7*y7 - a8*y8 - a9*y9 - a10*y10

        # Delays
        x10 = x9
        x9 = x8
        x8 = x7
        x7 = x6
        x6 = x5
        x5 = x4
        x4 = x3
        x3 = x2
        x2 = x1
        x1 = x0
        y10 = y9
        y9 = y8
        y8 = y7
        y7 = y6
        y6 = y5
        y5 = y4
        y4 = y3
        y3 = y2
        y2 = y1
        y1 = y0

        # Compute output value
        output_value.append(clip16(y0))

        # Convert output value to binary string
        # output_string = struct.pack('h', output_value)  
        # output_string = struct.pack('h', input_value)  

        # Write binary string to audio stream
        # stream.write(output_string)                     

        # Get next frame
        input_string = wf.readframes(1)

    return output_value
    # stream.stop_stream()
    # stream.close()
    # p.terminate()
