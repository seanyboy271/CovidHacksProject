import json
import csv
import os
import sys
import pprint


if __name__ == "__main__":

    names = ["dengue", "ebola", "h3n2_ha", "h3n2_na", "h5n1_ha", "hku1", "measles", "mers", "mumps", "nl63", "oc43", "SARSCoV", "zika"]

    for virus in names:
        aa_muts_json = json.load(open(os.getcwd() + '\\results_' + virus + '\\aa_muts.json'))
        nt_muts_json = json.load(open('./results_' + virus + '/nt_muts.json'))
        Metadata_file = open('./' + virus + '_meta.tsv')

        aa_muts_dict = dict(aa_muts_json)
        nt_muts_dict = dict(nt_muts_json)

        # print(aa_muts_dict, nt_muts_dict)

        aa_muts_nodes = aa_muts_dict['nodes']
        nt_muts_nodes = nt_muts_dict['nodes']

        reader = csv.DictReader(Metadata_file, dialect='excel-tab')
        count = 0
        finalDict = {}

        for row in reader:
            case = row['strain'].strip()
            Disease = row['virus'].strip()
            Date = row['date'].strip()
            Region = row['region'].strip()
            Country = row['country'].strip()
            aa_muts_list = []
            nt_muts_list= []

            if case in aa_muts_nodes:
                aa_muts_case_data = aa_muts_nodes[case]
                #print(aa_muts_case_data)
                for mutType in aa_muts_case_data['aa_muts']:
                    if aa_muts_case_data['aa_muts'][mutType]!= []:
                        #print(mutType, aa_muts_case_data['aa_muts'][mutType], case)
                        aa_muts_list.append({mutType: aa_muts_case_data["aa_muts"][mutType]})


            if case in nt_muts_nodes and len(nt_muts_nodes[case]['muts']) > 0:
                print(nt_muts_nodes[case]['muts'])
                nt_muts_list.extend(nt_muts_nodes[case]['muts'])


            tempDict = {'virus': Disease, 'date':Date, "region": Region, "country": Country, "aa_muts": aa_muts_list, "nt_muts": nt_muts_list}
            finalDict[case] = tempDict

        with open(Disease + '.json', 'w') as out:
            out.truncate(0)
            #pprint.pprint(finalDict, stream=out)
            json.dump(finalDict, out)