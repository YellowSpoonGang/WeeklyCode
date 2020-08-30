def compress(string):
    
    blank = ""
    count = 1
    
    blank += string[0]
    
    for i in range(len(string) - 1):
        if (string[i] == string[i+1]):
            count += 1
        else:
            if count > 1:
                blank += str(count)
            blank += string[i + 1]
            count = 1
        
    if count > 1:
        blank += str(count)
    return blank

if __name__ == "__main__":
    string = "aaaaabb"
    print (compress(string))
    
# blank = 
