import random

def LOCI_start(aux_loci_struc):
    number_of_loci=len(aux_loci_struc)
    aux_LOCI=[]
    for locus_ID in range(number_of_loci):
        locus_alleles = aux_loci_struc[locus_ID]
        aux_alleles=[]
        for allelle in range(len(locus_alleles)):
            random_value=random.uniform(0,1) # aqui da pra melhorar isso e colocar direto um random sample entre 0 e 1
            random_value_binary=int(round(random_value,0))
            aux_alleles.append(random_value_binary)
        aux_LOCI.append(aux_alleles)
    return aux_LOCI