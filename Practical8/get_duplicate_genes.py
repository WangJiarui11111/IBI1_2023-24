# Define a function:
def extract_genes_with_duplication(fasta_file, output_file):
    with open(fasta_file, 'r') as infile, open(output_file, 'w') as outfile:
        current_gene_name = None
        for line in infile:
            if line.startswith('>'):
                # Define the position of gene name
                gene_name = line[1:].strip().split()[0]
                if 'duplication' in line:
                    outfile.write(f">{gene_name}\n")
                    current_gene_name = gene_name
                else:
                    current_gene_name = None
            elif current_gene_name:
                outfile.write(line)
extract_genes_with_duplication("C:\\Users\\wangj\\Desktop\\data\\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", 'duplicate_genes.fa')