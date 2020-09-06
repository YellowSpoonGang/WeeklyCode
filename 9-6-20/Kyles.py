# 1.1

def unique(string):
    
    sorted(string)
    
    for i in range (len(string) - 1):
        
        if string[i] == string[i + 1]:
            return False
    return True

if __name__ == "__main__":
    
    string = "abcd"
    
    if(unique(string)):
        print("Yes")
    else:
        print("No")

#1.2

def perm(string, string2):
    
    
    
    a = sorted(string)
    string = "".join(a)
    b = sorted(string2)
    string2 = "".join(b)
    
    for i in range (0, len((string))):
        
        if string[i] != string2[i]:
            return False
    return True

if __name__ == "__main__":
    
    string = "Yellow"
    string2 = "Spoon"
    
    if (perm(string, string2)):
        print("Yes")
    else:
        print("No")

    

#1.3

sep_string = "%20"
string = "Mr    John    Smith   "
a_string = string.split()
print(sep_string.join(a_string))
