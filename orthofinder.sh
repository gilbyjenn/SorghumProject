#!/bin/bash

#SBATCH --job-name=orthoFinder
#SBATCH --partition=Orion
#SBATCH --mail-user=jgilby@uncc.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --mem=64GB
#SBATCH --time=72:00:00

module load anaconda3 

ortho=/projects/cooper_research/Programs/OrthoFinder_source

$ortho/orthofinder.py -f primaryTranscripts -t 16
