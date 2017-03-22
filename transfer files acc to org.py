import os
import shutil
for path, dirs, files in os.walk('F:\M.Tech\series_imp_info'):
    for file in files:
        read_f = open(os.path.join(path,file),'r');
        for line in read_f:
            line = line.rstrip()
            if line.startswith('!Sample_organism_ch1'):
                splitit = line.split('\t');
                if splitit[1] == '"Mus musculus"':
                    shutil.copy(file, "F:\M.Tech\org segregated\mus musculus")
                if splitit[1] == "Homo sapiens":
                    shutil.copy(file, "F:\M.Tech\org segregated\Homo sapiens")
                if splitit[1] == "Rattus norvegicus":
                    shutil.copy(file, "F:\M.Tech\org segregated\Rattus norvegicus")
                if splitit[1] == "Saccharomyces cerevisiae":
                    shutil.copy(file, "F:\M.Tech\org segregated\Saccharomyces cerevisiae")
                if splitit[1] == "Arabidopsis thaliana":
                    shutil.copy(file, "F:\M.Tech\org segregated\Arabidopsis thaliana")
                if splitit[1] == "Drosophila melanogaster":
                    shutil.copy(file, "F:\M.Tech\org segregated\Drosophila melanogaster")
                if splitit[1] == "Danio rerio":
                    shutil.copy(file, "F:\M.Tech\org segregated\Danio rerio")
                if splitit[1] == "Caenorhabditis elegans":
                    shutil.copy(file, "F:\M.Tech\org segregated\Caenorhabditis elegans")
                if splitit[1] == "Escherichia coli":
                    shutil.copy(file, "F:\M.Tech\org segregated\Escherichia coli")
                if splitit[1] == "Oryza sativa":
                    shutil.copy(file, "F:\M.Tech\org segregated\Oryza sativa")
                if splitit[1] == "Sus scrofa":
                    shutil.copy(file, "F:\M.Tech\org segregated\Sus scrofa")
                if splitit[1] == "Gallus gallus":
                    shutil.copy(file, "F:\M.Tech\org segregated\Gallus gallus")
        read_f.close()
#output.close()
