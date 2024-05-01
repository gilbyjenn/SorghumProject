# replaces - with N in alignment files for downstream use 

in_file = "/projects/cooper_research2/jenny/outfiles/alignments/alignment_og2.fa"
out_file = "og2_edited.fa" 

with open(out_file, 'w') as fout:
    
    with open(in_file, 'r') as fh:
        
        for line in fh:
            line = line.strip()
            if line.startswith(">"):
                fout.write('\n')
                fout.write(line)
                fout.write('\n')
            else:
                for nt in line:
                    if nt == "-":
                        fout.write("N")
                    else:
                        fout.write(nt)
