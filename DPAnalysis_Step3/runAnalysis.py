#! /usr/bin/env python
import os
import sys
import re
import time


pwd = os.environ['PWD']



dataset_name 		= ['GMSB_L180-CTAU500']
executable         	= "./tmp/main" 


for z in range(len(dataset_name)):


    inputfile = "root://eoscms//eos/cms/store/caf/user/sigamani/DPAnalysis/v21/"+dataset_name[z]+".root"
    outputdir = pwd+"/batch_output/"+dataset_name[z] 
   	     
    os.system("rm -r "+outputdir)
    os.system("mkdir -p "+outputdir)
    os.system("mkdir -p "+outputdir+"/log/")
    os.system("mkdir -p "+outputdir+"/input/")
    os.system("mkdir -p "+outputdir+"/output/")
    os.system("mkdir -p "+outputdir+"/src/")


    output = dataset_name[z]+"_"+str(stopmass)+"_"+str(lspmass)
    outputname = outputdir+"/src/"+output+".src"
    outputfile = open(outputname,'w')
    outputfile.write('#!/bin/bash\n')
    outputfile.write('export SCRAM_ARCH=slc6_amd64_gcc472\n')
    outputfile.write('cd '+pwd+'; eval `scramv1 runtime -sh`; source setup.sh; \n')
    outputfile.write('cd /tmp/sigamani; \n')
    outputfile.write('cp /afs/cern.ch/work/s/sigamani/public/CMSSW_5_3_14_STOPS/src/Stops-AN-14-067/runAnalysis/'+executable+' .; \n')
    outputfile.write("./"+executable+" "+inputfile+ " "+output+".root " +str(stopmass)+" "+str(lspmass)+";")
    outputfile.write("cp "+output+".root "+outputdir+"/output/ ; rm "+output+".root; ")
    outputfile.close
    os.system("echo bsub -q 1nd -o "+outputdir+"/log/"+output+".log source "+outputname)
    os.system("bsub -q 1nd -o "+outputdir+"/log/"+output+".log source "+outputname)
