# Contigs-Analysis
A python script to get the N50, length of the largest contig, number and total length of the contigs assembled.
Requirement - to create a script to analyze the contigs.fasta file to get number of contigs, length of the contigs and the N50 value and output a text file.
N50 - The N50 value represents the length at which 50% of the total length of all sequences is contained in sequences of that length or longer.
To explain it in logical terms, we need to get lengths sorted in reverse to the get the length of contigs to cover 50% genome and find the length of contigs that cover total length of genome / 2 (50%). Get length upto 50% and then return the length.
To parse a fasta file, biopython is imported and seqIO is used to read the file, in this function the largest contig , length and number of contigs is calculated.
Next, all this information is written to a report text file.
This must be run as a script on command line, so an argument function has to be created.
Using argparse, the arguments are decided and help is also created to use it as a script.


contigs.fa - provided as test data.

Usage:
python my_quast.py contigs.fa report.txt
