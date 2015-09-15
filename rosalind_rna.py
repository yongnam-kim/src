inFile = open("C:/data/rosalind_rna.txt","r")

dnsSeq = inFile.read()

rnsSeq = dnsSeq.replace("T",'U')

print (rnsSeq)
