'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC_t = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print(PC_t.show_approx())

# P(Cavity|catch) = P(Cavity and catch) / P(catch) = (0.108 + 0.072) / (0.108 + 0.016 + 0.072 + 0.144) = 0.5294
PC_c = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC_c.show_approx())

two_coins = 0.5*0.5  # probability of any given result of flipping two coins
C = JointProbDist(['coin1', 'coin2'])
C[T, T] = 0.25
C[T, F] = 0.25
C[F, T] = 0.25
C[F, F] = 0.25

PH_h = enumerate_joint_ask('coin1', {'coin2': T}, C)
print(PH_h.show_approx())

# yes, this answer makes sense
