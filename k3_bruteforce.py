import cipher_help
import cipher_ops
import random
import time

k1, k2, k3, k4 = cipher_help.get_kryptos_ciphertexts()

def table_random_op(table):
    r = random.randint(0, 2)
    opstr = ""
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
    return opstr, table

def random_solve_transposition(get_table):
    start_time = time.time()
    while True:
        table = get_table
        ops = []
        max_ops = 10
        opcount = random.randint(0, max_ops)
        for _ in range(opcount):
            op, table = table_random_op(table)
            ops.append(op)

        s = cipher_ops.table_to_string(table)
        s = cipher_help.dictionary_split_string(s)
        score = cipher_help.average_word_length(s)

        if score > 2.5:
            print(f"{ops} score: {score:.1f} took: {time.time() - start_time:.1f} seconds\n", s)
            return

random_solve_transposition(k3)
