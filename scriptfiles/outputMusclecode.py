import os
import subprocess
from Bio import SeqIO

def parse_clusters(cluster_file):
    clusters = []
    with open(cluster_file, 'r') as file:
        for line in file:
            clusters.append(line.strip().split())
    return clusters

def extract_sequences(fasta_file, protein_ids):
    sequences = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        if record.id in protein_ids:
            sequences.append(record)
    return sequences

def write_fasta(sequences, output_file):
    SeqIO.write(sequences, output_file, "fasta")

def run_muscle(input_file, output_file):
    #os.system(f"muscle -in {input_file} -out {output_file}")
    command = ["muscle", "-in", input_file, "-out", output_file]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Muscle command: {e}")
        # Handle the error as needed
        
def main(cluster_file, fasta_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    clusters = parse_clusters(cluster_file)

    for i, cluster in enumerate(clusters, start=1):
        cluster_fasta = os.path.join(output_dir, f"Clust{i}.fa")
        cluster_aln = os.path.join(output_dir, f"Clust{i}.aln")
        
        # Extract sequences for the current cluster
        sequences = extract_sequences(fasta_file, cluster)
        
        # Write the sequences to a FASTA file
        write_fasta(sequences, cluster_fasta)
        
        # Run muscle command to create alignment
        run_muscle(cluster_fasta, cluster_aln)

        print(f"Cluster {i}: FASTA file '{cluster_fasta}' and alignment file '{cluster_aln}' created.")

if __name__ == "__main__":
    cluster_file = "/mnt/g/MastersProject/OProtein_clusters.txt"  # Replace with your actual cluster file
    fasta_file = "/mnt/g/MastersProject/output.faa"     # Replace with your actual FASTA file
    output_dir = "/mnt/g/MastersProject/outputwithMuscle"          # Replace with your desired output directory
    main(cluster_file, fasta_file, output_dir)

