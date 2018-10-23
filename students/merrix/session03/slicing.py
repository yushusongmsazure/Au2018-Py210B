def exchange_first_last(str_seq, tup_seq):
    strseq = list(str_seq)
    ''.join(strseq)
    strseq[0], strseq[-1] = strseq[-1], strseq[0]
    tup_seq[0], tup_seq[-1] = tup_seq[-1], tup_seq[0]
    a_new_sequence = (strseq, tup_seq)
     
    return a_new_sequence
    
    
a_string = ("this is a string")
a_tuple = [2, 54, 13, 12, 5, 32]

assert (exchange_first_last(a_string, a_tuple)) == "ghis is a strint" ()


