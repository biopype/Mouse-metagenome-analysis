Title: “Computational Profiling of Mouse Gut Metagenome to Understand Genome Evolution”

1. **Introduction:**

In this project we aim to develop a python algorithm that utilizes metagenome data to sequentially align multiple sequences, create a phylogenetic tree and analyze the GC-content to understand genome evolution between different species of mouse gut metagenome. Further, we want to analyze our findings and make conclusions on the results obtained. This project is also designed to reduce time and provide a smooth flow for the metagenome analysis, instead of a time taking process. 

1) GC-content analysis:

GC-content analysis can give insights into the genetic diversity of microbial genomes. Because GC-content varies significantly among different genomes and genes of the same genome, it can act as a biomarker to explain genome evolution. Gene biased gene conversion (gBGC) theory explains the most supported evolutionary mechanism pertaining to GC-content. According to gBGC, GC alleles are preferred over AT alleles during double strand break-repair by homologous recombination. (Singh, 2016)

1) Multiple sequence alignment:

DNA sequencing of metagenomes yield insights into similarities and differences between multiple organisms. Multiple Sequence Alignment (MSA) is an approach that aims to align sequences based on conserved regions, genes that are similar in different organisms, and indicate no evolutionary change. We can also compare orthologous (same gene in different species) and paralogous (gene duplication within the same species) sequences to observe how functions of genes or proteins have diverged over time due to evolution (Gabaldón T, 2013). A very insightful representation of an MSA is a phylogenetic tree.

1) Phylogenetic tree:

A phylogenetic tree explains genome evolution by representing genetic similarities between different species. It indicates genome divergence between species that has occurred due to various reasons, such as, mutations, gene duplications and other mechanisms. Genome sequencing helps in constructing a phylogenetic tree by describing how species should be arranged in a phylogenetic tree. Genes with more similar makeup are placed closer to each other and vice versa. A phylogenetic tree can also help in identifying a common ancestor of different species (Kapli, 2020).

1. **Data Description:**

We downloaded a metagenome dataset, titled “Rat Chymus Sequencing”, from NCBI – SRA. This dataset was a result of chymus in rat sequencing using different redox potentials. AMPLICON strategy was used on Illumina, and our dataset contained 39.7M bases.

1. **Methodology:**

A programming environment for our project was created by installing ‘biopython’, which contains various libraries for biological data handling. Next, we installed Clustal Omega for our multiple sequence alignment. The data file (FASTA) was uploaded in the colab environment, and the number of sequences were reduced to 50 for a quicker alignment. The results were obtained and saved in a FASTA file. 

For phylogenetic tree construction, we imported ‘DistanceCalculator’ that measures the distance matrix between aligned sequences, and ‘DistanceTreeConstructor’ that creates a phylogenetic tree using the distance matrix. 

Neighbor Joining (NJ) algorithm is a sequential method to create a phylogenetic tree by collecting sequences as individual nodes and arranging them in a way to minimize the branch lengths. (Koichiro Tamura, 2004) Branch lengths refer to the genetic distance between organisms. We used NJ algorithm to construct a phylogenetic tree due to its accuracy for small number of nucleotides.

Lastly, we calculate the GC-content of our sequences using ‘calculate\_gc\_content()’ function in ‘biopython’. The individual GC-content for each sequence is stored in the dictionary, ‘gc-content’ and displayed.

1. **Visualization:**
- ![](Aspose.Words.16a0594f-d5e5-4be2-9874-376840a5f3cd.001.png)**Multiple Sequence Alignment of 50 random sequences (a snippet):**
- **Phylogenetic Tree:** 

![](Aspose.Words.16a0594f-d5e5-4be2-9874-376840a5f3cd.002.png)

- **GC-Content:**

![](Aspose.Words.16a0594f-d5e5-4be2-9874-376840a5f3cd.003.png)

1. **Results and Discussions:**

Multiple sequence alignment (MSA) results highlight conserved regions that are unchanged and exist in the same form in different genomes. In contrast, variable regions show evolutionary divergence through mismatches and gaps. These regions give information about selective pressures and mutations on microbial populations. The presence of diverse varied sequence in genomes is a hallmark of microbial communities that undergo swift genome alterations owing to evolutionary pressures. This is called genome flexibility in microbes (Cordero, 2014).

Phylogenetic tree represents clustering of closely related species and informs about multiple lineages in mouse gut metagenome. The tree indicates a complex and rich mouse gut microbe diversity.

The results of the GC-content analysis, as depicted by the histogram, illustrate that the sequences fall between 38% to 53.87% GC content. Most of the sequences are between 45% to 51% range. The histogram shape is right skewed with a peak around 48-50%, so most of the sequences are in this GC content range. Some sequences with higher GC content are above 50% range. 

Over 16 sequences fall in the major peak that is between 48% and 50%. This shows that most of the sequences have a balanced guanine and cytosine base composition.  The majority of the sequences have a moderate GC-content which means that the sequences are stable, as GC bonds are stronger than AT. 

More GC content stability might indicate that the organisms living in the mouse gut genome are exposed to various conditions, such as, temperature fluctuations and metabolic byproducts which have evolved them to be more thermally stable. 

Microbes between the 48% to 50% range have better evolved in terms of GC-content than others, because high GC-content indicate more genome stability. 

Horizontal Gene Transfer (HGT) can explain unique values that lie around 38% and 54%; this part of the genome might have evolved in different conditions or have accumulated foreign genes as a result of HGT.   

1. **Conclusion:**

Mouse gut is a rich and diverse colony of living species, each of them evolved into various ecological niches under selective pressures. Some species have a high mutation rate due to reasons, such as, HGT transfer, strict environment etc. Optimal GC content of some genomes under specific conditions in mouse, as represented by the histogram, indicate strong natural selection corresponding to the environment.

**References:**

1. Cordero, O. P. (2014). Explaining microbial genomic diversity in light of evolutionary ecology. *Nat Rev Microbiol 12*. [Read the paper](https://www.nature.com/articles/nrmicro3218)
1. Gabaldón T, K. E. (2013). Functional and evolutionary implications of gene orthology. *Nat Rev Genet*. [Read the paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5877793/#:~:text=Walter%20Fitch1%2C2%20introduced,descent%20from%20their%20common%20ancestor.)
1. Kapli, P. Y. (2020). Phylogenetic tree building in the genomic age. *Nat Rev Genet 21*. [Read the paper](https://www.nature.com/articles/s41576-020-0233-0)
1. Koichiro Tamura, M. N. (2004). Prospects for inferring very large phylogenies by using the neighbor-joining method. [Read the paper](https://www.pnas.org/doi/epdf/10.1073/pnas.0404206101)
1. Singh, R. M. (2016). Comparative Analysis of GC Content Variations in Plant Genomes. *Tropical Plant Biology*. [Read the paper](https://link.springer.com/article/10.1007/s12042-016-9165-4)


