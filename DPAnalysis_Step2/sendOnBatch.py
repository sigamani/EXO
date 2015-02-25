#! /usr/bin/env python
import os
import sys
import re
import time


pwd = os.environ['PWD']


dataset_name        = ['Run2012A', 'Run2012B_1', 'Run2012B_2', 'Run2012B_3', 'Run2012B_4', 
					   'Run2012C_1', 'Run2012C_2', 'Run2012C_3', 'Run2012C_4', 'Run2012C_5', 
					   'Run2012D_1', 'Run2012D_2', 'Run2012D_3', 'Run2012D_4', 'Run2012D_5', 
					   'GMSB_Lambda-140_CTau-10','GMSB_Lambda-140_CTau-100','GMSB_Lambda-140_CTau-1000', 'GMSB_Lambda-140_CTau-2000', 'GMSB_Lambda-140_CTau-50', 'GMSB_Lambda-140_CTau-500', 
					   'GMSB_Lambda-160_CTau-10', 'GMSB_Lambda-160_CTau-100', 'GMSB_Lambda-160_CTau-1000', 'GMSB_Lambda-160_CTau-2000', 'GMSB_Lambda-160_CTau-50', 'GMSB_Lambda-160_CTau-500', 
					   'GMSB_Lambda-180_CTau-10', 'GMSB_Lambda-180_CTau-2000', 'GMSB_Lambda-180_CTau-250', 'GMSB_Lambda-180_CTau-50', 'GMSB_Lambda-180_CTau-500', 
					   'G_Pt-120to170', 'G_Pt-170to300', 'G_Pt-300to470', 'G_Pt-470to800', 'G_Pt-50to80', 'G_Pt-80to120',
					   'QCD_Pt-80to120', 'QCD_Pt-120to170', 'QCD_Pt-170to300','QCD_Pt-300to470','QCD_Pt-470to600', 'QCD_Pt-600to800','QCD_Pt-800to1000', 'QCD_Pt-1000to1400', 
			           'TTJets']


dataset_name_nodata        = ['GMSB_Lambda-140_CTau-10','GMSB_Lambda-140_CTau-100','GMSB_Lambda-140_CTau-1000', 'GMSB_Lambda-140_CTau-2000', 'GMSB_Lambda-140_CTau-50', 'GMSB_Lambda-140_CTau-500',
                                           'GMSB_Lambda-160_CTau-10', 'GMSB_Lambda-160_CTau-100', 'GMSB_Lambda-160_CTau-1000', 'GMSB_Lambda-160_CTau-2000', 'GMSB_Lambda-160_CTau-50', 'GMSB_Lambda-160_CTau-500',
                                           'GMSB_Lambda-180_CTau-10', 'GMSB_Lambda-180_CTau-2000', 'GMSB_Lambda-180_CTau-250', 'GMSB_Lambda-180_CTau-50', 'GMSB_Lambda-180_CTau-500',
                                           'G_Pt-120to170', 'G_Pt-170to300', 'G_Pt-300to470', 'G_Pt-470to800', 'G_Pt-50to80', 'G_Pt-80to120',
                                           'QCD_Pt-80to120', 'QCD_Pt-120to170', 'QCD_Pt-170to300','QCD_Pt-300to470','QCD_Pt-470to600', 'QCD_Pt-600to800','QCD_Pt-800to1000', 'QCD_Pt-1000to1400',
                                   'TTJets']


dataset_name_inverted = ['Run2012A', 'Run2012B_1', 'Run2012B_2', 'Run2012B_3', 'Run2012B_4',
                                           'Run2012C_1', 'Run2012C_2', 'Run2012C_3', 'Run2012C_4', 'Run2012C_5',
                                           'Run2012D_1', 'Run2012D_2', 'Run2012D_3', 'Run2012D_4', 'Run2012D_5']


queue              	= "1nh" 
executable         	= "tmp/main" 

destinationfolder       = "/../DPAnalysis_Step3/v24triggered/"

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
    #outputfile.write("mv "+dataset_name[z]+".root "+outputdir+"/output/;") 
    outputfile.write("mv "+dataset_name[z]+".root "+pwd+destinationfolder)
    outputfile.close
    os.system("echo Submitting "+dataset_name[z]+" to batch queue")
    os.system("bsub -q 1nh -o "+outputdir+"/log/"+dataset_name[z]+".log source "+outputname)

