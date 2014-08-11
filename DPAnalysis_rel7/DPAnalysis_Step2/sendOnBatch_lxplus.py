#! /usr/bin/env python
import os
import sys
import re
import time


pwd = os.environ['PWD']


dataset_name 		= ['GMSB_L180-CTAU500'] 
queue               	= "1nh" 
executable         	= "tmp/main" 

for z in range(len(dataset_name)):

    inputlist = "list/"+dataset_name[z]
    outputdir = pwd+"/ntuples/"+dataset_name[z] 

    os.system("rm -r "+outputdir)
    os.system("mkdir -p "+outputdir)
    os.system("mkdir -p "+outputdir+"/log/")
    os.system("mkdir -p "+outputdir+"/input/")
    os.system("mkdir -p "+outputdir+"/output/")
    os.system("mkdir -p "+outputdir+"/src/")


    input = open(inputlist)
    inputfiles = input.readlines()

    ijob=0
    
    while (len(inputfiles) > 0):
        inputfilename = outputdir+"/input/input_"+str(ijob)
        inputfile = open(inputfilename,'w')
        for line in range(min(1,len(inputfiles))):
            ntpfile = inputfiles.pop()
            if ntpfile != '':
                inputfile.write(ntpfile)
    
        inputfile.close()


        output     = dataset_name[z]+"_"+str(ijob)
        outputname = outputdir+"/src/"+output+".src"
        outputfile = open(outputname,'w')
        outputfile.write('#!/bin/bash\n')
        outputfile.write('export SCRAM_ARCH=slc6_amd64_gcc472\n')
        outputfile.write('cd '+pwd+'; eval `scramv1 runtime -sh`; source setup.sh; \n')
        outputfile.write("./"+executable+" list/"+dataset_name[z]+" "+dataset_name[z]+";")
        outputfile.close
        os.system("echo bsub -q 1nd -o "+outputdir+"/log/"+output+".log source "+outputname)
        os.system("bsub -q 1nd -o "+outputdir+"/log/"+output+".log source "+outputname)
        ijob = ijob+1
                                                                                                                                                                                
        continue

