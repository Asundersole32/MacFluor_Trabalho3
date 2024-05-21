import math
import numpy as np
import matplotlib.pyplot as plt


def v_saida(g, heigth_t):
    return math.sqrt(2*g*heigth_t)


def vm_out(vm_in, mea, A0, A, v_out):
    frac1 = vm_in/(mea*A)
    frac2 = A0/A
    return frac1 - (frac2 * v_out)


g = 32.2
d0 = 2.5
d0 = d0 * (1/12)
A0 = (3.14 * (d0 ** 2)) / 4
vm_in = 30
mea = 62.4


