1.4:
import sys

def palinPerm():

    string = sys.argv[1]
    dict = create_Freq_Map(string)

    length = len(string)
    odds = 0

    if dict.__contains__(' '):
        length = length - dict.get(' ')


        print( length)
    if length%2 ==0:
        for char in dict:
            if char != ' ':
                if int(dict.get(char))%2 != 0:
                    return False
    else:
            for char in dict:
                if char != ' ':
                    if odds > 1:
                        return False
                    if int(dict.get(char))%2 != 0:
                        odds = odds +1

    if odds>1:
        return False
    else:
        return True

def create_Freq_Map(string):
    dict = {}
    for i in range(len(string)):
        if dict.__contains__(string[i]):
            previousVal = dict.get(string[i])
            dict.update( {str(string[i]) : (previousVal+1) })
        else:
            dict.update( {str(string[i]) : 1 })
    return dict


if __name__== "__main__":
    result = palinPerm()
    print(result)  


1.5:
import sys


def OneAway():
    string1 = sys.argv[1]
    string2 = sys.argv[2]

    edits = 0
    if len(string2) < len(string1)-1 or len(string2)>len(string1)+1:
        print("At least 2 edits")
        return False

    x = 0
    y = 0
    while x < len(string1) and y< len(string2):
        if edits >= 2:
            return False

        if  string1[x] != string2[y]:
                edits = edits + 1
                if len(string1)>len(string2):
                    x=x+1
                elif len(string1)<len(string2):
                    y=y+1
                else:
                    x=x+1
                    y=y+1
        else:
            x = x + 1
            y = y + 1
    if x<len(string1) or y <len(string2):
        edits= edits+1
    print(edits)
    if edits >1:
        return False
    else:
        return True



if __name__== "__main__":
    result = OneAway()
    print(result)

1.7:


import sys
import math

def rotateMatrix():
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    N = len(matrix)
    print(matrix)
    for i in range(0,int(N/2)):
        # print(matrix)
        for j in range(i,N-i-1):
            temp = matrix[i][j]

            # print(str(i)+","+str(j))
            # print(N-i)

            matrix[i][j] = matrix[j][N-1-i]
            # print(matrix)
            matrix[j][(N-1)-i] = matrix[(N-1)-i][(N-1)-j]
            # print(matrix)
            matrix[N - 1 - i][(N - 1) - j] = matrix[(N-1)-j][i]
            # print(matrix)

            matrix[(N-1)-j][i] = temp
    print(matrix)


if __name__ == "__main__":
    result = rotateMatrix()
    print(result)







