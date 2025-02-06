import torch
import numpy as np
import pandas as pd
import os
import nltk
import re


# print("check versions")
# print("torch==" + torch.__version__)
# print("numpy==" + np.__version__)
# print("pandas==" + pd.__version__)
# print("nltk==" + nltk.__version__)
# print("check cuda")
# print("cuda is available:", torch.cuda.is_available())

data_path = './data/'
def get_books(book_names):
    books = []
    for book_name in book_names:
        file_path = data_path + book_name + '.txt'
        with open(file_path, 'r', encoding='utf-8') as f:
            books.append(f.read())
    return books

def clean_text(text):
    # Убираем лишние пробелы и переносы
    text = re.sub(r"\s+", " ", text).strip()  # Убираем лишние пробелы

    # Убираем мусорные символы (спецсимволы, кроме букв, цифр и базовых знаков)
    text = re.sub(r"[^\w\s.,!?]", "", text)

    # Убираем пробелы между буквами в словах
    text = text.strip()

    return text

books_names = ['pelevin_buben_1',
              'pelevin_crazy_pustota',
              'pelevin_generation_p',
              'pelevin_iphuck10',
              'pelevin_transhumanizm_inc',
              'pelevin_yellow_arrow']
books = get_books(books_names)

print(books[0][:100])
print(clean_text(books[0][:100]))

