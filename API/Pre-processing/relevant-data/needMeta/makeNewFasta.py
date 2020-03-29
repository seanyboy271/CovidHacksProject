import os
import re
import csv

def parseDengue(case):
    componentList = re.split(r'\|', case)
    caseName = componentList.pop(0).strip()

    sequence = componentList.pop()
    sequence = re.split(r'\n', sequence)[1].strip()
    #print(sequence)
    return [caseName, sequence]

def parseSeasonal(case):
    componentList = re.split(r'\|', case)
    Assension = componentList.pop(0)
    caseName = componentList.pop(0).strip()

    sequence = componentList.pop()
    sequence = re.split(r'\n', sequence)[1].strip()
    print(sequence)
    return [caseName, sequence]


if __name__ == "__main__":
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    files = list(filter(lambda file: ".fasta" in file and 'new' not in file, files))

    for file in files:
        #print(file)
        fullInfo = []
        if "dengue" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseDengue(case)
                fullInfo.append(caseArr)
            with open('dengue_new.fasta', 'w+', newline='') as f:
                f.truncate(0)
                for case in fullInfo:
                    new = '>'+ case[0] + '\n' + case[1] + '\n'
                    f.write(new)
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
            with open('ebola_new.fasta', 'w+', newline='') as f:
                f.truncate(0)
                for case in fullInfo:
                    new = '>'+ case[0] + '\n' + case[1] + '\n'
                    f.write(new)
                f.close()

        elif "h5n1" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseDengue(case)
                fullInfo.append(caseArr)
            with open('h5n1_ha_new.fasta', 'w+', newline='') as f:
                f.truncate(0)
                for case in fullInfo:
                    new = '>'+ case[0] + '\n' + case[1] + '\n'
                    f.write(new)
                f.close()

        elif "measles" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseDengue(case)
                fullInfo.append(caseArr)
            with open('measles_new.fasta', 'w+', newline='') as f:
                f.truncate(0)
                for case in fullInfo:
                    new = '>'+ case[0] + '\n' + case[1] + '\n'
                    f.write(new)
                f.close()

        elif "mers" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseDengue(case)
                fullInfo.append(caseArr)
            with open('mers_new.fasta', 'w+', newline='') as f:
                f.truncate(0)
                for case in fullInfo:
                    new = '>'+ case[0] + '\n' + case[1] + '\n'
                    f.write(new)
                f.close()

        elif "mumps" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseDengue(case)
                fullInfo.append(caseArr)
            with open('mumps_new.fasta', 'w+', newline='') as f:
                f.truncate(0)
                for case in fullInfo:
                    new = '>'+ case[0] + '\n' + case[1] + '\n'
                    f.write(new)
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
            with open('229e_new.fasta', 'w+', newline='') as f:
                f.truncate(0)
                for case in fullInfo:
                    new = '>'+ case[0] + '\n' + case[1] + '\n'
                    f.write(new)
                f.close()


        elif "hku1" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseSeasonal(case)
                fullInfo.append(caseArr)
            with open('hku1_new.fasta', 'w+', newline='') as f:
                f.truncate(0)
                for case in fullInfo:
                    new = '>'+ case[0] + '\n' + case[1] + '\n'
                    f.write(new)
                f.close()

        elif "nl63" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseSeasonal(case)
                fullInfo.append(caseArr)
            with open('nl63_new.fasta', 'w+', newline='') as f:
                f.truncate(0)
                for case in fullInfo:
                    new = '>'+ case[0] + '\n' + case[1] + '\n'
                    f.write(new)

                f.close()

        elif "oc43" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseSeasonal(case)
                fullInfo.append(caseArr)
            with open('oc43_new.fasta', 'w+', newline='') as f:
                f.truncate(0)
                for case in fullInfo:
                    new = '>' + case[0] + '\n' + case[1] + '\n'
                    f.write(new)
                f.close()

        elif "h3n2_ha" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseDengue(case)
                fullInfo.append(caseArr)
            with open('h3n2_ha_new.fasta', 'w+', newline='') as f:
                f.truncate(0)
                for case in fullInfo:
                    new = '>'+ case[0] + '\n' + case[1] + '\n'
                    f.write(new)
                f.close()

        elif "h3n2_na" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseDengue(case)
                fullInfo.append(caseArr)
            with open('h3n2_na_new.fasta', 'w+', newline='') as f:
                f.truncate(0)
                for case in fullInfo:
                    new = '>'+ case[0] + '\n' + case[1] + '\n'
                    f.write(new)
                f.close()

        elif "zika" in file:
            currFile = open(file)
            currStr = currFile.read()
            stringList = re.split(r'>', currStr)
            stringList = list(filter(lambda x: x != '', stringList))
            for case in stringList:
                caseArr = parseDengue(case)
                fullInfo.append(caseArr)
            with open('zika_new.fasta', 'w+', newline='') as f:
                f.truncate(0)
                for case in fullInfo:
                    new = '>'+ case[0] + '\n' + case[1] + '\n'
                    f.write(new)
                f.close()

        else:
            break;
            #print("FILE",file)
            exit()