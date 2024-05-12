import cipher_help
import cipher_ops
import numpy as np
import cipher_ops
import time


k1, k2, k3, k4 = cipher_help.get_kryptos_ciphertexts()
vigenere_table = cipher_help.get_kryptos_vigenere_table()

dictionary = cipher_help.get_dictionary_list('data/american.txt')
#human would probably pick word longer than 5? (improves speed by few sec)
dictionary = [word for word in dictionary if 5 <= len(word) <= 10]

def bruteforce_keyed_vigenere(cipher_table):
    start_time = time.time()
    for word in dictionary:
        s = cipher_ops.decode_keyed_vigenere(cipher_table, vigenere_table, word)
        s = cipher_ops.table_to_string(s)
        s = cipher_help.dictionary_split_string(s)
        score = cipher_help.average_word_length(s)
        if score > 2.5:
            print(f"{word} score: {score:.1f} took: {time.time() - start_time:.1f} seconds")
            return

bruteforce_keyed_vigenere(k1)
bruteforce_keyed_vigenere(k2)

def fix_typo_bruteforce(initial_key, correct_word, cipher_table):
    start_time = time.time()
    while True:
        key = initial_key
        key = cipher_help.replace_random_char(key)
        test = cipher_ops.decode_keyed_vigenere(cipher_table, vigenere_table, key)
        test = cipher_ops.table_to_string(test)
        if correct_word in test:
            print(f"Found typo fix key: {key} took: {time.time() - start_time:.1f} seconds")
            return

fix_typo_bruteforce("palimpsest", "illusion", k1)
fix_typo_bruteforce("abscissa", "underground", k2)
