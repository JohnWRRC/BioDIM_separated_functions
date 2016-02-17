
import random
def gene_exchanceANTIGO(indiv_LOCI_indA,indiv_LOCI_indB,LOCI_gene_exchange_rate):
    aux_IndA = []
    aux_IndB = []
    number_of_loci=len(indiv_LOCI_indA)
    for locus_ID in range(number_of_loci):
        locus_alleles = indiv_LOCI_indA[locus_ID]
        aux_alleles_A=[]
        aux_alleles_B=[]
        for allelle in range(len(locus_alleles)):
            random_value=random.uniform(0,1)
            if (random_value<LOCI_gene_exchange_rate):
                aux_alleles_A.append(indiv_LOCI_indA[locus_ID][allelle])
            else:
                aux_alleles_A.append(indiv_LOCI_indB[locus_ID][allelle])
            random_value=random.uniform(0,1)
            if (random_value<LOCI_gene_exchange_rate):
                aux_alleles_B.append(indiv_LOCI_indB[locus_ID][allelle])
            else:
                aux_alleles_B.append(indiv_LOCI_indA[locus_ID][allelle])
        aux_IndA.append(aux_alleles_A)
        aux_IndB.append(aux_alleles_B)
    return aux_IndA,aux_IndB