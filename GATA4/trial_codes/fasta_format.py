import csv

csv_file_path = 'GATA4_anti-GST/GATA4_anti-GST_8mers_top_enrichment.txt'
fasta_file_path = 'output_sequences2.fasta'
            
with open(csv_file_path, 'r') as input_file, open(fasta_file_path, 'w') as output_file:
        next(input_file)
        for i, line in enumerate(input_file, start=1):
            sequence = line.strip().split('\t')[0]
            output_file.write(f">Sequence_{i}\n{sequence}\n")