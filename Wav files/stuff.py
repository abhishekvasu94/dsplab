import glob
from test1 import *
files = glob.glob('./*.wav')
for ele in files:
    f(ele)
quit()