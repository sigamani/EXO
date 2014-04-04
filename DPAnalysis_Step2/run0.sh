rm run.sh
python sendOnBatch.py Run2012B            >> run.sh
python sendOnBatch.py Run2012C            >> run.sh
python sendOnBatch.py Run2012D            >> run.sh
python sendOnBatch.py G_Pt-50to80      	  >> run.sh  
python sendOnBatch.py G_Pt-80to120   	  >> run.sh
python sendOnBatch.py G_Pt-120to170  	  >> run.sh
python sendOnBatch.py G_Pt-170to300  	  >> run.sh
python sendOnBatch.py G_Pt-300to470  	  >> run.sh
python sendOnBatch.py G_Pt-470to800  	  >> run.sh
python sendOnBatch.py QCD_Pt-80to120 	  >> run.sh 
python sendOnBatch.py QCD_Pt-120to170 	  >> run.sh
python sendOnBatch.py QCD_Pt-170to300 	  >> run.sh
python sendOnBatch.py QCD_Pt-300to470     >> run.sh
python sendOnBatch.py QCD_Pt-470to600 	  >> run.sh
python sendOnBatch.py QCD_Pt-600to800 	  >> run.sh
python sendOnBatch.py QCD_Pt-800to1000 	  >> run.sh
python sendOnBatch.py TTJets  		  >> run.sh
python sendOnBatch.py GMSB_L180-CTAU500   >> run.sh