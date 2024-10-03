import time

def get_even_odd_count_1(l):
	even_count,odd_count=0,0	
	for i in l:
		if i%2==0:
			even_count+=1
		else:
			odd_count+=1			
	return even_count,odd_count
	
def get_even_odd_count_2(l):
	even_count,odd_count=0,0	
	for i in l:
		if i%2:
			odd_count+=1
		else:
			even_count+=1			
	return even_count,odd_count
	
def get_even_odd_count_3(l):
	even_count,odd_count=0,0	
	for i in l:
		t=i%2
		odd_count+=t
		even_count+=1-t
	return even_count,odd_count
	
def get_even_odd_count_4(l):
	even_count,odd_count=0,0
	for i in l:
		t=bin(i)[-1]
		if t=='0':
			even_count+=1
		else:
			odd_count+=1
	return even_count,odd_count
	
def check(functions, l):
	time_taken = []
	for func in functions:
		s_time = time.time()
		func(l)  
		e_time = time.time()
		time_taken.append(e_time - s_time)
	return time_taken
	
def calculate_percent(time_taken):
	base_time = time_taken[0]
	for i, time_ in enumerate(time_taken[1:], start=2):
		percent_diff = ((base_time - time_) / base_time) * 100
		if percent_diff > 0:
			print(f"approach{i} is {abs(percent_diff):.2f}% faster than approach1")
		else:
			print(f"approach{i} is {abs(percent_diff):.2f}% slower than approach1")

l=[1,2,3,4,5,6,7,8,9]
	
print(get_even_odd_count_1(l))
print(get_even_odd_count_2(l))
print(get_even_odd_count_3(l))
print(get_even_odd_count_4(l))

time_taken=check([get_even_odd_count_1,get_even_odd_count_2,get_even_odd_count_3,get_even_odd_count_4],l)
print(time_taken)
print(calculate_percent(time_taken))
