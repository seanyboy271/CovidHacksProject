API is where all of the backend data processing things should go. The api.py is the a barebones API that will communicate with the website.
My hope is to essentially have it import one "main" method from a file that will do all the processing, and return an object that contains all the data we need. 

Web is where the web app's source code lives. Theres not much to do with this until we know what we want it to look like. 

Instructions to run api and web app:

Open up 3 command prompts/terminals:
In terminal 1: 
    - Navigate to CovidHacks/API/ 
    - python api.py

In terminal 2:
    - Navigate to CovidHacks/Web/covid_simulation\
    - run npm install (first time only)
    - npm start
    - This should open up a window in your browser that has the website in it.
    - NOTE: You will need to have node.js installed for this to work
 
 In terminal 3: 
    - Navigate to CovidHacks/Web/covid_simulation/node_modules/cors-anywhere
    - node server.js
    - NOTE: You will need to have node.js installed for this to work\
    
Important Files: \ 
- CovidHacksProject/API/Pre-processing/relevant-data/needMeta/MakeMeta.py 
    - Resposible for creating <virus>_meta.tsv files taht will be into augur
- CovidHacksProject/API/Pre-processing/relevant-data/needMeta/makeNewFasta.py
    - Responsible for reformatting teh fasta files
- CovidHacksProject/API/Pre-processing/VirusDataNew/runAugur.py
    - Automatically runs augur commands for each virus
- CovidHacksProject/API/Pre-processing/VirusDataNew/ParseVirusData.py 
    - Creates final <virus>.json files based on Augur results


 
