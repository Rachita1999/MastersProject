def parse_fasta(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        protein_id = None
        sequence = []
        
        for line in infile:
            line = line.strip()
            if line.startswith('>'):
                # If there is an ongoing sequence, process it
                if protein_id is not None:
                    sequence_str = ''.join(sequence).replace('*', '')
                    length = len(sequence_str)
                    outfile.write(f"{protein_id}\t{length}\n")
                
                # Start a new record
                protein_id = line.split()[0][1:]
                sequence = []
            else:
                # Accumulate sequence lines
                sequence.append(line)
        
        # Process the last sequence in the file
        if protein_id is not None:
            sequence_str = ''.join(sequence).replace('*', '')
            length = len(sequence_str)
            outfile.write(f"{protein_id}\t{length}\n")

# Define the input and output file names
input_file = "G:\MastersProject\output.faa"
output_file = "G:\MastersProject\output\Olengthprotein.len.tab"

# Run the function
parse_fasta(input_file, output_file)
