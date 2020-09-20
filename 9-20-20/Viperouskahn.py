import sys
import math

def zeroMatrix():
    matrix = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,0]]
    N = len(matrix)
    print(matrix)
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                for k in range(N):
                    matrix[i][k] = 0
                for l in range(N) :
                    matrix[l][j] = 0

    print(matrix)

def removeDup(list):

    head = list.head
    current = list.head
    value =  current.value
    while head!=list.tail:
        next= current.next
        if value == next.value:
            current.next = next.next
            next.next = None
        head = head.next
        value = head.value
        current= head

