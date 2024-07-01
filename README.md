# Masters Project
This is a Masters Study Project on Bioinformatics CRISPR Cas system Type 5.

Topic : Annotation and classification of Type 5 CRISPR CAS

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
