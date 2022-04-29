# Instructions
# Translate RNA sequences into proteins.

# RNA can be broken into three nucleotide sequences called codons, and then translated to a polypeptide like so:

# RNA: "AUGUUUUCU" => translates to

# Codons: "AUG", "UUU", "UCU" => which become a polypeptide with the following sequence =>

# Protein: "Methionine", "Phenylalanine", "Serine"

# There are 64 codons which in turn correspond to 20 amino acids; however, all of the codon sequences and resulting amino acids are not important in this exercise. If it works for one codon, the program should work for all of them. However, feel free to expand the list in the test suite to include them all.

# There are also three terminating codons (also known as 'STOP' codons); if any of these codons are encountered (by the ribosome), all translation ends and the protein is terminated.

# All subsequent codons after are ignored, like this:

# RNA: "AUGUUUUCUUAAAUG" =>

# Codons: "AUG", "UUU", "UCU", "UAA", "AUG" =>

# Protein: "Methionine", "Phenylalanine", "Serine"

# Note the stop codon "UAA" terminates the translation and the final methionine is not translated into the protein sequence.

# Below are the codons and resulting Amino Acids needed for the exercise.

# Codon	Protein
# AUG	Methionine
# UUU, UUC	Phenylalanine
# UUA, UUG	Leucine
# UCU, UCC, UCA, UCG	Serine
# UAU, UAC	Tyrosine
# UGU, UGC	Cysteine
# UGG	Tryptophan
# UAA, UAG, UGA	STOP

def proteins(strand):
    list_of_cordons = []
    final_list = []
    codon_protein = {"AUG":"Methionine",
"UUU":"Phenylalanine",
"UUA":"Leucine",
"UCU":"Serine",
"UAU":"Tyrosine",
"UGU":"Cysteine",
"UGG":"Tryptophan",
}
    for i in range(3, len(strand)+1,3):
        list_of_cordons.append(strand[i-3:i])
    for i in list_of_cordons:
        if i == "UUC":
            
            list_of_cordons.insert(list_of_cordons.index(i),"UUU")
            list_of_cordons.remove(i)
        
        if i == "UUG":
            
            list_of_cordons.insert(list_of_cordons.index(i),"UUA")
            list_of_cordons.remove(i)
       
        if i == "UCC" or i == "UCA" or i == "UCG":
            list_of_cordons.insert(list_of_cordons.index(i),"UCU")
            list_of_cordons.remove(i)

        if i == "UAC":
            
            list_of_cordons.insert(list_of_cordons.index(i),"UAU")
            list_of_cordons.remove(i)

        if i == "UGC":
            
            list_of_cordons.insert(list_of_cordons.index(i),"UGU")
            list_of_cordons.remove(i)
        
        for i in list_of_cordons:
            if i == "UAG" or i == "UAA" or i == "UGA":
                return final_list
                
            else:
                final_list.append(codon_protein[i])
        return final_list
