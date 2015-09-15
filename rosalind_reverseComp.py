def fReverseComplement(seq):
    
    newSeq = ""
    for i in range(len(seq)-1,-1,-1):
        
        nt = seq[i]
        
         
        if nt == 'A':
            newSeq += 'T'
        elif nt == 'T':
            newSeq += 'A'
        elif nt == 'C':
            newSeq += 'G'
        elif nt == 'G':
            newSeq += 'C'
        else :
            newSeq += nt

    return newSeq

#######end of def########

inFile = open("C:/data/rosalind_revc.txt","r")

seq = inFile.read().strip()

rcSeq = fReverseComplement(seq)

print (rcSeq)


