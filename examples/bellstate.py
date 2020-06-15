import manyq as mq
import numpy as np

mq.initQreg(2,3)
mq.H(1)
mq.CX(1,0)
mq.measureAll()


np.set_printoptions(precision=2)

print(mq.Qreg.inQ,'\n')
print(mq.Qreg.mQ,'\n')
print(mq.makeShots(2000))
