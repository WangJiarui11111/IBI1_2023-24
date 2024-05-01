import re
import os
# Define a function
def count_repeats(sequence, repeat):
    # Calculate the number of all the sub sequences
    return len(re.findall(repeat, sequence))
def process_genes(fasta_file, repeat_sequence, output_dir):
    # Set the output path
    output_file_name = f"{repeat_sequence}_duplicate_genes.fa"
    output_file_path = os.path.join(output_dir, output_file_name)   
    with open(fasta_file, 'r') as infile, open(output_file_path, 'w') as outfile:
        gene_name = None
        gene_sequence = ''
        for line in infile:
            if line.startswith('>'):
                if gene_name:
                    repeat_count = count_repeats(gene_sequence, repeat_sequence)
                    if repeat_count > 0:
                        # Add the number of instances
                        outfile.write(f"> {gene_name} ({repeat_sequence} instances: {repeat_count})\n")
                        outfile.write(f"{gene_sequence}\n")
                gene_name = line[1:].strip().split()[0]  # Only gene name is needed
                gene_sequence = ''
            else:
                gene_sequence += line.strip() 
        # The last gene:
        if gene_name and gene_sequence:
            repeat_count = count_repeats(gene_sequence, repeat_sequence)
            if repeat_count > 0:
                outfile.write(f"> {gene_name} ({repeat_sequence} instances: {repeat_count})\n")
                outfile.write(f"{gene_sequence}\n")
# Get the repeated sequence
repeat_sequence = input("Enter one of the two repetitive sequences ('GTGTGT' or 'GTCTGT'): ").strip()
# Save it in the directory 'Practical 8'
output_dir = 'practical8'
fasta_file_path = 'duplicate_genes.fa'
# Output a new file
process_genes(fasta_file_path, repeat_sequence, output_dir)