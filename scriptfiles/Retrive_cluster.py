import os
from Bio import SeqIO

def parse_clusters(cluster_file):
    clusters = {}
    with open(cluster_file, 'r') as file:
        cluster_id = 1
        for line in file:
            line = line.strip()
            if line:
                seq_ids = line.split()
                clusters[cluster_id] = seq_ids
                cluster_id += 1
    return clusters

def parse_fasta(fasta_file):
    sequences = {}
    for record in SeqIO.parse(fasta_file, 'fasta'):
        sequences[record.id] = record
    return sequences

def write_clusters_to_files(clusters, sequences, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for cluster_id, seq_ids in clusters.items():
        cluster_filename = os.path.join(output_dir, f'cluster_{cluster_id}.fa')
        with open(cluster_filename, 'w') as cluster_file:
            for seq_id in seq_ids:
                if seq_id in sequences:
                    SeqIO.write(sequences[seq_id], cluster_file, 'fasta')
                else:
                    print(f"Warning: {seq_id} not found in the FASTA file.")

def main(fasta_file, cluster_file, output_dir):
    clusters = parse_clusters(cluster_file)
    sequences = parse_fasta(fasta_file)
    write_clusters_to_files(clusters, sequences, output_dir)

if __name__ == "__main__":
    fasta_file = "/mnt/g/MastersProject/output.faa"
    cluster_file = "/mnt/g/MastersProject/OProtein_clusters.txt"
    output_dir = "/mnt/g/MastersProject/output"

    main(fasta_file, cluster_file, output_dir)
