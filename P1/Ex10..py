from Seq1 import Seq

print("----Exercise 10----")
FOLDER = "../Session 4./"
ext = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", 'RNU6_269P']
bases = ["A", "C", "G", "T"]

for i in genes:
    s1 = Seq("")
    seq = read_fasta(FOLDER+i+ext)
    dict = count(seq)
    best = ''
    maximum = 0
    for x, val in dict.items():
        while val > maximum:
            maximum = val
            best = x
    print("Gene", i, ': Most frequent base:', best)