def get_ss_sl(num):
	max_no, min_no = -2147483648, 2147483647
	sl_max, ss_max = -1, -1
	l=0
	def ss_sl(nums):
		l=[]
		for i in nums:
			if isinstance(i, int):
				l.append(i)
			elif isinstance(i,(set,list,tuple)):
				l += ss_sl(i)
			elif isinstance(i,dict):
				l += ss_sl(i.items())
		return l
	l = ss_sl(num)
	for i in l :
		if i > max_no :
			
			sl_max = max_no
			max_no = i

		if i > sl_max and i != max_no:
			sl_max = i
		if i < min_no :
			ss_max = min_no
			min_no = i
		elif i < ss_max and i > min_no:
			ss_max = i
	return sl_max, ss_max
	
	

	
	
	
print(get_ss_sl([12,23,35,43,'sggs',46,{'34':986,54:2143,13:34324243},(345,7564,'sggshiiy',21567,86)]))	
	
	
	
	
#print(get_ss_sl([16,8,456,64684,4684,646545,8496,1684,31,64843,165484,1644,431,6465,3164,4316316,4843131,6546,4134,6464,6431,15,5,3]))
