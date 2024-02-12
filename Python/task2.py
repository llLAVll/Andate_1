#!/usr/bin/python3
# -*- coding: utf-8 -*-

def add_line_numbers(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()

        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for i, line in enumerate(lines, start=1):
                output_file.write(f"{i}: {line}")

        print(f"Файл успешно создан: {output_filename}")
    except FileNotFoundError:
        print(f"Файл '{input_filename}' не найден.")

def main():
    input_filename = input("Введите имя исходного файла: ")
    output_filename = input("Введите имя целевого файла: ")

    add_line_numbers(input_filename, output_filename)

if __name__ == "__main__":
    main()