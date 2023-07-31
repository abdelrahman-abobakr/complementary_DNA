#    GC content     

sequence ="CTCTGGGAGCGAGGGA"
C_cont= sequence.count("C")
G_cont= sequence.count("G")

GC_sum= C_cont + G_cont

length=len(sequence)

GC_content= (GC_sum*100)/length

print(GC_content)


#       the complement of sequence

print(sequence)

Comp_seq=[]

for x in range(length):
    if sequence[x]=="A":
        Comp_seq.append("T")
    
    if sequence[x]=="T":
        Comp_seq.append("A")
    
    if sequence[x]=="C":
        Comp_seq.append("G")
    
    if sequence[x]=="G":
        Comp_seq.append("C")
    

list_to=''.join([str(elem)for elem in Comp_seq])
print(list_to)  