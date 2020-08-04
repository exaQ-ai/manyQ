## ManyQ
#### A fast quantum computer simulator

Uses SIMD, multicore and GPU to speedup computations

Optimized for Quantum Machine Learning algorithms

ManyQ is the underlying quantum computer simulator of PolyadicQML: 
https://github.com/entropicalabs/polyadicQML



### To install 
```bash
pip install manyq
```

### Quick start

```python
import manyq as mq


mq.initQreg(2)
mq.H(1)
mq.CX(1,0)
mq.measureAll()


print(mq.Qreg.inQ) 
# quantum state (vector of amplitudes)

print(mq.Qreg.mQ) 
# measurement (vector of probabilities)

print(mq.makeShots(2000)) 
# 2000 shots (nb of occurence of each bit string) 
```
