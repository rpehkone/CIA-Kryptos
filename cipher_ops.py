import numpy as np

def table_to_string(table):
    return "".join("".join(sublist) for sublist in table)

def reshape_string_to_table(s, w, h):
    return [list(s[i*w:(i+1)*w]) for i in range(h)]

def reshape_table(table, w, h):
    s = table_to_string(table)
    return reshape_string_to_table(s, w, h)

def table_rotate_clockwise(matrix):
    return [list(col) for col in zip(*matrix[::-1])]

def table_rotate_counterclockwise(matrix):
    matrix = table_rotate_clockwise(matrix)
    matrix = table_rotate_clockwise(matrix)
    matrix = table_rotate_clockwise(matrix)
    return matrix

def find_all_factors(n):
    res = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            j = n // i
            if i < j:
                res.append([i, j])
    return res

def decode_keyed_vigenere(cipher_table, vigenere_table, key):
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
