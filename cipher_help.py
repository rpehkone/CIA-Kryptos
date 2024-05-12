import random
import re

#drops all the characters not needed in k1 and k2
#but maybe needed in k4
def get_kryptos_vigenere_table():
    lines = open("data/right.txt", 'r').readlines()
    for i, l in enumerate(lines):
        lines[i] = l.strip().lower()
    del lines[0]
    del lines[-1]
    del lines[-1]

    for i, l in enumerate(lines):
        lines[i] = l[1:27]
    return lines

def get_kryptos_ciphertexts():
    code_lines = open("data/left.txt", 'r').readlines()
    for i, l in enumerate(code_lines):
        code_lines[i] = list(l.strip().lower())

    k1 = code_lines[:2]
    k2 = code_lines[2:14]
    k3 = code_lines[14:25]
    #which one does the '?' belong to
    #Sanborn revealed that the four letters in positions 22–25, ...
    #so its part of k4
    end = k3[-1][-5:]
    k3[-1] = k3[-1][:-5]
    k4 = code_lines[25:]
    k4.insert(0, end)
    return k1, k2, k3, k4

def get_dictionary_list(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    lines = [line.split('/')[0].strip() + '\n' for line in lines if line.split('/')[0].strip()]
    res = []
    for line in lines:
        line = line.strip().lower()
        line = re.sub(r'[^a-z]', '', line)
        res.append(line)
    return res

def _init_dictionaries():
    res = get_dictionary_list('data/english.txt')
    res += get_dictionary_list('data/american.txt')
    res = sorted_words = sorted(res, key=len, reverse=True)
    res = set(res)
    return res

sorted_dictionary = _init_dictionaries()

def dictionary_split_string(s):
    result = []
    i = 0
    full_len = len(s)
    max_word_length = 10
    while i < full_len:
        matched = False
        for length in range(min(max_word_length, full_len - i), 0, -1):
            if s[i:i+length] in sorted_dictionary:
                result.append(s[i:i+length])
                i += length
                matched = True
                break
        if not matched:
            result.append(s[i])
            i += 1
    res_str = ' '.join(result)
    return res_str.replace(' ?', '?')

def average_word_length(sentence):
    words = sentence.split()
    total_length = sum(len(word) for word in words)
    if len(words) == 0:
        return 0
    average_length = total_length / len(words)
    return average_length

def replace_random_char(s):
    index_to_replace = random.randint(0, len(s) - 1)
    new_char = random.choice('abcdefghijklmnopqrstuvwxyz')
    s = s[:index_to_replace] + new_char + s[index_to_replace + 1:]
    return s
