### parse through gff files to extract VIT gene information and write into TSV file for downstream use 
### Jennifer Gilby, Dr. Liz Cooper Lab UNC Charlotte

import os

def gffParser(directory, gff_file, gene_name):

	# read in gff file 
	with open((directory+'/' + gff_file), 'r') as fh:
		for line in fh:
			if line.startswith('#'):
				continue # Skip comment lines
			fields = line.strip().split('\t') # split tsv into field elements 
			if len(fields) < 9:
				continue # check file format is as expected
			feature_type = fields[2] # 'gene'
			attributes = fields[8] # gene_name

			if feature_type == 'gene':
				for name in gene_name:
					if name in attributes:
						chromosome = fields[0] # chromosome
						start = fields[3]
						print(start)
						stop = fields[4]
						print(stop)
						print(name)
						yield chromosome, name, start, stop



def main():
	
	output_file = "sorghum-VIT-gene-positions.tsv"

	# create list of gene names
	with open("orthologs.txt", 'r') as fh:
		gene_name = []
		for line in fh:
			line = line.strip().split(' ')
			for i in range(len(line)):
				gene_name.append(line[i])
		# print(gene_name)

	# iterate through gff files 
	directory = '/projects/cooper_research2/jenny/sorghum_gff'
	with open(output_file, 'w') as fout:
		for file in os.listdir(directory):
			gff_file = file
			
			for chromosome, name, start, stop in gffParser(directory, gff_file, gene_name): # ValueError: too many values to unpack (expected 3)
				fout.write(chromosome + '\t')
				fout.write(start + '\t')
				fout.write(stop + '\t')
				fout.write(name + '\t')
				# new line?
				print('File updated.')
		print('TSV file written. Program quitting...')
			


if __name__ == '__main__':
	main()
