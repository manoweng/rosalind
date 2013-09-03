#!/usr/bin/python

# ID: SUBS
# TITLE: Combing Through the Haystack

def find_motif(dna1, dna2):
  motif_index = []
  count = 0
  for i in range(0, len(dna1)):
    if dna1[i] == dna2[0]:
      for j in range(0, len(dna2)):
        if i+j < len(dna1):
          if dna1[i + j] == dna2[j]:
            count += 1
          else:
            break
      if count == len(dna2):
        motif_index.append(i + 1)
      count = 0
  return motif_index
  
dna1 = 'ATTCCCAATTCCCAGTATTCCCATATTCCCAAATTCCCAAGGCATTCCCAATTCCCAGATTCCCATGCATTCCCAGAGTGGGATTCCCAAACATTCCCAGGTATTCCCAATATTCCCAATTCCCATATTCCCAATTCCCAATTCCCAACCATTCCCACATTCCCAGTTATTCCCATTTTTATTCCCAATTCCCAGATTCCCAATGCCGTATTCCCACCGAATGGAATTCCCAATTCCCATATTCCCAACATTCCCAATTCCCAATTCCCACGGATTCCCAATTCCCAATTCCCAAAGGGAATTCCCAATACCAGTCTATTCCCAGGTATTCATTCCCACACTTCAATTCCCACTAATTCCCAATTCCCATGTTGATTCCCAGAGCGATTCCCAAACGCATTCCCATATTCCCAATTCCCATGGATCGAAGATTCCCATTATTCCCAAATTCCCAACAATTCCCAATTCCCATAATTCCCAGATTCCCAGATTCCCAATTCCCACGCATTCCCATATTCCCACTATTCCCAATTCCCAATGCATTCCCAATTCCCAGGCAATTCCCAATTCCCAGCATTCCCATATTCCCATATTCCCAGGCATTCCCACATTCCCAGGATTCCCAATTCCCAATTCCCATAATTCCCAGTTTAGTAATATTCCCAATTCCCATATATTCCCAGTACTCATTCCCAGTTAATTCCCAACTATTCCCACACAGGATTCCCAATTCCCAATTCCCACATTCCCATATTCCCAAATATTCCCAGAAATCATTCCCACCAATTCCCAATTTATTCCCAAGACCAGCCCACGATTCCCAATTCCCAACGCCATTCCCAAATTCCCA'
dna2 = 'ATTCCCAAT'
print find_motif(dna1, dna2)