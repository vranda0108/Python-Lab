def modulo(num,deno):
	if deno==0:
		return "Division by zero not possible!"
	else:
		if num>0 and deno>0:
			while(num>=deno):
				num=num-deno
			return num
		elif num<0 and deno>0:
			while(-num>=deno):
				num=num+deno
			return -num
		elif num>0 and deno<0:
			while(num>=-deno):
				num=num+deno
			return num
		elif num<0 and deno<0 :
			while(-num>=-deno):
				num=num-deno
			return -num
		else :
			return 0
print(modulo(15,4))
print(modulo(15.5,4))
print(modulo(15,4.5))
print(modulo(-12,5))
print(modulo(-12.5,5))
print(modulo(-12,5.5))
print(modulo(12,-7))
print(modulo(12.5,-7))
print(modulo(12,-7.5))
print(modulo(-15,-6))
print(modulo(-15.5,-6))
print(modulo(-15,-6.5))
print(modulo(0,3))
print(modulo(3,0))
print(modulo(0,0))
