from fasta import Seq, FastaReader

seq = Seq("test", "ATCGTUAACG")
print(f"Длина: {len(seq)}")
print(f"Тип: {seq.alphabet()}")

reader_one = FastaReader("homefasta3/exampels/Pezoporus_wallicus_exampels.fasta")
for sequence in reader_one:
    print(sequence)
