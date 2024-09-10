import numpy as np
from Qubit import *
from SingleQubitSimulator import *


def qrng(qubit: Qubit) -> bool:
  #qubit.h()
  result = qubit.measure()
  return result

if __name__ == "__main__":
  qsim = SimulatedQubit()
  for _ in range(10):

    print(qrng(qsim))
