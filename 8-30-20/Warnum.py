string = "aabcccccaaa"
num =0

def compression(string):
  global num
  comp = ""
  length = len(string)
  
  while(num != length):
    count = 1
    
    while((num < (length-1)) and (string[num] == string[num+1])):
      count = count + 1
      num = num + 1
     
    if (count == 1):
      comp = comp + str(string[num])
    else:
      comp = comp + str(string[num]) + str(count)
      
    num = num + 1
    
  return comp
  
print(compression)
