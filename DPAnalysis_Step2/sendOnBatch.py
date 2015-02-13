#! /usr/bin/env python
import os
import sys
import re
import time


pwd = os.environ['PWD']


#dataset_name 		= ['Run2012A', 'Run2012B', 'Run2012C', 'Run2012D', 'GMSB_Lambda-180_CTau-500'] // add the names of the list here 
queue              	= "1nh" 
executable         	= "tmp/main" 

for z in range(len(dataset_name)):

    inputlist = "list2/"+dataset_name[z]+".list"
    outputdir = pwd+"/ntuples/"+dataset_name[z] 

    os.system("rm -r "+outputdir)
    os.system("mkdir -p "+outputdir)
    os.system("mkdir -p "+outputdir+"/log/")
    os.system("mkdir -p "+outputdir+"/input/")
    os.system("mkdir -p "+outputdir+"/output/")
    os.system("mkdir -p "+outputdir+"/src/")

    outputname = outputdir+"/src/"+dataset_name[z]+".src"
    outputfile = open(outputname,'w')
    outputfile.write('#!/bin/bash\n')
    outputfile.write('export SCRAM_ARCH=slc6_amd64_gcc472\n')
    outputfile.write('cd '+pwd+'; eval `scramv1 runtime -sh`; \n')
    outputfile.write("./"+executable+" "+inputlist+" "+dataset_name[z]+";")
    outputfile.close
    os.system("echo bsub -q 1nd -o "+outputdir+"/log/"+dataset_name[z]+".log source "+outputname)
    os.system("bsub -q 1nd -o "+outputdir+"/log/"+dataset_name[z]+".log source "+outputname)
                                                                                                                                                                            
    continue

