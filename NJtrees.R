### R script to create neighbor joining trees for VIT gene orthogroups
### Jennifer Gilby, Dr. Liz Cooper Lab UNC Charlotte



# install packages 
install.packages('adegenet', dep=TRUE)
install.packages('phangorn', dep=TRUE)

# load packages 
library(stats)
library(ade4)
library(ape)
library(adegenet)
library(phangorn)

# load in fasta formatted sequences
dna <- fasta2DNAbin(file='/Users/jennifergilby/cooperLab/iron_gene_alignments.fa')
dna

# distance-based 
D <- dist.dna(dna, model = "TN93")
length(D)


# construct tree 
tre <- nj(D)
class(tre) #all trees created using {ape} package will be of class phylo

tre <- ladderize(tre)
tre

plot(tre, cex = 0.6)
title("NJ Tree of Aligned Iron Genes")


# TREE FOR ORTHOGROUP 1
# load in fasta formatted sequences
dna_og1 <- fasta2DNAbin(file='/Users/jennifergilby/cooperLab/alignment_og1.fa')

# distance-based 
D_og1 <- dist.dna(dna_og1, model = "TN93")

# construct tree 
tre_og1 <- njs(D_og1)
tre_og1 <- ladderize(tre_og1)

plot(tre_og1, cex = 0.6)
title("NJ Tree of Aligned Iron Genes in Orthogroup 1")



# TREE FOR ORTHOGROUP 2
# load in fasta formatted sequences
dna_og2 <- fasta2DNAbin(file='/Users/jennifergilby/cooperLab/alignment_og2.fa')

# distance-based 
D_og2 <- dist.dna(dna_og2, model = "TN93")

# construct tree 
tre_og2 <- njs(D_og2)
tre_og2 <- ladderize(tre_og2)

plot(tre_og2, cex = 0.6)
title("NJ Tree of Aligned Iron Genes in Orthogroup 2")
