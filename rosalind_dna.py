inFile = open("C:/data/rosalind_dna (4).txt","r")

seq = inFile.read()
seq = seq.strip()
cCnt = seq.count("C")
aCnt = seq.count("A")
tCnt = seq.count("T")
gCnt = seq.count("G")

"%d %d %d %d"%(aCnt, cCnt, gCnt, tCnt)


