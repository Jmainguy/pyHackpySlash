#!/usr/bin/python
from ConfigParser import RawConfigParser
config = RawConfigParser()
def weapon(file):
	config.read(file)
	weapon = config.get('character', 'weapon')
	return weapon
def name(file):
	config.read(file)
	name = config.get('character', 'name')
	return name
def health(file):
	config.read(file)
	health = config.get('character', 'health')
	return health
def dex(file):
	config.read(file)
	dex = config.get('character', 'dexterity')
	return dex
