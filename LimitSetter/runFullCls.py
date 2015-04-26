#! /usr/bin/env python
import os
import sys
import re
import time


pwd = os.environ['PWD']
scram = os.environ['SCRAM_ARCH']

TMP_DIR = "/tmp/sigamani/"

#signal_point 		= [ 'L180CT1','L180CT10', 'L180CT50','L180CT250','L180CT500','L180CT2000',
#			   			'L160CT1', 'L160CT10', 'L160CT100','L160CT500','L160CT1000','L160CT2000',
#			   			'L140CT1','L140CT10', 'L140CT100','L140CT500','L140CT1000','L140CT2000'] 

signal_point 		= ['L140CT2000']

for z in range(len(signal_point)):


        outputdir = pwd + "/DATACARDS/"
        output = "datacard-"+str(signal_point[z])
        outputname = outputdir+"/"+output+".src"

        outputfile = open(outputname,'w')
        outputfile.write('#!/bin/bash\n')
        outputfile.write('export SCRAM_ARCH'+scram+'; \n')
        outputfile.write('cd '+outputdir+'; eval `scramv1 runtime -sh`; \n')  
        outputfile.write('cd '+TMP_DIR+'; \n') 
        outputfile.write('cp '+pwd+'/combine .; \n') 
        outputfile.write('cp '+pwd+'/limit_V3 .; \n') 
        outputfile.write('cp '+outputdir+'/'+output+'.txt . ; \n')
        outputfile.write('cp '+outputdir+'/simple-shapes-TH1'+str(signal_point[z])+'.root . ; \n') 
        outputfile.write('./limit_V3 '+output+'.txt ; \n') 
        outputfile.write('hadd -f '+outputdir+'/FULL_CLS_RESULT_'+str(signal_point[z])+'.root higgsCombineTest.HybridNew.mH120.* ; \n') 
        outputfile.write('cp higgsCombineTest.Asymptotic.mH120.root '+outputdir+'/ASYMPTOTIC_CLS_RESULT_'+str(signal_point[z])+'.root; \n')
        outputfile.write('rm higgsCombineTest.HybridNew.mH120.* ; \n') 
        outputfile.write('cp datacard-'+str(signal_point[z])+'.txt.result.txt '+outputdir+'/RESULT_'+str(signal_point[z])+'.txt; \n')
        outputfile.write('rm *root; \n')
        outputfile.close
        os.system("echo bsub -q 2nd -o "+outputdir+"/"+output+".log source "+outputname)
        os.system("bsub -q 2nd -o "+outputdir+"/"+output+".log source "+outputname)
