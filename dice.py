#!/usr/bin/python
import random

def attackroll():
	attackdice = 1
	attackdicesides = 20
	RANDOM = random.randint(1, attackdicesides)
	return RANDOM
def damageroll():
	damagedice = 1
	damagesides = 6
	RANDOM = random.randint(1, damagesides)
	return RANDOM
