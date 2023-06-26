""" BinaryGap
    Find longest sequence of zeros in binary representation of an integer.
"""
def solution(N):
    binary_n = format(N, 'b')
    binary_n = binary_n.strip('0')
    binary_n = binary_n.split('1')
    return len(max(binary_n))