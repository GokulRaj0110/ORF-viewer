def protein_finder(codon):
    file = open(codon,'r+')
    data=file.read()
    rna_data = data.replace("T", "U")
    global codon_list
    codon_list = [rna_data[i:i+3] for i in range(0,len(rna_data),3)]
    nucleotide = ""
    for l in codon_list:
        nucleotide+=l
    print("Codon = ",nucleotide)

def amino_seq(codon_seq):
    protein_seq = []
    for j in codon_seq:
        if j=="UUU" or j=="UUC":
            protein_seq.append("Phe")
        elif j=="UUA" or j=="UUG" or j=="CUU" or j=="CUC" or j=="CUA" or j=="CUG":
            protein_seq.append("Leu")
        elif j=="AUU" or j=="AUC" or j=="AUA":
            protein_seq.append("Ile")
        elif j=="AUG":
            protein_seq.append("Met")
        elif j=="GUU" or j=="GUC" or j=="GUA" or j=="GUG":
            protein_seq.append("Val")
        elif j=="UCU" or j=="UCC" or j=="UCA" or j=="UCG":
            protein_seq.append("Ser")
        elif j=="CCU" or j=="CCC" or j=="CCA" or j=="CCG":
            protein_seq.append("Pro")
        elif j=="ACU" or j=="ACC" or j=="ACA" or j=="ACG":
            protein_seq.append("Thr")
        elif j=="GCU" or j=="GCC" or j=="GCA" or j=="GCG":
            protein_seq.append("Ala")
        elif j=="UAU" or j=="UAC":
            protein_seq.append("Tyr")
        elif j=="CAU" or j=="CAC":
            protein_seq.append("His")
        elif j=="CAA" or j=="CAG":
            protein_seq.append("Gln")
        elif j=="AAU" or j=="AAC":
            protein_seq.append("Asn")
        elif j=="AAA" or j=="AAG":
            protein_seq.append("Lys")
        elif j=="GAU" or j=="GAC":
            protein_seq.append("Asp")
        elif j=="GAG" or j=="GAG":
            protein_seq.append("Glu")
        elif j=="UGU" or j=="UGC":
            protein_seq.append("Cys")
        elif j=="UGG":
            protein_seq.append("Trp")
        elif j=="CGU" or j=="CGC" or j=="CGA" or j=="CGG" or j=="AGA" or j=="AGG":
            protein_seq.append("Arg")
        elif j=="AGU" or j=="AGC":
            protein_seq.append("Ser")
        elif j=="GGU" or j=="GGC" or j=="GGA" or j=="GGG":
            protein_seq.append("Gly")
        else:
            protein_seq.append("  ")
    amino_acid = ""
    for k in protein_seq:
        amino_acid+=k+" "
    print("Amino Sequence = ",amino_acid)


def ORF_finder(codon):
    ORF = ""
    for m in codon:
        for n in codon:
            if m=="AUG":
                if n=="UAA" or n=="UAG" or n=="UGA":
                    lst= codon[codon.index(m):codon.index(n)]
    for p in lst:
        ORF+=p
    print("ORF = ",ORF,end="\n")            
    
amino_seq(codon_list)
ORF_finder(codon_list)


