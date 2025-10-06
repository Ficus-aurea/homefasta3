# homefasta3

Python библиотека для чтения и анализа файлов в формате FASTA.

## Возможности

- Чтение FASTA файлов любого размера
- Автоматическое определение типа последовательности (ДНК/РНК/белковая)
- Получение информации о последовательностях
- Валидация формата FASTA файлов

## Установка

```bash

# Клонируйте репозиторий
git clone https://github.com/Seitsan/FastaReader.git
cd homefasta3
```

## Быстрый старт

```python
from fasta import Seq, FastaReader

# Создание последовательности
seq = Seq("test_sequence", "ATCGATCG")
print(seq)  # Seq('test_sequence', 8, nucleotide)

# Чтение FASTA файла
reader = FastaReader("Pezoporus_wallicus_exampels.fasta")
for sequence in reader:
    print(f"{sequence.title}: {len(sequence)} bp")
```

## Пример вывода
```text
Запись #1:
Заголовок fasta: sequence_1 description
Длина последовательности: 150
Алфавит последовательности: ДНК
Первые 50 символов последовательности: ATGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA

--------------------------------------------------
```

## Структура проекта

```text
homefasta3/
├── Fasta/              # Исходный код
│   ├── m.py
│   ├── seq.py
│   └── fasta.py
├── docs/               # Документация
│   ├── source/
│   └── build/
├── examples/           # Примеры FASTA файлов
├── bl.py            # Демонстрация
└── README.md          # Этот файл
```



## Разработка

### Демонстрация
Запустите демонстрационную программу:

```bash
python demo.py
```

### Документации

HTML документация находится в `docs/build/html/index.html`

Чтобы пересобрать документацию:
```bash
cd docs
sphinx-build -b html source build
```

## Лицензия
Этот проект распространяется под лицензией MIT. См. файл `LICENSE` для подробностей.

# Для разработки и документации:
sphinx>=4.0.0
sphinx-rtd-theme>=1.0.0
pytest>=6.0.0
