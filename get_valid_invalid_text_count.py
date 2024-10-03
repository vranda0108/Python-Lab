s={'{','(','[','<','>',']',')','}'}
pairs={'{':'}','<':'>','[':']','(':')'}	

def validate_string(text):
	
	stack=[]
	for char in text:
		if char in pairs:
			stack.append(char)
		elif char in pairs.values():
			if not stack:
				return False
			top=stack.pop()
			if pairs[top]!=char:
				return False
		elif char not in s:
				return False
	return not stack

def get_valid_invalid_text_count(texts):
	valid_count=0
	invalid_count=0
	
	for item in texts:
		if isinstance(item,str):
			if validate_string(item):
				valid_count+=1
			else:
				invalid_count+=1
		
	return (valid_count,invalid_count)
	
print(get_valid_invalid_text_count(['[{(', [45], "()", "{<>}", "invalid", "(<>)", "([<>])", 123]))


