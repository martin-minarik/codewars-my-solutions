def find_missing(seq):
    '''
    :param seq: 
    :return: (((n + 1) * (a1 + an)) / 2) - sum(seq)
    '''
    return ((len(seq) + 1) * (seq[0] + seq[-1]) // 2) - sum(seq)