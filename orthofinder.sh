#!/bin/bash

#SBATCH --job-name=orthoFinder
#SBATCH --partition=Orion
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --mem=64GB
#SBATCH --time=72:00:00


module load anaconda3
source activate OrthoFinder 

orthofinder -f sorghumPepFiles -t 16
