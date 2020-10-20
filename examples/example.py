import manyq as mq
import numpy as np


angles = np.array([np.pi/3,np.pi/2,2*np.pi/3])

mq.initQreg(2,angles.shape[0])
mq.SX(0)
mq.SX(1)
mq.RZ(0,angles)
# mq.fSIM(0,1,angles,angles)
mq.SX(0)
mq.SX(1)
mq.measureAll()
shots = mq.makeShots(100)

np.set_printoptions(precision=2)

print(mq.Qreg.inQ,"\n")
print(mq.Qreg.mQ,'\n')
print(shots)
