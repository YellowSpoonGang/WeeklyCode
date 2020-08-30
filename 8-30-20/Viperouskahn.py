import sys

def main():
    changes = 0
    if len(sys.argv) != 2:
        print("Usage : ./StringCompress <first string>")

    original_String = sys.argv[1]

    finalString = ""

    previousChar=original_String[0]

    increment = 0

    for i in range(len(original_String)):
        if original_String[i] == previousChar:
            increment+=1

        else:
            finalString= finalString+str(previousChar+str(increment))
            previousChar = original_String[i]
            increment = 1

    finalString = finalString + str(previousChar + str(increment))

    if len(finalString) >len(original_String):
        finalString=original_String

    print(finalString)


if __name__== "__main__":
    result = main()
