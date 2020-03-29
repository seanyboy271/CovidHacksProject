API is where all of the backend data processing things should go. The api.py is the a barebones API that will communicate with the website.
My hope is to essentially have it import one "main" method from a file that will do all the processing, and return an object that contains all the data we need. 

Web is where the web app's source code lives. Theres not much to do with this until we have processing done.  

Important Data Processing Files: 
-
- CovidHacksProject/API/Pre-processing/relevant-data/needMeta/MakeMeta.py 
    - Responsible for creating \<virus>\_meta.tsv files that will be loaded into augur
- CovidHacksProject/API/Pre-processing/relevant-data/needMeta/makeNewFasta.py
    - Responsible for reformatting the fasta files
- CovidHacksProject/API/Pre-processing/VirusDataNew/runAugur.py
    - Automatically runs augur commands for each virus
- CovidHacksProject/API/Pre-processing/VirusDataNew/ParseVirusData.py 
    - Creates final \<virus>\.json files based on Augur results
    
Process to get final .json:
- 
   - Upload <virus>.fasta files into a directory 
   - Edit MakeMeta.py so that it look for the correct virus names (Note: There are 2 parsing methods that are being used right now. Depending on the formatting of your fasta files, new parsing methods may need to be created. )
   - Run MakeMeta.py from the directory with all your fasta files 
   - Edit makeNewFasta.py in the same way as MakeMeta.py
   - run makeNewFasta.py in the same directory as all your fasta files
   - Edit config files in VirusNewData to fit your data and drop the config directory into the same directory as using to run MakeMeta and makeNewFasta
   - run runAugur.py (This must be done in linux or there will be errors)
   - Once this is complete (it may take a while),edit ParseVirusData.py to contain the proper virus names.
   - Run ParseVirusData.py
   - This should create the final json files, each named \<virus>\.json
