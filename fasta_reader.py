filename = input("Enter FASTA file name: ")

with open(filename, 'r') as file:
    sequence = ""
    for line in file:
        if not line.startswith(">"):
            sequence += line.strip()

print("DNA Sequence from FASTA:")
print(sequence)
print("Length:", len(sequence))
