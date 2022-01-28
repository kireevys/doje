# https://www.codewars.com/kata/556deca17c58da83c00002db/train/python
def tribonacci(signature, n):
    if n <= 0:
        return []

    if n <= len(signature):
        return signature[:n]

    while len(signature) != n:
        ln_sig = len(signature)
        next_num = sum(signature[ln_sig - 3:])
        signature.append(next_num)

    return signature
