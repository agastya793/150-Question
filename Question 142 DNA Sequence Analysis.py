''' DNA Sequence Analysis

In bioinformatics, a DNA sequence is a string of four letters — A, T, C, G — representing nucleotide bases:

A = Adenine

T = Thymine

C = Cytosine

G = Guanine

These form the genetic code and can be analyzed to find patterns, count bases, create complementary strands, transcribe to RNA, and calculate composition metrics.'''

''' write functions to perform these analyses:

Count nucleotides

Find the complementary DNA strand

Find a pattern in the DNA

Transcribe DNA to RNA

Calculate % of GC content'''

def count_nucleotides(dna):
    counts = {"A":0, 'T': 0, "C": 0, "G": 0}
    for base in dna:
        if base in counts:
            counts[base]  += 1
    return counts   

dna =   "ATGCGATCCATGACAAT"
print(count_nucleotides(dna))   


# complementary DNA strand
# in DNA : A pairs with T and C pairs with G

def complementary_strand(dna):
    comp = ""
    for base in dna:
        if base == 'A':
            comp += 'T'
        elif base == 'T' :
            comp += 'A'   
        elif base == 'C' :
            comp += 'G'  
        elif base == 'G'  :
            comp += 'C'  
    return comp

print(complementary_strand("ATGCGATTCA"))


# FIND PATTERN IN DNA

def find_pattern(dna,pattern):
    positions =[]

    length = len(pattern)
    for i in range(len(dna) - length + 1):
        if dna[i:i+length] == pattern:
            positions.append(i)
    return positions        

dna = "ATAGCGATATCGAGCTAC"
print(find_pattern(dna, "AGC"))

''' Transcribe DNA to RNA

Goal: Replace all T bases with U to simulate RNA.

DNA → RNA: Replace Thymine (T) with Uracil (U)'''

def transcribe_DNA_to_RNA(dna):
    return dna.replace('T','U')

print(transcribe_DNA_to_RNA("ATGCTAGCT"))

'''Calculate the percentage of bases that are G or C.

 Why It Matters

GC content is important in genetics — higher GC often means more stable DNA.'''

def gc_content(dna):
    gc_count = dna.count('G') + dna.count('C')
    return (gc_count / len(dna)) * 100

print(gc_content("ATGCGAT"))
