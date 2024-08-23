import numpy as np
import random

def table_to_string(table):
    return "".join("".join(sublist) for sublist in table)

def reshape_string_to_table(s, w, h):
    return [list(s[i*w:(i+1)*w]) for i in range(h)]

def reshape_table(table, w, h):
    s = table_to_string(table)
    return reshape_string_to_table(s, w, h)

def flatten_table(table):
    return [item for sublist in table for item in sublist]

def table_rotate_clockwise(matrix):
    return [list(col) for col in zip(*matrix[::-1])]

def table_rotate_counterclockwise(matrix):
    matrix = table_rotate_clockwise(matrix)
    matrix = table_rotate_clockwise(matrix)
    matrix = table_rotate_clockwise(matrix)
    return matrix

def find_all_factors_int(n):
    res = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            j = n // i
            if i < j:
                res.append([i, j])
    return res

def find_all_factors_table(table):
    s = table_to_string(table)
    return find_all_factors_int(len(s))

def decode_keyed_vigenere_char_questionmarks_included(cipher_table, vigenere_table, key):
    row_indices = [next(i for i, row in enumerate(vigenere_table) if row[0] == k) for k in key]
    
    cipher_flattened = []
    qmark_indices = []
    index = 0
    for row in cipher_table:
        for char in row:
            if char != '?':
                cipher_flattened.append(char)
            else:
                qmark_indices.append(index)
            index += 1

    cipher_filtered = np.array([ord(c) - ord('a') for c in cipher_flattened])

    repetitions_needed = len(cipher_filtered) // len(row_indices) + 1
    repetitions = (row_indices * repetitions_needed)[:len(cipher_filtered)]
    vigenere_numbers = [[ord(char) - ord('a') for char in row] for row in vigenere_table]
    vigenere_selected = [vigenere_numbers[r] for r in repetitions]

    decoded_matches = []
    for cipher_val, v_row in zip(cipher_filtered, vigenere_selected):
        decoded_row = [(cipher_val - v_char) % 26 for v_char in v_row]
        match_indices = [idx for idx, val in enumerate(decoded_row) if val == 0]
        decoded_matches.extend(match_indices)

    out_filtered = [vigenere_table[0][i] for i in decoded_matches]

    result_table = []
    non_qmark_index = 0
    index = 0
    for row in cipher_table:
        result_row = []
        for char in row:
            if index in qmark_indices:
                result_row.append('?')
            else:
                result_row.append(out_filtered[non_qmark_index])
                non_qmark_index += 1
            index += 1
        result_table.append(result_row)

    return result_table

def table_remove_questionmarks(cipher_table):
    for i in reversed(range(len(cipher_table))):
        for k in reversed(range(len(cipher_table[i]))):
            if cipher_table[i][k] == '?':
                del cipher_table[i][k]
    return cipher_table

def int_to_string(intlist):
    return ''.join([chr(num + ord('a')) for num in intlist])

def string_to_int(string):
    return [ord(char) - ord('a') for char in string]

def table_char_to_int(table):
    return [[ord(char) - ord('a') for char in row] for row in table]

def table_int_to_char(table):
    return [[chr(num + ord('a')) for num in row] for row in table]

def decode_keyed_vigenere_optimized(cipher_table, vigenere_table, key):
    vigenere_array = np.array(vigenere_table)
    key_indices = [np.where(vigenere_array[:, 0] == k)[0][0] for k in key]
    cipher_flattened = np.concatenate(cipher_table)
    indices = np.tile(key_indices, (len(cipher_flattened) // len(key_indices)) + 1)[:len(cipher_flattened)]
    selected_vigenere = vigenere_array[indices]
    decoded_values = (cipher_flattened[:, None] - selected_vigenere)
    decoded_indices = np.where(decoded_values == 0)[1]
    result_characters = vigenere_array[0, decoded_indices]
    result_table = []
    start = 0
    for row in cipher_table:
        end = start + len(row)
        result_table.append(result_characters[start:end].tolist())
        start = end
    return result_table
