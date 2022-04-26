import pytest


def test_logic():
    a1 = [9, 8, 7, 6, 5, 4, 3, 2]
    print(a1.sort())
    for i in range(0, len(a1)):
        for j in range(i, len(a1)):
            if a1[i] > a1[j]:
                temp = a1[i]
                a1[i] = a1[j]
                a1[j] = temp


    print(a1)
