s={'{','(','[','<','>',']',')','}'}
pairs={'{':'}','<':'>','[':']','(':')'}	

def validate_string(text):
	
	stack=[]
	for char in text:
		if char in pairs:
			stack.append(char)
		elif char in pairs.values():
			if not stack:
				return "Invalid:Extra closing bracket."
			top=stack.pop()
			if pairs[top]!=char:
				return "Invalid:MIsmatched brackets."
		elif char not in s:
			return "Invalid:Illegal symbol."
	if stack:
		return "Inavlid:Extra opening bracket."
	return "Valid"	
		

print(validate_string("sggs"))
print(validate_string("{sggs}"))
print(validate_string("<>"))
print(validate_string("{<}>"))
print(validate_string("[<>]"))

print(validate_string(""))
print(validate_string("}(}"))
print(validate_string("<<<>>>"))

print(validate_string("{<}"))
print(validate_string("{}<"))
print(validate_string("sggs"))
