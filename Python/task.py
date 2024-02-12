#!/usr/bin/python3
# -*- coding: utf-8 -*-

def find_min_punctuation_sentence(text):
    sentences = text.split('.')  # Разделение текста на предложения по точкам
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]  # Удаление лишних пробелов и пустых предложений

    min_punctuation_count = float('inf')
    min_punctuation_sentence = None
    
    for sentence in sentences:
        punctuation_count = sum(1 for char in sentence if char in '.,;:!?')  # Подсчёт знаков пунктуации в предложении
        if punctuation_count < min_punctuation_count:
            min_punctuation_count = punctuation_count
            min_punctuation_sentence = sentence
    
    return min_punctuation_sentence

def main():
    filename = input("Введите имя файла для чтения: ")
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        
        min_punctuation_sentence = find_min_punctuation_sentence(text)
        
        if min_punctuation_sentence:
            print("Предложение с минимальным количеством знаков пунктуации:")
            print(min_punctuation_sentence)
        else:
            print("В файле нет текста или нет предложений.")
    
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")

if __name__ == "__main__":
    main()