#isolated photons, low met
for z in range(len(dataset_name_inverted)):

    inputlist = "list2/"+dataset_name[z]+".list"
    outputdir = pwd+"/ntuples/"+dataset_name[z]+"isolow"

    os.system("rm -r "+outputdir)
    os.system("mkdir -p "+outputdir)
    os.system("mkdir -p "+outputdir+"/log/")
    os.system("mkdir -p "+outputdir+"/input/")
    os.system("mkdir -p "+outputdir+"/output/")
    os.system("mkdir -p "+outputdir+"/src/")

    outputname = outputdir+"/src/"+dataset_name[z]+"isolow.src"
    outputfile = open(outputname,'w')
    outputfile.write('#!/bin/bash\n')
    outputfile.write('export SCRAM_ARCH=slc6_amd64_gcc472\n')
    outputfile.write('cd '+pwd+'; eval `scramv1 runtime -sh`; \n')
    outputfile.write("./"+executable+" "+inputlist+" "+dataset_name[z]+"isolow;")
    outputfile.write("mv "+dataset_name[z]+"isolow.root "+pwd+destinationfolder)
    outputfile.close
    os.system("echo Submitting "+dataset_name[z]+"isolow to batch queue")
    os.system("bsub -q 1nh -o "+outputdir+"/log/"+dataset_name[z]+"isolow.log source "+outputname)

#fake photons, high met
for z in range(len(dataset_name_inverted)):

    inputlist = "list2/"+dataset_name[z]+".list"
    outputdir = pwd+"/ntuples/"+dataset_name[z]+"fakehigh"

    os.system("rm -r "+outputdir)
    os.system("mkdir -p "+outputdir)
    os.system("mkdir -p "+outputdir+"/log/")
    os.system("mkdir -p "+outputdir+"/input/")
    os.system("mkdir -p "+outputdir+"/output/")
    os.system("mkdir -p "+outputdir+"/src/")

    outputname = outputdir+"/src/"+dataset_name[z]+"fakehigh.src"
    outputfile = open(outputname,'w')
    outputfile.write('#!/bin/bash\n')
    outputfile.write('export SCRAM_ARCH=slc6_amd64_gcc472\n')
    outputfile.write('cd '+pwd+'; eval `scramv1 runtime -sh`; \n')
    outputfile.write("./"+executable+" "+inputlist+" "+dataset_name[z]+"fakehigh;")
    outputfile.write("mv "+dataset_name[z]+"fakehigh.root "+pwd+destinationfolder)
    outputfile.close
    os.system("echo Submitting "+dataset_name[z]+"fakehigh to batch queue")
    os.system("bsub -q 1nh -o "+outputdir+"/log/"+dataset_name[z]+"fakehigh.log source "+outputname)

#fake photons, low met
for z in range(len(dataset_name_inverted)):

    inputlist = "list2/"+dataset_name[z]+".list"
    outputdir = pwd+"/ntuples/"+dataset_name[z]+"fakelow"

    os.system("rm -r "+outputdir)
    os.system("mkdir -p "+outputdir)
    os.system("mkdir -p "+outputdir+"/log/")
    os.system("mkdir -p "+outputdir+"/input/")
    os.system("mkdir -p "+outputdir+"/output/")
    os.system("mkdir -p "+outputdir+"/src/")

    outputname = outputdir+"/src/"+dataset_name[z]+"fakelow.src"
    outputfile = open(outputname,'w')
    outputfile.write('#!/bin/bash\n')
    outputfile.write('export SCRAM_ARCH=slc6_amd64_gcc472\n')
    outputfile.write('cd '+pwd+'; eval `scramv1 runtime -sh`; \n')
    outputfile.write("./"+executable+" "+inputlist+" "+dataset_name[z]+"fakelow;")
    outputfile.write("mv "+dataset_name[z]+"fakelow.root "+pwd+destinationfolder)
    outputfile.close
    os.system("echo Submitting "+dataset_name[z]+"fakelow to batch queue")
    os.system("bsub -q 1nh -o "+outputdir+"/log/"+dataset_name[z]+"fakelow.log source "+outputname)


# for z in range(len(dataset_name_nodata)):

#     inputlist = "list2/"+dataset_name_nodata[z]+".list"
#     outputdir = pwd+"/ntuples/"+dataset_name_nodata[z]

#     os.system("rm -r "+outputdir)
#     os.system("mkdir -p "+outputdir)
#     os.system("mkdir -p "+outputdir+"/log/")
#     os.system("mkdir -p "+outputdir+"/input/")
#     os.system("mkdir -p "+outputdir+"/output/")
#     os.system("mkdir -p "+outputdir+"/src/")

#     outputname = outputdir+"/src/"+dataset_name_nodata[z]+".src"
#     outputfile = open(outputname,'w')
#     outputfile.write('#!/bin/bash\n')
#     outputfile.write('export SCRAM_ARCH=slc6_amd64_gcc472\n')
#     outputfile.write('cd '+pwd+'; eval `scramv1 runtime -sh`; \n')
#     outputfile.write("./"+executable+" "+inputlist+" "+dataset_name_nodata[z]+";")
#     #outputfile.write("mv "+dataset_name_nodata[z]+".root "+outputdir+"/output/;")                                                                                                                                                                    
#     outputfile.write("mv "+dataset_name_nodata[z]+".root "+pwd+destinationfolder)
#     outputfile.close
#     os.system("echo Submitting "+dataset_name_nodata[z]+" to batch queue")
#     os.system("bsub -q 1nh -o "+outputdir+"/log/"+dataset_name_nodata[z]+".log source "+outputname)
