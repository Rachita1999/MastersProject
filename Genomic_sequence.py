import pandas as pd
from Bio import Entrez, SeqIO
import time
import requests
from requests.exceptions import RequestException
import pickle
import os

def fetch_genome_sequence(accession_number, start, end, email, api_key):
    """
    Fetch the genome sequence for the given accession number and region.

    Parameters:
    accession_number (str): The accession number of the genome.
    start (int): The start position of the region.
    end (int): The end position of the region.
    email (str): Email address to be used with NCBI Entrez.
    api_key (str): NCBI Entrez API key.

    Returns:
    str: The sequence in FASTA format.
    """
    Entrez.email = "your@email.com"  # Set the email address for NCBI Entrez
    Entrez.api_key = " "  # Set the API key for higher rate limits

    max_retries = 5
    for attempt in range(max_retries):
        try:
            # Fetch the genome record
            print(f"Fetching data for accession number {accession_number} (attempt {attempt + 1})...")
            handle = Entrez.efetch(db="nucleotide", id=accession_number, rettype="gb", retmode="text")
            record = SeqIO.read(handle, "genbank")
            handle.close()

            # Extract the sequence within the specified region
            sequence = record.seq[start-1:end]  # Adjusting to 0-based index

            # Print extracted sequence for debugging
            print(f"Extracted sequence: {sequence}")

            # Create FASTA format
            fasta_format = f">{record.id} {record.description} [{start}:{end}]\n{sequence}\n"

            return fasta_format
        except Exception as e:
            print(f"Error fetching data (attempt {attempt + 1}): {e}")
            time.sleep(5)  # Wait before retrying
    raise Exception("Failed to fetch genome sequence after multiple attempts.")

def save_fasta_sequence(fasta_sequence, output_file):
    """
    Save a single FASTA sequence to a file.

    Parameters:
    fasta_sequence (str): FASTA formatted sequence.
    output_file (str): The output file path.
    """
    with open(output_file, 'a') as file:
        file.write(fasta_sequence)

def save_checkpoint(checkpoint_file, index):
    """
    Save the current processing index to a checkpoint file.

    Parameters:
    checkpoint_file (str): The checkpoint file path.
    index (int): The current processing index.
    """
    with open(checkpoint_file, 'wb') as f:
        pickle.dump({'index': index}, f)

def load_checkpoint(checkpoint_file):
    """
    Load the processing index from a checkpoint file.

    Parameters:
    checkpoint_file (str): The checkpoint file path.

    Returns:
    int: The last processed index, or 0 if no checkpoint exists.
    """
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file, 'rb') as f:
            checkpoint = pickle.load(f)
            return checkpoint['index']
    return 0

def main():
    input_excel = r"/Path/Output/file.xlsx" # Replace with your input Excel file path
    output_file = r"/Path/Output/file.fasta"  # Replace with your desired output file path
    checkpoint_file = r"/content/checkpoint.pkl"  # Replace with your checkpoint file path
    email = "rachitag1999@gmail.com"  # Replace with your email
    api_key = "94c5dca4b936e703cefd00c4586875222708"  # Replace with your NCBI API key

    # Test connection to NCBI server
    url = "https://www.ncbi.nlm.nih.gov"
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Connected to NCBI server successfully!")
    except RequestException as e:
        print(f"Error connecting to NCBI: {e}")
        exit(1)

    # Read the Excel file
    df = pd.read_excel(input_excel)

    # Load the last processed index from the checkpoint
    start_index = load_checkpoint(checkpoint_file)

    # Loop through each row in the DataFrame starting from the last checkpoint
    for index in range(start_index, len(df)):
        row = df.iloc[index]
        accession_number = row['accession_numbers']
        start = row['start']
        end = row['end']

        try:
            fasta_sequence = fetch_genome_sequence(accession_number, start, end, email, api_key)
            save_fasta_sequence(fasta_sequence, output_file)
            print(f"FASTA sequence for {accession_number} saved to {output_file}")
        except Exception as e:
            print(f"Failed to retrieve data for {accession_number}: {e}")

        # Save checkpoint after each iteration
        save_checkpoint(checkpoint_file, index + 1)

if __name__ == "__main__":
    main()
