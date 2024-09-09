# -*- coding: utf-8 -*-
"""Metagenome analysis.ipynb

# Computational profiling of mouse gut metagenome to understand genome evolution

## Data accession
"""

# Metagenome used in this notebook can be accessed from https://www.ncbi.nlm.nih.gov/sra/SRX25816343

"""## Installing Libraries"""

!pip install biopython

!apt-get install clustalo

"""## Multiple Sequence Alignment (MSA)"""

from Bio import SeqIO, AlignIO
from Bio.Align.Applications import ClustalOmegaCommandline
import random
import gzip

# Define paths for input and output files   # Delete the previously made files from colab storage if any before execution
input_gz_fasta = "/content/input.fasta.gz"
decompressed_fasta = "/content/decompressed.fasta"
reduced_fasta = "/content/reduced_sequences.fasta"
output_fasta = "/content/aligned_reads.fasta"

# Decompress the gzipped FASTA file
with gzip.open(input_gz_fasta, 'rt') as gz_file:
    with open(decompressed_fasta, 'w') as fasta_file:
        fasta_file.write(gz_file.read())

# Read sequences from the decompressed FASTA file
sequences = list(SeqIO.parse(decompressed_fasta, "fasta"))

# Reduce the number of sequences for a custom alignment (e.g., take a random subset of 50 sequences)
reduced_sequences = random.sample(sequences, min(50, len(sequences)))

# Save the reduced set of sequences to a new FASTA file
SeqIO.write(reduced_sequences, reduced_fasta, "fasta")

# Align sequences using Clustal Omega
clustalomega_cline = ClustalOmegaCommandline(infile=reduced_fasta, outfile=output_fasta, verbose=True, auto=True)

try:
    # Execute Clustal Omega
    stdout, stderr = clustalomega_cline()

    # Read the aligned sequences
    aligned_reads = AlignIO.read(output_fasta, "fasta")
    print(aligned_reads)
except Exception as e:
    print(f"Error running Clustal Omega: {e}")

"""## Phylogenetic Tree"""

from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import Phylo
import random

output_fasta = "/content/aligned_reads.fasta"
output_tree = "/content/phylogenetic_tree.xml"

# Calculate the distance matrix using the Jukes-Cantor model
calculator = DistanceCalculator('identity')
distance_matrix = calculator.get_distance(aligned_reads)

# Construct the phylogenetic tree using the Neighbor-Joining method
constructor = DistanceTreeConstructor(calculator, method='nj')
phylo_tree = constructor.build_tree(aligned_reads)

# Write the phylogenetic tree to a file
Phylo.write(phylo_tree, output_tree, "phyloxml")

# Visualize the phylogenetic tree
Phylo.draw(phylo_tree)

print("{e}")

"""## GC-content Analysis and Visualization"""

import matplotlib.pyplot as plt
from Bio import SeqIO

# Function to calculate GC content
def calculate_gc_content(sequence):
    gc_count = sum(1 for base in sequence if base in 'GC')
    return (gc_count / len(sequence)) * 100

# Function to analyze GC content in a FASTA file
def analyze_gc_content(fasta_file):
    gc_contents = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequence = str(record.seq)
        gc_content = calculate_gc_content(sequence)
        gc_contents.append(gc_content)
    return gc_contents

# Function to plot histogram of GC contents
def plot_gc_content_histogram(gc_contents):
    plt.figure(figsize=(10, 6))
    plt.hist(gc_contents, bins=10, color='skyblue', edgecolor='black')
    plt.title("GC Content Distribution")
    plt.xlabel("GC Content (%)")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

fasta_file = "aligned_readsx.fasta"
gc_contents = analyze_gc_content(fasta_file)

# Plot histogram
plot_gc_content_histogram(gc_contents)

# Optional: Print GC content for each sequence
for i, gc_content in enumerate(gc_contents, 1):
    print(f"Sequence {i}: GC Content: {gc_content:.2f}%")
