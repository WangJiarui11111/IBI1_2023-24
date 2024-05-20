# Open the file
with open("C:\\Users\\wangj\\Desktop\\data\\SLC6A4_HUMAN.fa", 'rt') as file:
    # Read the file from the second line
    file.readline() 
    # Read the file
    seq1 = file.read()
seq1 = seq1.replace('\n','')

# Open the file
with open("C:\\Users\\wangj\\Desktop\\data\\SLC6A4_MOUSE.fa", 'rt') as file:
    # Read the file from the second line
    file.readline()
    # Read the file
    seq2 = file.read()
seq2 = seq2.replace('\n','')
# Open the file
with open("C:\\Users\\wangj\\Desktop\\data\\SLC6A4_RAT.fa", 'rt') as file:
    # Read the file from the second line
    file.readline()
    # Read the file
    seq3 = file.read()
seq3 = seq3.replace('\n','')

#set initial distance as zero
edit_distance=0 

# Iterate over each element in the list
for	i in range(len(seq1)):
 #compare each amino acid
	if	seq1[i]!=seq2[i]:		
		edit_distance +=1 #add a score 1 if amino acids are	different
# Print the edit distance between human and mouse
print(edit_distance)

# Iterate over each element in the list
for	i in range(len(seq1)):
 #compare each amino acid
	if	seq1[i]!=seq3[i]:		
		edit_distance +=1 #add a score 1 if amino acids are	different
# Print the edit distance between human and rat
print(edit_distance)

# Iterate over each element in the list
for	i in range(len(seq2)):
 #compare each amino acid
	if	seq2[i]!=seq3[i]:		
		edit_distance +=1 #add a score 1 if amino acids are	different
# Print the edit distance between mouse and rat
print(edit_distance)

import blosum as bl
matrix=bl.BLOSUM(62)

# Calculate the score
def blosum_score(seq1, seq2):
    score = 0
    for aa1, aa2 in zip(seq1, seq2):
        score += matrix[aa1][aa2]
    print(f'Blosum_score is:',score)

# Calculate the consistency
def calculate_identity(seq1, seq2):
    print(f'Identity is:',sum(1 for a, b in zip(seq1, seq2) if a == b) / len(seq1) * 100)

print('Human and mouse')
blosum_score(seq1, seq2)
calculate_identity(seq1, seq2)
print('Human and rat')
blosum_score(seq1, seq3)
calculate_identity(seq1, seq3)
print('Mouse and rat')
blosum_score(seq2, seq3)
calculate_identity(seq2, seq3)

