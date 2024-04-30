"""
parse through sorghum fasta files to extract VIT gene sequences from previously generated
TSV file and write into new fasta file.
Jennifer Gilby, Dr. Liz Cooper Lab UNC Charlotte

"""


import os

def fastaParser(directory, fasta_file_list, geneName, start, stop):
	
	# iterate through list of fasta file names
	# if name == gene name then open fasta file and parse 
	for fasta in fasta_file_list:
		if geneName.split('.')[0].upper() in str(fasta).upper():

			# read in fasta file 
			with open((directory+'/' + fasta), 'r') as fh:
				print('file ' + str(fasta) + ' open...')
		
				# test code
				# print('gene name: ' + geneName)
				# print('start and stop positions: ' + str(start) + ' ' + str(stop))

				# parse 
				header = None
				seq = ""
				for line in fh:
					line = line.strip()
					#line = line.readline()
					
					if line.startswith('>'):
						
						if header: 
							geneSeq = seq[start-1:stop-1]
							# test code
							# print(header)
							# print(geneName)
							# print(geneSeq)
							header = None
							yield geneName, geneSeq
							break
						
						# VIT gene on chromosome 4, labeled different in different sorghum fastas
						if line == ">4" or line == ">Chr04" or line == ">Chr04_RagTag" or line == ">chromosome_4": 
							header = line 
							seq = ""

						else:
							pass 
					else:
						if header:
							seq += line 

						else:
							continue
		else: 
			continue


def main():
	
	output_file = "iron_genes.fa"
	directory = '/scratch/jgilby/cooperLab/sorghumFastas'

	# read in ortholog information file from gff parser output
	with open("sorghum-VIT-gene-positions.tsv", 'r') as fh:
	    for lst in fh:
	        lst = lst.strip().split('\t')
	        # Test code: 
		# print('test lst')
	        # print(lst)

	fasta_file_list = []
	for file in os.listdir(directory):
		fasta_file_list.append(file)

	with open(output_file, 'w') as fout:

		for i in range(0, len(lst), 3):
			start = int(lst[i])
			stop = int(lst[i+1])
			geneName = (lst[i+2])
			# Test Code:
			# print('test geneName')
			# print(geneName)

			for geneName, geneSeq in fastaParser(directory, fasta_file_list, geneName, start, stop): # input list element 
				# test code
				# print(geneName)
				# print(geneSeq)
				fout.write('>' +  geneName + '\n')
				fout.write(geneSeq + '\n')
				print('DNA seq for ' + geneName + ' found. File updated.')
		print('File written. Program quitting...')
			


if __name__ == '__main__':
	main()
