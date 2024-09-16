decimal_dict={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def decimal_subtraction(num1,num2):

	def string_to_integer(text):
		result=0
		text_length=len(text)
		if text_length==0:
			return 0
		elif text_length==1:
			return decimal_dict[text]
		else:
			return decimal_dict[text[0]]*pow(10,text_length-1)+string_to_integer(text[1:])
	
	def borrow_subtract(num1,num2):
		if len(num1) < len(num2):
			num1, num2= num2, num1
		num2=num2.zfill(len(num1))
		result=[]
		borrow=0
		
		for i in range(len(num1)-1,-1,-1):
			digit1=decimal_dict[num1[i]]-borrow
			digit2=decimal_dict[num2[i]]
			
			if digit1 < digit2:
				borrow = 1
				digit1 +=10
			else:
				borrow=0
			
			result_digit=digit1-digit2
			result.append(str(result_digit))
			
		result=result[::-1]
		return ''.join(result).lstrip('0') or '0'
		
	int_num1 = string_to_integer(num1)
	int_num2 = string_to_integer(num2)
			
	if int_num1 > int_num2:
		result=borrow_subtract(num1,num2)
	elif int_num1 < int_num2:
		result = '-' + borrow_subtract(num2, num1)
	else:
		result='0'
		
	return result
	
print(decimal_subtraction("12", "7")) 
print(decimal_subtraction("12", "10"))  
#print(decimal_subtraction("12", "000"))
print(decimal_subtraction("12", "15"))  
print(decimal_subtraction("12", "12"))
