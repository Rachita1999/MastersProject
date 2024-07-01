# Masters Project
This is a Masters Study Project on Bioinformatics CRISPR Cas system Type V.

Topic : Annotation and classification of Type V CRISPR CAS

## Overview
This project provides a comprehensive pipeline for genomic sequence analysis. It includes steps for extracting genomic sequences based on accession numbers, generating prodigal files, creating similarity matrices, clustering using MCL, performing multiple sequence alignments, and building Hidden Markov Models (HMM) for each alignment.

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
    1. [Genomic Sequence Extraction](#genomic-sequence-extraction)
    2. [Prodigal File Generation](#prodigal-file-generation)
    3. [Similarity Matrix Generation](#similarity-matrix-generation)
    4. [Clustering by MCL](#clustering-by-mcl)
    5. [Multiple Sequence Alignment](#multiple-sequence-alignment)
    6. [HMM Build](#hmm-build)
4. [Contributing](#contributing)
5. [License](#license)

## Requirements

- Python 3.6+
- Biopython
- Prodigal
- BLAST+
- MCL
- MUSCLE
- HMMER

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Rachita1999/MastersProject.git
    cd MastersProject
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure the external tools (Prodigal, BLAST+, MCL, MUSCLE, HMMER) are installed and accessible from your PATH.

## Usage

### Genomic Sequence Extraction

Extract genomic sequences from given accession numbers and specified start and end regions.

Code can be found at Genomic_sequence.py

## Prodigal File Generation

Generate prodigal files from the extracted genomic sequences.

```
prodigal -i fullresults.fasta -o output.gbk -a output_Protein_Seqs.faa -c -m -g 11 -p meta
```

Code can be found at Prodigal_Generation.py

## Similarity Matrix Generation

Generate a similarity matrix using protein sequences.

```
output_ProteinSeqs.faa output_ProteinSeq.faa -m 8 > output_ProteinSeq.fastab
```
For every protein, length is calculated and stored with separation by tab. 

### Calculation of Coverage 

```
cat output_ProteinSeq.fastab | bin/hashcol Olengthprotein.len.tab | bin/hashcol Olengthprotein.len.tab 2 | awk '{print $1 "\t" $2 "\t" $11 "\t" $13/$14 "\t" ($8-$7)/(2*$13)+($10-$9)/(2*$14) "\t" ($7+$8-$9-$10)/($13+$14)}' > ProteinSeq.fastab.coverage
```

## Clustering by MCL

Cluster proteins using the MCL algorithm.

``` cat ProteinSeq.fastab.coverage  | awk '{if ($3 <= 1) print}' | awk '{if ($5 >= 0.4) print}' | awk '{if (sqrt(($4-1)^2) - (sqrt(sqrt($5))-.8) + sqrt($6^2) <= 0.1) print $1 "\t" $2}' | bin/mcl - -o - --abc -I 1.2 > OProtein_clusters.txt```

## Multiple Sequence Alignment

Generate multiple sequence alignments using the MUSCLE tool.

```muscle -in Cluster_1.fa -out  Cluster_1.aln ```



