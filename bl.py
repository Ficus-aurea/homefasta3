from Fasta import seq, Fasta

seq = seq("test", "ATCGTUAACG")
print(f"Длина: {len(seq)}")
print(f"Тип: {seq.alphabet()}")

reader_one = Fasta("homefasta3/exampels/Pezoporus_wallicus_exampels.fasta")
for sequence in reader_one:
    print(sequence)
