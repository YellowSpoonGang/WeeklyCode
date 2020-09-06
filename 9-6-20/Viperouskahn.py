1.1 
 def main():
    original_String = sys.argv[1]
    return uniqueChecker(original_String)

def uniqueChecker(string1):
    for i in range(len(string1)-1):
        for j  in range (i+1, len(string1)):
            if string1[i] == string1[j]:
                return False
    return True 
   
1.2
  def main():
    first_String = sys.argv[1]
    second_String = sys.argv[2]
    return permutationChecker(first_String,second_String)

def permutationChecker(String1,String2):
    first_Dict = {}
    second_Dict = {}
    if len(String1) != len(String2):
        return False

    first_Dict = create_Freq_Map(String1)
    second_Dict = create_Freq_Map(String2)
    print(first_Dict)
    print(second_Dict)

    for key in first_Dict:
        if second_Dict.__contains__(key) == False:
            return False
        else:
            firstVal = first_Dict[key]
            secondVal = second_Dict[key]
            if firstVal != secondVal:
                return False
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
    
 1.3
 def main():
    original_String = sys.argv[1]
    return URLifyChecker(original_String)

def URLifyChecker(string):
    string = string.replace(" ", "%20")
    return string 
