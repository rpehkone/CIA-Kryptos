import cipher_help
import cipher_ops
import numpy as np
import cipher_ops
import time

k1, k2, k3, k4 = cipher_help.get_kryptos_ciphertexts()
vigenere_table = cipher_help.get_kryptos_vigenere_table()

k1 = cipher_ops.table_remove_questionmarks(k1)
k2 = cipher_ops.table_remove_questionmarks(k2)
k1 = cipher_ops.table_char_to_int(k1)
k2 = cipher_ops.table_char_to_int(k2)
vigenere_table = cipher_ops.table_char_to_int(vigenere_table)

dictionary = cipher_help.get_dictionary_list('data/american.txt')
#human would probably pick word longer than 5? (improves speed by few sec)
dictionary = [word for word in dictionary if 7 <= len(word) <= 11]
print(len(dictionary))
dictionary = [s for s in dictionary if len(set(s)) >= 5]
print(len(dictionary))
dictionary = [cipher_ops.string_to_int(word) for word in dictionary]

def bruteforce_keyed_vigenere(cipher_table):
    start_time = time.time()
    for intword in dictionary:
        s = cipher_ops.decode_keyed_vigenere_optimized(cipher_table, vigenere_table, intword)
        score = cipher_help.english_probability_int(cipher_ops.flatten_table(s))

        # s = cipher_ops.table_int_to_char(s)
        # s = cipher_ops.table_to_string(s)
        # score = cipher_help.english_probability(s)

        # s = cipher_help.dictionary_split_string(s)
        # score = cipher_help.average_word_length(s)
        # if score > 2.5:

        if int(score) > 65:
            print(f"{cipher_ops.int_to_string(intword)} english probability: {score:.1f} took: {time.time() - start_time:.3f} seconds")
            return
    print("bruteforce failed")

bruteforce_keyed_vigenere(k1)
bruteforce_keyed_vigenere(k2)

def fix_typo_bruteforce(initial_key, correct_word, cipher_table):
    start_time = time.time()
    while True:
        key = initial_key
        key = cipher_help.replace_random_char(key)
        intword = cipher_ops.string_to_int(key)
        test = cipher_ops.decode_keyed_vigenere_optimized(cipher_table, vigenere_table, intword)
        test = cipher_ops.table_to_string(cipher_ops.table_int_to_char(test))
        if correct_word in test:
            print(f"Found typo fix key: {key} took: {time.time() - start_time:.3f} seconds")
            return

fix_typo_bruteforce("palimpsest", "illusion", k1)
fix_typo_bruteforce("abscissa", "underground", k2)
