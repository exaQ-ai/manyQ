

import manyq as mq 
import numpy as np 
import time, sys

ftime = time.time

def speed(nb_qbits, nb_circuits, repeat=1, depth=2, gpu=False, multicore = False):

    params = np.pi * np.random.rand(depth, nb_qbits, nb_circuits)
    
    start_time = ftime()
    
    for _ in range(repeat):
        mq.initQreg(nb_qbits, nb_circuits, gpu = gpu, multicore = multicore)
        for l in range(depth):
            for i in range(nb_qbits):
                mq.SX(i)
                mq.RZ(i, params[l,i])
                mq.SX(i)

            for i in range(nb_qbits - 1):
                mq.CZ(i, i+1)

        for i in range(nb_qbits):
            mq.SX(i)

        mq.measureAll()

    end_time = ftime()

    return (end_time - start_time)/repeat

if __name__=='__main__':
    
    try: nbqubits = int( sys.argv[1])
    except:    nbqubits = 5
    try: nbcircuits = int( sys.argv[2])
    except: nbcircuits = 10
    try: depth = int( sys.argv[3])
    except: depth = 2

    try: multicore = 'multicore' == sys.argv[4] 
    except: multicore = False

    t = speed(nbqubits, nbcircuits, depth=depth, multicore = multicore)

    print(f"nb qubits={nbqubits}, nb circuits={nbcircuits}, depth={depth}:")
    print(f"milliseconds {t*1000}")
    print(f"     seconds {t}")
    # print(f"     minutes {t/60}")
