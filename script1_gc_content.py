def gc_content(dna):
    dna = dna.upper()
    g = dna.count('G')
    c = dna.count('C')
    return ((g + c) / len(dna)) * 100


sequence = input("Enter DNA sequence: ")
gc = gc_content(sequence)

print("DNA Sequence:", sequence)
print("GC Content:", round(gc, 2), "%")
