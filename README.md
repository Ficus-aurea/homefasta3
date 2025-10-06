# homefasta3
Python библиотека для чтения и анализа файлов в формате FASTA.

# Возможности
-Чтение FASTA файлов любого размера
-Автоматическое определение типа последовательности (ДНК/РНК/белковая)
-Получение информации о последовательностях
-Валидация формата FASTA файлов

# Установка

Клонируйте репозиторий
git clone https://github.com/Seitsan/FastaReader.git
cd FastaReader
Быстрый старт
from fasta_reader import FastaReader

# Создайте объект для чтения FASTA файла
reader = FastaReader("example.fna")

# Проверьте формат файла
if reader.is_fasta():
    # Читайте записи последовательностей
    for i, seq_record in enumerate(reader.read_records(), 1):
        print(f"Запись #{i}:")
        print(seq_record)
        print("-" * 50)
else:
    print("Файл не является корректным FASTA файлом")

Пример вывода
Запись #1:
Заголовок fasta: sequence_1 description
Длина последовательности: 150
Алфавит последовательности: ДНК
Первые 50 символов последовательности: ATGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA

--------------------------------------------------
# Структура проекта
FastaReader/
├── fasta_reader.py  # Основной класс для чтения FASTA
├── seq.py           # Класс для работы с последовательностями
├── main.py          # Пример использования
├── docs/            # Документация
├── tests/           # Тесты
└── examples/        # Примеры файлов
Документация
Полная документация доступна в папке docs/

# Разработка
Запуск тестов
python -m pytest tests/
Сборка документации
cd docs
sphinx-build -b html source build
Лицензия
Этот проект распространяется под лицензией MIT. См. файл LICENSE для подробностей.

# Вклад в проект
Форкните репозиторий
Создайте ветку для новой функциональности (git checkout -b feature/amazing-feature)
Закоммитьте изменения (git commit -m 'Add some amazing feature')
Запушьте в ветку (git push origin feature/amazing-feature)
Создайте Pull Request
requirements.txt

# Для основных функций зависимости не требуются

# Для разработки и документации:
sphinx>=4.0.0
sphinx-rtd-theme>=1.0.0
pytest>=6.0.0
