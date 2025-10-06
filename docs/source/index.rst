Fasta Project — Документация
=============================

.. role:: badge
.. role:: muted

:badge:`Версия 0.1.0`

Простая библиотека для чтения FASTA-файлов. Классы ``Seq`` и ``FastaReader``.

.. toctree::
   :maxdepth: 2
   :caption: Содержание:
   
   api

Введение
--------

Этот проект реализует два простых класса для работы с FASTA-файлами:

* **Seq** — хранит заголовок и последовательность, умеет возвращать длину, красиво представлять себя в FASTA-формате и определять, нуклеотид это или белок.
* **FastaReader** — потоковый (генераторный) ридер FASTA-файлов: читает файл построчно и возвращает объекты ``Seq``, не загружая весь файл в память.

Установка
---------

:muted:`Репозиторий предполагает минимальные зависимости — только Python 3.6+.`

.. card::

   **Локальная установка (рекомендуется):**
   
   .. code-block:: bash
   
      python -m venv .venv
      source .venv/bin/activate  # Linux / macOS
      .venv\Scripts\activate     # Windows
      pip install -U pip

   :muted:`Если у тебя есть` ``pyproject.toml`` :muted:`или` ``setup.py``, :muted:`можно установить проект в editable-режиме:`
   
   .. code-block:: bash
   
      pip install -e .

Быстрый старт
-------------

Небольшой пример: создаём файл ``example.fasta`` с двумя записями, а затем читаем его.

.. grid::

   .. grid-item::
   
      **example.fasta**
      
      .. code-block:: text
      
         >seq1
         ACGTACGTACGT
         >protein1
         MKTWQILV

   .. grid-item::
   
      **demo.py**
      
      .. code-block:: python
      
         from fasta import Seq, FastaReader
         
         reader = FastaReader('example.fasta')
         for i in reader:
             print(i.title, len(i), i.alphabet())

.. example-output::

   **Ожидаемый вывод:**
   
   .. code-block:: text
   
      seq1 12 nucleotide
      protein1 8 protein

Примеры
-------

1. **Сводка по файлу**

   .. code-block:: python
   
      from fasta import FastaReader
      
      reader = FastaReader('example.fasta')
      for i in reader:
          print(f"{i.title}: length={len(i)}, type={i.alphabet()}")

2. **Фильтрация по длине**

   .. code-block:: python
   
      min_len = 100
      for i in FastaReader('large.fasta'):
          if len(i) >= min_len:
              # обработать или сохранить
              pass

3. **Сохранение отфильтрованных записей**

   .. code-block:: python
   
      with open('filtered.fasta','w') as out:
          for i in FastaReader('data.fasta'):
              if i.alphabet() == 'nucleotide' and len(i) >= 200:
                  out.write(str(i) + '\n')

FAQ и советы
------------

**Как работать с большими FASTA-файлами?**

Используй ``for i in FastaReader('big.fasta'):`` — благодаря генератору память остаётся небольшой.

**Как поддержать .gz файлы?**

Проверяй расширение файла: если заканчивается на ``.gz``, используй ``gzip.open(path, 'rt')`` вместо ``open``.

**Что если файл содержит некорректные символы?**

:muted:`Можно добавить в Seq проверку и выбрасывать` ``ValueError`` :muted:`при встрече запрещённых символов, либо возвращать` ``'unknown'`` :muted:`в методе` ``alphabet()``.

**Как опубликовать на ReadTheDocs?**

1. Добавь Sphinx-конфигурацию и docs/ в репозиторий.
2. Создай ``requirements-docs.txt`` с зависимостями (sphinx, тема).
3. Зарегистрируй репозиторий на readthedocs.org и настрой сборку.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

