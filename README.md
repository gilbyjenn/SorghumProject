# SorghumProject
Scripts written for the sorghum VIT gene project for Dr. Elizabeth Cooper's Lab at UNC Charlotte. These scripts take reference genome fasta and gff files and use open-source bioinformatics tools to identify and evaluate VIT gene orthologs. 

https://elizcooperlab.com/

### 1. primary-transcript-parser.py
This python script takes sorghum peptide fasta files and filters out alternate transcripts, writing out a fasta file containing only primary transcripts. This primary transcript file will be passed into OrthoFinder to determine gene orthology groups. 

### 2. orthofinder.sh 
This bash script calls OrthoFinder and iterates through a directory containing the previously prepared primary transcript fasta files. Orthofinder will output a text file containing all orthogroups. A new text file called orthogroups.txt was written to include only the orthogroups containing the reference genes of interest: Sobic.004g301500, Sobic.004g301600, and Sobic.004g301650.  

### 3. sorghum-gff-parser.py
This python script uses the previously produced orthologs.txt file and searches through a directory containing sorghum GFF files. It will write out the gene names, start, and stop positions of the orthologous genes into an output tsv file called sorghum-VIT-gene-positions.tsv. 

### 4. sorghum-fasta-parser.py
This python script will take the previously written sorghum-VIT-gene-positions.tsv file and use the gene name, start and stop positions to extract the DNA sequences of these genes from the sorghum reference genome fasta files. It will write out a file called iron_genes.fa. 

### 5. orthogroup-fasta-parser.py 
This python script will take the previously written iron_genes.fa file and split it into three fasta files called iron_genes_orthogroup1-1.fa, iron_genes_orthogroup1-2.fa, and iron_genes_orthogroup2.fa. Each file will contain only the DNA sequences for our VIT orthogroups of interest.

### 6. Alignment with Clustal Omega
The genes of each orthogroup were aligned using the web api for Clustal Omega.
https://www.ebi.ac.uk/jdispatcher/msa/clustalo

## Data visualization
### 1. NJtrees.R
This R script takes the aligned fasta files from step 6 and generates a neighbor joining tree. 

### 2. haplonet.R 
haplonet.R is an R script written by mhoban (https://github.com/mhoban/haplonet). The script on this repository has been slightly edited to force the use of the big-pallet color pallet and include a legend without need for command line arguments. haplonetEdited.R can be run on the command line using the following command: 

$ /usr/local/bin/Rscript ./debughapnet.R -f genotype og1-1_edited.fa og1data.tsv 

haplonet.R requires a data file containing descriptive information. The data files included here use the genotype name as the descriptor. 
