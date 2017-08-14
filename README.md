# Coding4Medicine-2017
Programs written for teaching Coding4Medicine 2017

**File descriptions:**
- states.py: Converts state abbreviations into full names
    - states.txt: Data used in dictionary
- aldh.py: Converts a string of nucleotides into amino acids
    - genetic-code.txt: Data used in dictionary
    - ALDH.txt: [Input gene](https://www.ncbi.nlm.nih.gov/nucleotide/325910902)
    - random-gene.txt: Input gene
    - protein.txt: Output protein
- random-gene.py: Generates a random string of nucleotides to demonstrate DNA is not random (too many stop codons)
    - random-gene.txt: Output file
- biopython.py: A test program used for messing with the Biopython library
- cointoss.py: Determines when a person tossing a coin has changed to a coin with different weights
- **Compare-Human-Chimp/**: Used for an experiment comparing human genes with chimp genes
    - MC1R.fa: Input gene for [human](https://www.ncbi.nlm.nih.gov/nucleotide/237681094) and [chimp](https://www.ncbi.nlm.nih.gov/nucleotide/15011300) (the chimp one doesn't match exactly, since I extracted it from a different genome)
    - MC1R.aln: Human and chimp MC1R genes aligned
    - pull.py: Pulls a certain gene from a genome (used BLAST to find the human one in chimp, then extracted it with this to align them)
- **Ancestry/**: Used for an experiment for sorting people by race by their genomes
    - categorize.py: Groups people by their race by using their genomes
    - person[1-5]: 5 slightly modified versions of south-america
    - random-edit.py: Makes user-specified random edits to an input genome
    - south-america/asia/africa/europe: Fake auto-generated genomes
- **Jigsaw/**: Used for assembling a genome from pieces
    - k-mers.py: Counts the k-mers of a genome
    - length.py: Prints the length of a genome
    - random-gene.fa: Random gene of about equal length to E. coli K12 genome
    - ALDH.fa: Same as /ALDH.txt but FASTA format, for testing with k-mers.py
