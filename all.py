class Seq:
    def __init__(self, header, sequence):

        self.header = header.strip() if header else ''
        self.sequence = sequence


    def __len__(self):

        """
        Возвращает длину последовательности.

        Returns
        -------
        int
            Длина последовательности
        """

        return len(self.sequence)


    def alphabet_validation(self):

        """
        Определяет алфавит последовательности на основе уникальных символов.

        Returns
        -------
        str
            'белковый', 'ДНК', 'РНК', 'смешанный' или 'пустая'

        Notes
        -----
        Использует статистический анализ для определения типа последовательности
        на основе уникальных символов, характерных для каждого алфавита.
        """

        protein_alphabet = set("DEFHIKLMNPQRSTVWY*")
        nucleotide_alphabet = set("ACGTU")

        clean_sequence = ''.join(char for char in self.sequence.upper()
                                 if char.isalpha() or char == '*')

        if not clean_sequence:
            return "пустая"

        seq_chars = set(clean_sequence)

        unique_protein_chars = protein_alphabet - nucleotide_alphabet

        if any(char in unique_protein_chars for char in seq_chars):
            return 'белковый'
        elif seq_chars.issubset(nucleotide_alphabet):
            if 'U' in seq_chars and 'T' not in seq_chars:
                return 'РНК'
            else:
                return 'ДНК'
        else:
            return 'смешанный'


    def __str__(self):
        return f'''
Заголовок fasta: {self.header}
Длина последовательности: {len(self)}
Алфавит последовательности: {self.alphabet_validation()}
Первые 50 символов последовательности: {self.sequence[:50]}'''
    


import os


class FastaReader:
    """
    Класс для чтения файла в формате fasta.

    Attributes:
        path_to_file (str): Путь к файлу fasta
    """

    def __init__(self, path_to_file):
        """
        Инициализирует объект FastaReader.

        Raises:
            FileNotFoundError: Если файл не существует
        """

        if not os.path.exists(path_to_file):
            raise FileNotFoundError(f"Файл не найден: {path_to_file}")

        self.path_to_file = path_to_file

    def _is_fasta(self):
        """
        Проверяет, имеет ли файл допустимый формат fasta.
        """

        try:
            with open(self.path_to_file, "r", encoding="utf-8") as file:
                first_line = file.readline().strip()
                return first_line.startswith(">")
        except:
            return False

    def __iter__(self):
        """
        Перебирает последовательности с помощью генератора.
        """

        title = None
        sequence_lines = []

        with open(self.path_to_file, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                if line.startswith(">"):
                    if title is not None:
                        yield Seq(title, "".join(sequence_lines))
                    title = line[1:]
                    sequence_lines = []
                else:
                    sequence_lines.append(line)

        if title is not None:
            yield Seq(title, "".join(sequence_lines))