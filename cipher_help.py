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

def get_dictionary(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    lines = [line.split('/')[0].strip() + '\n' for line in lines if line.split('/')[0].strip()]
    res = [line.strip().lower() for line in lines]
    return res

def dictionary_split_string(s, words):
    result = []
    i = 0
    while i < len(s):
        matched = False
        for word in sorted(words, key=len, reverse=True):
            if s[i:i+len(word)] == word:
                result.append(word)
                i += len(word)
                matched = True
                break
        if not matched:
            result.append(s[i])#add ?
            # print('no words matched')
            i += 1
    res_str =  ' '.join(result)
    return res_str.replace(' ?', '?')

def average_word_length(sentence):
    words = sentence.split()
    total_length = sum(len(word) for word in words)
    if len(words) == 0:
        return 0
    average_length = total_length / len(words)
    return average_length
