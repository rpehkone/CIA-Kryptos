import cipher_help
import cipher_ops

k1, k2, k3, k4 = cipher_help.get_kryptos_ciphertexts()
table = cipher_help.get_kryptos_vigenere_table()

s1 = cipher_ops.decode_keyed_vigenere(k1, table, "palimpsest")
s1 = cipher_ops.table_to_string(s1)
s1 = cipher_help.dictionary_split_string(s1)
print(s1 + "\n")



s2 = cipher_ops.decode_keyed_vigenere(k2, table, "abscissa")
s2 = cipher_ops.table_to_string(s2)
s2 = cipher_help.dictionary_split_string(s2)
print(s2 + "\n")



k3 = cipher_ops.reshape_table(k3, 24, 14)
k3 = cipher_ops.table_rotate_counterclockwise(k3)
k3 = cipher_ops.reshape_table(k3, 8, 42)
k3 = cipher_ops.table_rotate_counterclockwise(k3)
s3 = cipher_ops.table_to_string(k3)
s3 = cipher_help.dictionary_split_string(s3)
print(s3 + "\n")
