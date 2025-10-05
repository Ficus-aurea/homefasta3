from fasta import FastaReader

def main():
    path = r"/home/anna/Документы/Anna/lab3sem(oop)/examples/Pezoporus_wallicus_exampels.fasta"
    try:
        fasta= FastaReader(path)

        if not fasta.is_fasta():
            return 'Указанный файл не является файлом формата Fasta'

        for i, seq_record in enumerate(fasta.read_records(), 1):
            print(f'Запись #{i}:')
            print(seq_record)
            print('-' * 50)

            if i >= 3:
                print('И так далее...')
                break
    except Exception as e:
        print(f'Произошла ошибка {e}')

if __name__ == "__main__":
    main()