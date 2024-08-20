def change_case(string,style):
	result=''
	
	#convert from uppercase to lowercase
	if style=="c":
		for char in string:
			if 'a'<=char<='z':
				result+=chr(ord(char)-ord('a')+ord('A'))
			else:
				result+=char
	
	#covert from lowercase to uppercase
	elif style=="s":
		for char in string:
			if 'A'<=char<='Z':
				result+=chr(ord(char)-ord('A')+ord('a'))
			else:
				result+=char
	
	#Reverse the case
	elif style == "r":  
        	for char in string:
            		if 'a' <= char <= 'z':  # Convert lowercase to uppercase
                		result += chr(ord(char) - ord('a') + ord('A'))
            		elif 'A' <= char <= 'Z':  # Convert uppercase to lowercase
                		result += chr(ord(char) - ord('A') + ord('a'))
            		else:
                		result += char
	
	#Alternatingcase
	elif style == "u":  
        	first_char = string[0]
        	uppercase = 'A' <= first_char <= 'Z'  

        	for i, char in enumerate(string):
            		if 'a' <= char <= 'z' or 'A' <= char <= 'Z':  
                		if i % 2 == 0:  
                    			if uppercase:
                        			result += char.lower() if 'A' <= char <= 'Z' else char
                    			else:
                        			result += char.upper() if 'a' <= char <= 'z' else char
                		else:  
                    			if uppercase:
                        			result += char.upper() if 'a' <= char <= 'z' else char
                    			else:
                        			result += char.lower() if 'A' <= char <= 'Z' else char
            		else:
                		result += char
	
	else:
		return string
	
	return result	
input_string="Python Programming"	
print(change_case(input_string,"c"))
print(change_case(input_string,"s"))
print(change_case(input_string,"r"))
print(change_case(input_string,"u"))
