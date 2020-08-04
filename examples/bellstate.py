import manyq as mq
import numpy as np

mq.initQreg(2,3)
mq.H(1)
mq.CX(1,0)
mq.measureAll()


np.set_printoptions(precision=2)

print(mq.Qreg.inQ,'\n') 
# quantum state (vector of amplitudes)

print(mq.Qreg.mQ,'\n') 
# measurement (vector of probabilities)

print(mq.makeShots(2000)) 
# 2000 shots (nb of occurence of each bit string) 
