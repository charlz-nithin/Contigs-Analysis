import argparse
from Bio import SeqIO

def calculate_n50(lengths):
    Length_sorted = sorted(lengths, reverse=True)
    Length_total = sum(lengths)
    target_length = total_length / 2
    current_length = 0
    for length in Length_sorted:
        current_length += length
        if current_length >= target_length:
            return length

def parse_fasta(fasta_file):
    contig_lengths = []
    largest_contig = 0
    for record in SeqIO.parse(fasta_file, "fasta"):
        length = len(record.seq)
        contig_lengths.append(length)
        if length > largest_contig:
            largest_contig = length
    num_contigs = len(contig_lengths)
    total_length = sum(contig_lengths)
    n50 = calculate_n50(contig_lengths)
    return num_contigs, total_length, largest_contig, n50

def write_report(output_file, num_contigs, total_length, largest_contig, n50):
    with open(output_file, "w") as f:
        f.write(f"Number of contigs: {num_contigs}\n")
        f.write(f"Total length of contigs: {total_length}\n")
        f.write(f"Length of largest contig: {largest_contig}\n")
        f.write(f"N50: {n50}\n")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a report file for a fasta file")
    parser.add_argument("fasta_file", help="The input fasta file")
    parser.add_argument("quast_test_output", help="The output report file")
    args = parser.parse_args()

    num_contigs, total_length, largest_contig, n50 = parse_fasta(args.fasta_file)
    write_report(args.output_file, num_contigs, total_length, largest_contig, n50)