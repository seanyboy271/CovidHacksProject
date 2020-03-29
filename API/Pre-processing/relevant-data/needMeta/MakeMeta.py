import os
import re
import csv
# strain
# virus
# accession
# collection_date
# region
# country
# division
# location
# source
# locus
# authors
# url
# title
# journal
# puburl
def ParseName(name):
    curr = name.split('|')
    return curr[0:6]

def parseDengue(case):
    componentList = re.split(r'\|', case)
    #print(componentList)
    caseName = componentList.pop(0)
    #print(caseName)

    disease = componentList.pop(0)
    Assension = componentList.pop(0)
    collection_date = componentList.pop(0)
    region = componentList.pop(0)
    country = componentList.pop(0)
    return [caseName, disease, Assension, collection_date, region, country]

def parseSeasonal(case):
    region = '?'
    componentList = re.split(r'\|', case)
    # print(componentList)
    Assension = componentList.pop(0)
    caseName = componentList.pop(0)
    disease = componentList.pop(0)
    collection_date = componentList.pop(0)
    country = componentList.pop(0)
    return [caseName, disease, Assension, collection_date, region, country]






if __name__ == "__main__":
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    files = list(filter(lambda file: ".fasta" in file and 'new' not in file, files))

    print(files)

    tsvHeader = ['strain', 'virus', 'assention', 'date', 'region', 'country']

    state = 0
    name = ""

    for file in files:
        print(file)
        fullInfo = []
        if "dengue" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseDengue(case)
                fullInfo.append(caseArr)
            with open('dengue_meta.tsv', 'w+', newline='') as f:
                f.truncate(0)
                tsv_writer = csv.writer(f, delimiter='\t')
                tsv_writer.writerow(tsvHeader)
                for case in fullInfo:
                    tsv_writer.writerow(case)
                f.close()

        elif "ebola" in file:
            #print("EBOLA")
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseDengue(case)
                fullInfo.append(caseArr)
            with open('ebola_meta.tsv', 'w+', newline='') as f:
                f.truncate(0)
                tsv_writer = csv.writer(f, delimiter='\t')
                tsv_writer.writerow(tsvHeader)
                for case in fullInfo:
                    tsv_writer.writerow(case)
                f.close()

        elif "h5n1" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseDengue(case)
                fullInfo.append(caseArr)
            with open('h5n1_ha_meta.tsv', 'w+', newline='') as f:
                f.truncate(0)
                tsv_writer = csv.writer(f, delimiter='\t')
                tsv_writer.writerow(tsvHeader)
                for case in fullInfo:
                    tsv_writer.writerow(case)
                f.close()

        elif "measles" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseDengue(case)
                fullInfo.append(caseArr)
            with open('measles_meta.tsv', 'w+', newline='') as f:
                f.truncate(0)
                tsv_writer = csv.writer(f, delimiter='\t')
                tsv_writer.writerow(tsvHeader)
                for case in fullInfo:
                    tsv_writer.writerow(case)
                f.close()

        elif "mers" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseDengue(case)
                fullInfo.append(caseArr)
            with open('mers_meta.tsv', 'w+', newline='') as f:
                f.truncate(0)
                tsv_writer = csv.writer(f, delimiter='\t')
                tsv_writer.writerow(tsvHeader)
                for case in fullInfo:
                    tsv_writer.writerow(case)
                f.close()

        elif "mumps" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseDengue(case)
                fullInfo.append(caseArr)
            with open('mumps_meta.tsv', 'w+', newline='') as f:
                f.truncate(0)
                tsv_writer = csv.writer(f, delimiter='\t')
                tsv_writer.writerow(tsvHeader)
                for case in fullInfo:
                    tsv_writer.writerow(case)
                f.close()

        elif "229e" in file:
            #Assention
            # case_name
            # dieasea
            #collection data
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseSeasonal(case)
                fullInfo.append(caseArr)
            with open('229e_meta.tsv', 'w+', newline='') as f:
                f.truncate(0)
                tsv_writer = csv.writer(f, delimiter='\t')
                tsv_writer.writerow(tsvHeader)
                for case in fullInfo:
                    tsv_writer.writerow(case)
                f.close()


        elif "hku1" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseSeasonal(case)
                fullInfo.append(caseArr)
            with open('hku1_meta.tsv', 'w+', newline='') as f:
                f.truncate(0)
                tsv_writer = csv.writer(f, delimiter='\t')
                tsv_writer.writerow(tsvHeader)
                for case in fullInfo:
                    tsv_writer.writerow(case)
                f.close()

        elif "nl63" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseSeasonal(case)
                fullInfo.append(caseArr)
            with open('nl63_meta.tsv', 'w+', newline='') as f:
                f.truncate(0)
                tsv_writer = csv.writer(f, delimiter='\t')
                tsv_writer.writerow(tsvHeader)
                for case in fullInfo:
                    tsv_writer.writerow(case)
                f.close()

        elif "oc43" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseSeasonal(case)
                fullInfo.append(caseArr)
            with open('oc43_meta.tsv', 'w+', newline='') as f:
                f.truncate(0)
                tsv_writer = csv.writer(f, delimiter='\t')
                tsv_writer.writerow(tsvHeader)
                for case in fullInfo:
                    tsv_writer.writerow(case)
                f.close()

        elif "h3n2_ha" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseDengue(case)
                fullInfo.append(caseArr)
            with open('h3n2_ha_meta.tsv', 'w+', newline='') as f:
                f.truncate(0)
                tsv_writer = csv.writer(f, delimiter='\t')
                tsv_writer.writerow(tsvHeader)
                for case in fullInfo:
                    tsv_writer.writerow(case)
                f.close()

        elif "h3n2_na" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseDengue(case)
                fullInfo.append(caseArr)
            with open('h3n2_na_meta.tsv', 'w+', newline='') as f:
                f.truncate(0)
                tsv_writer = csv.writer(f, delimiter='\t')
                tsv_writer.writerow(tsvHeader)
                for case in fullInfo:
                    tsv_writer.writerow(case)
                f.close()

        elif "zika" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseDengue(case)
                fullInfo.append(caseArr)
            with open('zika_meta.tsv', 'w+', newline='') as f:
                f.truncate(0)
                tsv_writer = csv.writer(f, delimiter='\t')
                tsv_writer.writerow(tsvHeader)
                for case in fullInfo:
                    tsv_writer.writerow(case)
                f.close()

        else:
            break;
            #print("FILE",file)
            exit()




