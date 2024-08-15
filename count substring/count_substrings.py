def count_substrings(string, sub_string, flag):
    count = 0
    start = 0
    
    while True:
        start=string.find(sub_string, start)
        if start == -1:
            break
        count += 1
        if flag:
            start += 1 
        else:
            #start += string.count(sub_string) 
            start += len(sub_string)
    return count

print(count_substrings("sgggsggsssgs", "gg", False))  
print(count_substrings("sgggsggsssgs", "gg", True))   
print(count_substrings("sgggsggggsssgs", "gg", True)) 

