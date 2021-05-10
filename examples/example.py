import manyq as mq
import numpy as np


# angles = np.array([[np.pi/3,np.pi/2,2*np.pi/3]])
omega = np.array([[np.pi/3,np.pi/2,2*np.pi/3],[-np.pi/3,-np.pi/2,2*np.pi/3]])
theta = np.array([-np.pi/3,np.pi/3])
mq.initQreg(2,omega.shape[1])
mq.SX(0)
mq.SX(1)
# mq.RZ(0,angles)
mq.RZ(0,omega[0])
mq.RZ(0,theta[0])
mq.RZ(1,omega[1])
mq.RZ(1,theta[1])
# mq.fSIM(0,1,angles,angles)
mq.SX(0)
mq.SX(1)
mq.measureAll()
shots = mq.makeShots(100)

np.set_printoptions(precision=2, suppress=True)
print(mq.Qreg.inQ,"\n")
print(mq.Qreg.mQ,'\n')
# print(shots)
