def count(string,sub_string,flag):

	if flag=="False":
		#non_overlapping=string.count(sub_string)
		non_overlapping=len(sub_string)
		return non_overlapping
	else:
		count=0
		start=0
		while "False":
			start=string.find(sub_string,start)
			if start==-1:
				break
			count+=1
			start+=1
		return count
		
print(count("sgggsggsssgs","gg","False"))
print(count("sgggsggsssgs","gg","True"))
print(count("sgggsggggsssgs","gg","True"))
