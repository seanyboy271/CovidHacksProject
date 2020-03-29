import os
import sys

names = ["dengue", "ebola", "h3n2_ha", "h3n2_na", "h5n1_ha", "hku1", "measles", "mers", "mumps", "nl63", "oc43", "SARSCoV", "zika"]

for strain in names:
    try:
        path = os.getcwd() + '/results_' + strain
        #print(os.getcwd())
        os.mkdir(path)
    except:
        e = sys.exc_info()[0]
        #print("<p>Error: %s</p>" % e)

    os.system("augur filter --sequences "+strain+"_new.fasta \
  --metadata "+strain+"_meta.tsv \
  --exclude config/"+strain+"_dropped_strains.txt \
  --output results_"+strain+"/filtered.fasta \
  --group-by country year month \
  --sequences-per-group 20 \
  --min-date 2012")

    os.system("augur align \
    --nthreads 6 \
  --sequences results_"+strain+"/filtered.fasta \
  --reference-sequence config/"+strain+"_reference.gb \
  --output results_"+strain+"/aligned.fasta \
  --fill-gaps")

    os.system("augur tree \
    --nthreads 6 \
  --alignment results_"+strain+"/aligned.fasta \
  --output results_"+strain+"/tree_raw.nwk")


    os.system("augur refine \
  --tree results_"+strain+"/tree_raw.nwk \
  --alignment results_"+strain+"/aligned.fasta \
  --metadata "+strain+"_meta.tsv \
  --output-tree results_"+strain+"/tree.nwk \
  --output-node-data results_"+strain+"/branch_lengths.json \
  --timetree \
  --coalescent opt \
  --date-confidence \
  --date-inference marginal \
  --clock-filter-iqd 4")


    os.system("augur ancestral \
  --tree results_"+strain+"/tree.nwk \
  --alignment results_"+strain+"/aligned.fasta \
  --output results_"+strain+"/nt_muts.json \
  --inference joint")


    os.system("augur translate \
  --tree results_"+strain+"/tree.nwk \
  --ancestral-sequences results_"+strain+"/nt_muts.json \
  --reference-sequence config/"+strain+"_reference.gb \
  --output results_"+strain+"/aa_muts.json")
