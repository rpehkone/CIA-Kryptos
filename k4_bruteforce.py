import cipher_help
import cipher_ops
import threading
import random
import copy
import time

k1, k2, k3, k4 = cipher_help.get_kryptos_ciphertexts()
vigenere_table = cipher_help.get_kryptos_vigenere_table()

# k4 = cipher_ops.table_remove_questionmarks(k4)
# k4 = cipher_ops.table_to_string(k4)
# print(cipher_help.english_probability(k4))
# 26.718793814433013
# exit(0)

dictionary = cipher_help.get_dictionary_list('data/american.txt')
dictionary = [word for word in dictionary if 5 <= len(word) <= 10]

# maybe rewrite like 1 vigenere per test,
# and for every op combination try the whole dictionary
# i think that might solve under 30h, if constraints correct

def table_random_op(table):
    r = random.randint(0, 4)
    opstr = ""
    #should implement this such that:
        # can't do the inverse of previous op
        # no 2 consecutive reshapes
        # vigenere add support for non rectangular?

    match r:
        case 0:
            table = cipher_ops.table_rotate_clockwise(table)
            opstr = "clockwise"
        case 1:
            table = cipher_ops.table_rotate_counterclockwise(table)
            opstr = "counterclockwise"
        case 2:
            #assume only reshapes without truncation or padding
            factors = cipher_ops.find_all_factors_table(table)
            new_size = random.choice(factors)
            swap = random.randint(0, 1)
            if swap:
                table = cipher_ops.reshape_table(table, new_size[0], new_size[1])
                opstr = "reshape " + str(new_size[0]) + " " + str(new_size[1])
            else:
                table = cipher_ops.reshape_table(table, new_size[1], new_size[0])
                opstr = "reshape " + str(new_size[1]) + " " + str(new_size[0])
        case 3:
            random_key = random.choice(dictionary)
            table = cipher_ops.decode_keyed_vigenere(table, vigenere_table, random_key)
            opstr = "vigenere " + random_key
        case 4:
            special_words = ["palimpsest", "iqlusion", "palimpcest", "illusion", "abscissa", "undergruund", "abvcissa", "underground",
                             "desparatly", "desperately", "kryptos", "polonium"]

            random_key = random.choice(special_words)
            table = cipher_ops.decode_keyed_vigenere(table, vigenere_table, random_key)
            opstr = "vigenere " + random_key
        # case 4:
        #     resize to any size with padding
        # case 4:
        #     padding left
        # case 4:
        #     hill cipher (because its written on the sculpture)
        # case 4:
        #     playfair cipher (because repeating letters in k4)
        # case 4:
        #     shuffle rows
        # case 5:
        #     shuffle columns
        # Ciphers by family	
        #     Polyalphabetic	
        #         AlbertiEnigmaTrithemiusVigenère
        #     Polybius square	
        #         ADFGVXBifidNihilistTap codeTrifidVIC cipher
        #     Square	
        #         PlayfairTwo-squareFour-square
        #     Substitution	
        #         AffineAtbashAutokeyBeaufortCaesarChaocipherGreatHillPigpenROT13Running key
        #     Transposition	
        #         ColumnarDoubleMyszkowskiRail fenceRoute
    return opstr, table

def random_solve(get_table):
    start_time = time.time()
    while True:
        table = copy.deepcopy(get_table)
        ops = []
        max_ops = 8#because designed with paper its some low number?
        opcount = random.randint(2, max_ops)
        for _ in range(opcount):
            op, table = table_random_op(table)
            ops.append(op)

        s = cipher_ops.table_to_string(table)
        s = cipher_help.dictionary_split_string(s)
        score = cipher_help.average_word_length(s)

        # 'clock' is bad, too many falses
        known = ["berlin", "eastnorth", "northeast"]
        for k in known:
            if k in s:
                print(f"{k}    {ops} score: {score:.1f} took: {time.time() - start_time:.1f} seconds\n", s)
        if score > 2.3:
            print(f"{ops} score: {score:.1f} took: {time.time() - start_time:.1f} seconds\n", s)
            # return

threads = []
for i in range(24):
    thread = threading.Thread(target=random_solve, args=(k4,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
    exit(0)
