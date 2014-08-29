import get_sites
import subprocess
import append
import os
import append
import add_to_db
import re


def call_structure(sites, indices):
	'''Now we execute structure'''
	print 'input file generated'
	new_lines = [re.sub(r'#define NUMLOCI \d{3,4}','#define NUMLOCI %d' % sites, line) for line in open('mainparams')]
	final = [re.sub(r'#define NUMINDS \d{1,2}','#define NUMINDS %d' % indices, line) for line in new_lines]
	outfile = open('mainparams','w')
	outfile.writelines(["%s" % item  for item in final])
	outfile.close()
	print 'Parameter file generated'
	print 'Running Structure. This may take a few minutes'
	os.system("./structure") 
	print 'Structure run complete'


if __name__ == '__main__':
    call_structure(sites, indices)
