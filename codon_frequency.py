def codon_frequency(dna):
    dna = dna.upper()
    codon_freq = {}

    for i in range(0, len(dna) - 2, 3):
        codon = dna[i:i+3]
        if len(codon) == 3:
            codon_freq[codon] = codon_freq.get(codon, 0) + 1

    return codon_freq


sequence = input("Enter DNA sequence: ")
freq = codon_frequency(sequence)

print("Codon Frequencies:")
for codon, count in freq.items():
    print(codon, ":", count)
