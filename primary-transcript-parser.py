### parse through sorghum peptide files to extract primary transcripts and rewrite file
### Jennifer Gilby, Dr. Liz Cooper Lab UNC Charlotte


import os


def peptideParser(fasta_file):
	header = None
	seq = ""

	with open(fasta_file, 'r') as fh:
		for line in fh:
			line = line.strip()
			if line.startswith(">"):
				if line.endswith('.1'): # .01 for "sorghum_" files
					if header:
						yield header, seq
					header = line
					seq = ""
				else:
					pass
			else:
				seq += line
		if header:
			yield header, seq 
				

def main():
	
	directory = '/scratch/jgilby/sorghumPepFiles/pep2'
	for file in os.listdir(directory):
		fasta_file = file
		output_file = fasta_file + "primary_transcripts_only.fa" 
			
		with open(output_file, 'w') as fout:
			for header,seq in peptideParser(fasta_file):
				fout.write(header + '\n')
				fout.write(seq + '\n')
			


if __name__ == '__main__':
	main()