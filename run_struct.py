import subprocess
import append
import os
import append
import add_to_db


def call_structure():
	'''Now we execute structure'''
	append.append()
	add_to_db.add_to_base()
	print 'input file generated'
	os.system("python ../Structure/structure.py -K 2 --input=structure_input.csv --output=ctl_output --prior=logistic --format=str --full cv=2") 

call_structure()
