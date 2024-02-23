### Write VIT genes into separate fasta files for orthogroup 1 and 2 (from orthofinder output)
### Jennifer Gilby, Dr. Liz Cooper Lab UNC Charlotte



# write tsv file for each gene name (id) and region 

og1 = ['353.004G328800', 'AusTRCF317961.004G261900', 'IS19953.004G326900', 'IS19953.004G327000', 'IS3614-3.004G305200', 'IS8525.004G336100', 'IS8525.004G336200', 'IS929.004G288600', 'Ji2731.004G334300', 'Ji2731.004G334400', 'PI525695.004G298000', 'PI525695.004G298100', 'PI532566.K002713', 'PI536008.004G098800', 'PI536008.004G098900', 'R931945-2-2.004G304000', 'R931945-2-2.004G304100', 'S369-1.004G252100', 'S369-1.004G252200', 'SbRio.04G321700', 'SbRio.04G321800', 'SbiCamber.04g046800', 'SbiCamber.04g046810', 'SbiGrassl.04g048530', 'SbiGrassl.04g048540', 'SbiLeoti.04g048500', 'SbiLeoti.04g048510', 'SbiPI229841.04g048450', 'SbiPI229841.04g048460', 'SbiPI297155.04g048480', 'SbiPI297155.04g048490', 'SbiPI329311.04g051380', 'SbiPI329311.04g051390', 'SbiPI506069.04g049010', 'SbiPI510757.04g049310', 'SbiPI510757.04g049320', 'SbiPI655972.04g048500', 'SbiPI655972.04g048510', 'Sobic.004G301500', 'Sobic.004G301600']
og2 = ['IS3614-3.004G305400', 'PI525695.004G298200', 'SbRio.04G321900', 'SbiGrassl.04g048550', 'SbiPI329311.04g051400', 'SbiPI510757.04g049330', 'SbiPI655972.04g048520', 'Sobic.004G301650']


def getOG1(og1):

	header = None
	seq = ""

	with open("iron_genes.fa", 'r') as fh:
	    for line in fh:
	        line = line.strip().split('\n')
	        line = line[0]

	        if line.startswith('>'):
	        	if header:
	        		#seq += line
	        		print(header)
	        		print(seq)
	        		yield header, seq
	        		header = None

	        	if line[1:] in og1: 
	        		header = line 
	        		seq = ""

	        	else:
	        		pass 

	        else:
	        	if header:
	        		seq += line

	        	else:
	        		continue

def getOG2(og2):

	header = None
	seq = ""

	with open("iron_genes.fa", 'r') as fh:
	    for line in fh:
	        line = line.strip().split('\n')
	        line = line[0]

	        if line.startswith('>'):
	        	if header:
	        		#seq += line
	        		print(header)
	        		print(seq)
	        		yield header, seq
	        		header = None

	        	if line[1:] in og2: 
	        		header = line 
	        		seq = ""

	        	else:
	        		pass 

	        else:
	        	if header:
	        		seq += line

	        	else:
	        		continue



def main():
	
	output_file1 = "iron_genes_orthogroup1.fa"
	output_file2 = "iron_genes_orthogroup2.fa"
	directory = '/Users/jennifergilby/cooperLab'



	with open(output_file1, 'w') as fout:

		for header,seq in getOG1(og1):
			print('Adding sequence for ' + str(header) + ' to file...')

			fout.write(header + '\n')
			fout.write(seq + '\n')
			print('\n\n file updated...')

	with open(output_file2, 'w') as fout:

		for header,seq in getOG2(og2):
			print('Adding sequence for ' + str(header) + ' to file...')
			fout.write(header + '\n')
			fout.write(seq + '\n')
			print('\n\n file updated...')

	print('Files written. Program quitting...')




if __name__ == '__main__':
	main()