#!/usr/bin/python

# ID: DNA
# TITLE: Counting DNA Nucleotides

# funcao para comparar cada caracter na string
def count(dna):
  A, T, C, G = 0, 0, 0, 0
  for i in dna:
    if i == 'A':
      A = A + 1
    elif i == 'C':
      C = C + 1
    elif i == 'G':
      G = G + 1
    elif i == 'T':
      T = T + 1
  print A, C, G, T

# string a ser avaliada
dna = '''AACCCCCTAATAGTGAAAGCACGGCGACTTTTGGATTCCGGTGTCATCCTATAAGGG
      GTTGTTGGCCTATAAATCTCTCAAATTTCTATATACTTAGCGAGGGCTCTTAATCTT
      ATGGGGCCTAGCCGCACCAAGGGATGCACTTGCTTCTTCCGACGTAATACGCTATTG
      ACATAAAAGAAGGCAAGTTATTAGGGTTGGGTAGTACACGTGGGTTGTGAGGATTCC
      CAATCGATGCGTAGACATCGATATTTCGCACAGGTATTGTCCTATTCAAGGAGTACG
      ACGAGGTACACGATTTGGGAATGTCAGGGCGCCTTAGGCCATTGCTCGTCAAATTCC
      ACAGCCGCACAATTGTCCGCACTTCCTTGGCACCCCGCCGTGTTGGCTTCTAATATA
      GTAGCTACGGGTATCAGGCTATGATGCCGTGGCCCGAGGCCACCCCTTAGTTCGGGC
      TTCCAGGATCAGACGACAATTACTGCATCGCGTCCAGGATACCCTCTGATGCCGGTA
      GAAATGGTAGTACCCTGGATCGATTTTTCGGACTTAGAATGGAAAACCCCCGATGTT
      GTGGTAGTCCATCGTACCCAGAACTATTTTGGCAAGTTGGATCAAAATACAGACTGA
      CGTCGCTGAGTCTGTGGAGTATGGGCACGTAGTGTATAGAAATCACTTGCACAGGGA
      GCACAATTACGACGCCTGGTTTTTACGTGACAATTACCGGGGCTACTTACCCGTTAT
      AGACCCCTGACCGGCGACCAAAACTTATGGGGTATTCCTCCTCTTTAGTCTCGGTGA
      TCCGCTCGTAGGTCAGTTAAATCCATTTACTCGGCATGGTACACCCGCATCTAAGAG
      CTGCGAATAGGCATGGAAAAGATTTGTACACAACAGAAATAGTTCCTAGCTGCTCAC
      CGAGCTGGTGCCGTCCGTCTTTGCTTTTTTTCGTCGACACCGTGGTTGTAATTCATA
      GGGTATGTCATCCA'''
dna = dna.upper()

count(dna)
