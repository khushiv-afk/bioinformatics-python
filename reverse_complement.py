def reverse_complement(dna):
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    dna = dna.upper()
    rev_comp = ""

    for base in reversed(dna):
        rev_comp += complement[base]

    return rev_comp


sequence = input("Enter DNA sequence: ")
print("Reverse Complement:", reverse_complement(sequence))
