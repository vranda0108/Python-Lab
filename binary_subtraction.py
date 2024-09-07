def binary_subtraction(num1,num2):
	
	if all(char in '01' for char in num1) and all(char in '01' for char in num2):
        	# Make both binary strings of equal length by padding the shorter one with leading zeros
		max_len = max(len(num1),len(num2))
		num1 = num1.zfill(max_len)
		num2 = num2.zfill(max_len)
		
		result = []
		borrow = 0
		
		for i in range(max_len-1,-1,-1):
			bit1 = int(num1[i])
			bit2 = int(num2[i])
			
			if borrow:
				if bit1 == 1:
					bit1 = 0
					borrow = 0
				else:
					bit1 = 1
					borrow = 1
					
			if bit1 >= bit2:
				result.append(str(bit1 - bit2))
			else:
				result.append(str(bit1+2-bit2))
				borrow = 1
				
		result = ''.join(result[::-1]).lstrip('0')

		print(f"\n{num1}\n{num2}\n"+'-'*max_len)
		return result.zfill(max_len) if result else 0

	else:
        	return "\nError: Input contains digits other than 0 and 1."

print(binary_subtraction("1101","1001"))
print(binary_subtraction("1101","1011"))
print(binary_subtraction("1101","1001"))
print(binary_subtraction("1101","1201"))
