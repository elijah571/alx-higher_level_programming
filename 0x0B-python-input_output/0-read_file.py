#!/usr/bin/python3
def read_file(filename=""):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)
