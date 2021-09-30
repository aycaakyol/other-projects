import os
import sys
import os.path
from os import path

dict1 = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I",
         10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R",
         19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z", 27: " "}

dict2 = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9,
         "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18,
         "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26, " ": 27}

dict3 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9,
         "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18,
         "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, " ": 27}

# This function is for writing the content of key file as a key matrix
def key(key_file, key_matrix, key_list, start):
    try:
        for j in key_file:
            for i in j:
                if i != "\n" and i != ",":
                    key_list.append(int(i))
                elif i != "," and i != "\n" and isinstance(i, int):
                    raise ValueError
    except ValueError:
        print("Invalid Character In Key File Error")
        sys.exit()
    n = len(key_list) ** (1 / 2)
    n = int(n)
    for i in range(n):
        key_matrix.append(key_list[start:start + n])
        start += n
    return key_matrix

# This function is for multiplying the key matrix with the numbers who represent letters. It can be used for reverse too.
def mul_matrix(key_matrix, matrix2, sent, result, list2, sent1):
    for i in range(len(key_matrix)):                                   # The main logic is that: For example if the matrix is 3*3
        matrix2.append([0])                                            # It takes the first three numbers from the list which holds the number of the message
    for b in range(len(sent1) // len(key_matrix)):                     # Then puts them in another list and then deletes the numbers it multiplied with.
        for x in range(len(key_matrix)):                               # This goes on until the first list is empty.
            matrix2[x][0] = sent[x]
            if x == len(key_matrix) - 1:
                del sent[0:len(key_matrix)]
                for i in range(len(key_matrix)):
                    for j in range(len(matrix2[0])):
                        for k in range(len(matrix2)):
                            result[i] += key_matrix[i][k] * matrix2[k][j]
                            if i == len(key_matrix) - 1 and j == 0 and k == len(matrix2) - 1:
                                list2.append(result)
                                result = [0] * len(key_matrix)
    list2 = [inner for outer in list2 for inner in outer]
    return list2

# This function is needed during finding the determinant of the matrix according to the adjoint rule, it reduces the matrix until it's 2*2
def part_matrix(matrix, r, c):
    matlist = []                                     # This function takes the matrix to be reduced and takes the row and column as parameter
    for x in range(len(matrix)):                     # For example in a 3*3 matrix if we were to enter 0 and 0 as row and column
        for y in range(len(matrix)):                 # The parted matrix would include the elemants of the original matrix which were not
            if x != r and y != c:                    # on the 0th row and 0th column
                matlist.append(matrix[x][y])
    newmat = []
    start4 = 0
    n4 = int(len(matlist) ** (1 / 2))
    for i in range(n4):
        newmat.append(matlist[start4:start4 + n4])
        start4 += n4
    return newmat

# We need this function when we use adjoint method while taking the inverse of a matrix
def mul_by_determinant(matrix, determinant):
    for r in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[r][j] = (1 / determinant) * matrix[r][j]
    return matrix

# The logic of this function is that it reduces the matrix until it is 2*2, and then with recursion we get to the main matrix back
def find_determinant(matrix, r, c):
    a = 0
    if len(matrix) == 2:
        a = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return a
    else:
        while c < len(matrix):
            if c % 2 == 1:
                a -= matrix[r][c] * find_determinant(part_matrix(matrix, r, c), 0, 0)
                c += 1
            else:
                a += matrix[r][c] * find_determinant(part_matrix(matrix, r, c), 0, 0)
                c += 1
        return a

# After we get a matrix with with new values, we are not done
def take_inverse(matrix, r, c):
    d = 0
    first_matrix = []
    mlist = []
    for u in range(len(matrix) ** 2):
        mlist.append(0)
    start6 = 0
    for t in range(len(matrix)):
        first_matrix.append(mlist[start6:start6 + len(matrix)])
        start6 += len(matrix)
    if len(matrix) == 1:
        inverse_matrix = 1 / (matrix[0][0])
        return inverse_matrix
    elif len(matrix) == 2:
        two_matrix = [[matrix[1][1], (-1) * matrix[0][1]], [(-1) * matrix[1][0], matrix[0][0]]]
        inverse_matrix = mul_by_determinant(two_matrix, find_determinant(matrix, 0, 0))
        return inverse_matrix
    else:
        while d < len(matrix) * len(matrix):                                      # According to the rest of the method after we find the determinants of
            if (r + c) % 2 == 1:                                                  # we need to multiply it by 4 or - according to its position
                first_matrix[r][c] = (-1) * find_determinant(part_matrix(matrix, r, c), 0, 0)
                c += 1
                if c == len(matrix):
                    c = 0
                    r += 1
                d += 1
            else:
                first_matrix[r][c] = find_determinant(part_matrix(matrix, r, c), 0, 0)  # If the sum of the row and column is even it's positive
                c += 1                                                                  # If it's odd, it's negative
                if c == len(matrix):
                    c = 0
                    r += 1
                d += 1
        inverse_matrix = mul_by_determinant(first_matrix, find_determinant(matrix, 0, 0))
        final_matrix = []
        mlist2 = []
        for z in range(len(inverse_matrix) ** 2):
            mlist2.append(0)
        start7 = 0
        for e in range(len(inverse_matrix)):                                            # After this we need to reflect the matrix by the left diagonal
            final_matrix.append(mlist2[start7:start7 + len(inverse_matrix)])
            start7 += len(inverse_matrix)
        for q in range(len(inverse_matrix)):
            for w in range(len(inverse_matrix)):
                final_matrix[q][w] = inverse_matrix[w][q]
        return final_matrix

class ParameterNumberError(Exception):
    pass

class UndefinedParameterError(Exception):
    pass

class CorruptFileError(Exception):
    pass

try:
    if len(sys.argv) != 5:
        raise ParameterNumberError
    else:
        # First we need to check if the key and input files are accessible, readable and are not empty
        try:
            path2 = sys.argv[3]
            name1, extension1 = os.path.splitext(path2)
            if extension1 != ".txt":
                raise CorruptFileError
            elif os.path.getsize(path2) == 0:
                raise TypeError
            elif os.path.exists(path2) == False:
                raise FileNotFoundError
            else:
                f = open(path2, "r")
        except CorruptFileError:
            print("The Input File Could Not Be Read Error")
            sys.exit()
        except FileNotFoundError:
            print("Input File Not Found Error")
            sys.exit()
        except TypeError:
            print("Input File Is Empty Error")
            sys.exit()

        try:
            path1 = sys.argv[2]
            name2, extension2 = os.path.splitext(path1)
            if extension2 != ".txt":
                raise CorruptFileError
            elif os.path.getsize(path1) == 0:
                raise TypeError
            elif os.path.exists(path1) == False:
                raise FileNotFoundError
            else:
                k = open(path1, "r")
        except CorruptFileError:
            print("Key File Could Not Be Read Error")
            sys.exit()
        except FileNotFoundError:
            print("Key File Not Found Error")
            sys.exit()
        except TypeError:
            print("Key File Is Empty Error")
            sys.exit()

        try:
            if sys.argv[1] == "enc":
                sentence = []
                # I turn letters into numbers and put it in the list "sentence"
                for i in f:
                    for j in i:
                        try:
                            if j not in dict2.keys() and j not in dict3.keys():
                                raise TypeError
                            else:
                                sentence.append(dict2[j])
                        except KeyError:
                            sentence.append(dict3[j])
                        except TypeError:
                            print("Invalid Character In Input File Error")
                            sys.exit()
                matrix1 = []
                list1 = []
                start1 = 0
                k_matrix = key(k, matrix1, list1, start1)
                # If the length of the sentence is not divided to the length of the matrix without remainder, we have to add spaces
                if len(sentence) % len(k_matrix) != 0:
                    for i in range(len(k_matrix) - len(sentence) % len(k_matrix)):
                        sentence.append(27)
                newm = []
                new_list = []
                result1 = [0] * len(k_matrix)
                csent = sentence.copy()
                final_list = mul_matrix(k_matrix, newm, sentence, result1, new_list, csent)
                # Finally I write the result as a string and write it in the output file
                str_list = [str(i) for i in final_list]
                d = ",".join(str_list)
                o = open(sys.argv[4], "w")
                o.writelines(d)
                o.close()

            elif sys.argv[1] == "dec":
                dec_numbers = []
                l = [i.split(",") for i in f]
                for j in l:
                    for g in j:
                        try:
                            g = int(g)
                            dec_numbers.append(g)
                        except ValueError:
                            print("Invalid Character In Input File Error")
                            sys.exit()
                f_matrix = []
                f_list = []
                start2 = 0
                k_matrix2 = key(k, f_matrix, f_list, start2)
                final_inverse_matrix = take_inverse(k_matrix2, 0, 0)
                newm2 = []
                new_list2 = []
                result2 = [0] * len(k_matrix2)
                copy_numbers = dec_numbers.copy()
                num_list = mul_matrix(final_inverse_matrix, newm2, dec_numbers, result2, new_list2, copy_numbers)
                # While calculating the inverse matrix I hadn't turn the numbers into integers so I'm doing it here
                for n in range(len(num_list)):
                    num_list[n] = int(num_list[n])
                str_list2 = []
                for f in range(len(num_list)):
                    str_list2.append(dict1[num_list[f]])
                d2 = "".join(str_list2)
                o2 = open(sys.argv[4], "w")
                o2.writelines(d2)
                o2.close()
            else:
                raise UndefinedParameterError
        except UndefinedParameterError:
            print("Undefined Parameter Error")
            sys.exit()
except ParameterNumberError:
    print("Parameter Number Error")
    sys.exit()
