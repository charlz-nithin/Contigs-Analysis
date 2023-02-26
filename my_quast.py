import argparse
from Bio import SeqIO

# Define a function to calculate the N50 value from a list of contig lengths
def calculate_n50(lengths):
    Length_sorted = sorted(lengths, reverse=True) # Sort the list of contig lengths in descending order
    Length_total = sum(lengths) # Calculate the total length of all contigs
    target_length = Length_total / 2 # Calculate the target length for the N50 value (i.e. half of the total length)
    current_length = 0 # Initialize a variable to keep track of the current length
    for length in Length_sorted:
        current_length += length # Add the current contig length to the running total
        if current_length >= target_length: # If the running total has reached the target length for the N50 value
            return length # Return the length of the current contig as the N50 value

# Define a function to parse the input fasta file and extract relevant information
def parse_fasta(fasta_file):
    contig_lengths = [] # Initialize an empty list to store the lengths of all contigs
    largest_contig = 0 # Initialize a variable to store the length of the largest contig
    for record in SeqIO.parse(fasta_file, "fasta"): # Loop over each record in the input fasta file
        length = len(record.seq) # Get the length of the current contig
        contig_lengths.append(length) # Add the length of the current contig to the list of contig lengths
        if length > largest_contig: # If the length of the current contig is greater than the length of the largest contig seen so far
            largest_contig = length # Update the length of the largest contig
    num_of_contigs = len(contig_lengths) # total number of contigs
    total_length = sum(contig_lengths) # total length of all contigs
    n50 = calculate_n50(contig_lengths) # Calculate the N50 value for the list of contig lengths
    return num_of_contigs, total_length, largest_contig, n50

# Define a function to write a report file with the parsed information
def write_report(output_file, num_of_contigs, total_length, largest_contig, n50):
    with open(output_file, "w") as f:
        f.write(f"Number of contigs: {num_of_contigs}\n") # Write the total number of contigs to the report file
        f.write(f"Total length of contigs: {total_length}\n") # Write the total length of all contigs to the report file
        f.write(f"Length of largest contig: {largest_contig}\n") # Write the length of the largest contig to the report file
        f.write(f"N50: {n50}\n") # Write the N50 value to the report file

# Parsing the command-line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a report file for a fasta file")
    parser.add_argument("fasta_file", help="The input fasta file")
    parser.add_argument("quast_test_output", help="The output report file")
    args = parser.parse_args()

    # Call the parse_fasta function to extract relevant information from the input fasta file
    num_of_contigs, total_length, largest_contig, n50 = parse_fasta(args.fasta_file)

    # Write a report file with the parsed information
    write_report(args.output_file, num_of_contigs, total_length, largest_contig, n50)
