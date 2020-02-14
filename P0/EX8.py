from Seq0 import *

FOLDER = "../Session 4./"
ext = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "G", "T"]

for i in genes:
    seq = seq_read_fasta(FOLDER+i+ext)

    dict = seq_count(seq)
    list = [val for val in dict.values()]
    maximum = max(list)
    print("Gene", i, ': Most frequent base:', bases[list.index(maximum)])