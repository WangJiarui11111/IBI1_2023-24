#Define a sequence
seq='ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
#Define the two repeated sequence that will be found
repeated_seq=['GTGTGT','GTCTGT']
#Define a function
def find_repeated_sequence(seq,repeated_seq):
    #Input: a sequence
    #Code: find repeated sequence
    #Output: number of repeats
    count=0
    for pattern in repeated_seq:
        count+=seq.count(pattern)
    return count
count=find_repeated_sequence(seq,repeated_seq)
print('Total number of repeats:', count)
#Print the total number of repeats