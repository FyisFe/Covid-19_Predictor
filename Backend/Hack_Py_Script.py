import sys
import math
import json
import numpy as np
from scipy.integrate import odeint

# Fixed parameters
# θ: the ratio of infection ability between E and I
cita = 1
# σ: incubation period
sigama = 1 / 7
# α: death rate
alpha = 0.013
# δI: I -> H rate 
delta_I = 0.133
# γI: I -> R rate (Self-healing)
gamma_I = 0.140
# δq: Eq -> H rate (examine for disease)
delta_q = 0.126
# γH: H -> R rate (post-treatment recovery)
gamma_H = 0.330
# β: infection probobility
beta = 2.1011 * math.pow(10, -8)
# q: quarantined ratio in S
q = 1.8887 * math.pow(10, -7)
# c: contact ratio of E and I
c = 2
# ρ: effective contact coefficient
rou = 1

# Define function to calculate Ordinary Differential Equation Set
def funcSEIRHD(y_list, t):
    Y = np.zeros(8)
    S, E, I, Sq, Eq, H, R, D = y_list
    Y[0] = lamada * Sq - (rou * c * beta + rou * c * q * (1 - beta)) * S * (I + cita * E) - rou * c * (1 - beta) * (1 - q) * S * (I + cita * E) * v * e - (S - S * (I + cita * E) * rou * c) * v * e
    Y[1] = rou * c * beta * (1 - q) * S * (I + cita * E) - sigama * E
    Y[2] = sigama * E - (delta_I + alpha + gamma_I) * I
    Y[3] = rou * c * q * (1 - beta) * S * (I + cita * E) - lamada * Sq
    Y[4] = rou * c * beta * q * S * (I + cita * E) - delta_q * Eq
    Y[5] = delta_I * I + delta_q * Eq - (alpha + gamma_H) * H
    Y[6] = gamma_I * I + gamma_H * H + rou * c * (1 - beta) * (1 - q) * S * (I + cita * E) * v * e + (S - S * (I + cita * E) * rou * c) * v * e
    Y[7] = alpha * I + alpha * H

    return Y


# Get remaining para from Node.js
# Initial susceptible
S_0 = int(sys.argv[1])
# Initial exposed
E_0 = int(sys.argv[2])
# Initial infection
I_0 = int(sys.argv[3])
# Sq: susceptible and quarantined
Sq_0 = int(sys.argv[4])
# Eq: exposed and quarantined
Eq_0 = int(sys.argv[5])
# H: hospitalized
H_0 = int(sys.argv[6])
# Initial recovery
R_0 = int(sys.argv[7])
# D: Death group
D_0 = int(sys.argv[8])
# Time span
T = int(sys.argv[9])
# λ: quarantine contact rate
temp_str = sys.argv[10]
temp_strList = temp_str.split('/')
lamada = float(temp_strList[0]) / float(temp_strList[1])
# v: Vaccination ratio
v = float(sys.argv[11])
# e: Vaccine efficiency
e = float(sys.argv[12])
# Initial values of the system of ODE
INI = (S_0, E_0, I_0, Sq_0, Eq_0, H_0, R_0, D_0)

# Independent variable
t = np.arange(0, T + 1)
# Calculation
result = odeint(funcSEIRHD, INI, t)

# Output flow in JSON
jsonList = []
for i in range(0, 8):
    jsonList.append(result[:, i].tolist())
jsonArr = json.dumps(jsonList, ensure_ascii = False)
print(jsonArr)
