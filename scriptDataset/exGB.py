import re
import json
from copy import deepcopy


def screenplay(film_script_txt_file_path):
    slug_lines = r'(EXT\..*|INT\..*)'
    with open(film_script_txt_file_path, "r", encoding='utf-8') as f:
        film_string = f.readlines()
    mu: list = []
    people: list = []
    for line in film_string:

        valid = re.findall(slug_lines, line)
        if valid:
            # print(line)
            print(valid)
            mu.append(valid[0])
        if line.isupper():
            if not ('EXT.' in line or 'INT.' in line):
                # person.append(valid[0])
                print(line)
                people.append(line)
        if line.isupper():
            if not ('EXT.' in line or 'INT.' in line):
                # print(line)
                if '(' in line or '#' in line:
                    print(line)
                    people.append(line)
    return mu,people

# def person(film_script_txt_file_path):
#     # per1 = r'^[\s]+[A-Z]+\n'
#     # per2 = r'(?<=\s)+[A-Z]+\n'
#     # per3 = r'(?<=\s)+[A-Z]+.*[A-Z]+\n'
#     with open(film_script_txt_file_path, "r", encoding='utf-8') as f:
#         film_string = f.readlines()
#     people = []
#     for line in film_string:
#         if line.isupper():
#             if not ('EXT.' in line or 'INT.' in line):
#                 # person.append(valid[0])
#                 print(line)
#                 people.append(line)
#         if line.isupper():
#             if not ('EXT.' in line or 'INT.' in line):
#                 # print(line)
#                 if '(' in line or '#' in line:
#                     print(line)
#                     people.append(line)
#     #此处返回的是未处理过格式的person
#     return people

screenplay('GreenBooks.txt')

# person('GreenBooks.txt')