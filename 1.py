global a 
a = [1,3,-1,-3,-4,1,2,4,2,-1,-3,-4,-1,2,4,5,6,7,-1,-2,3]
b = [3,5,6,-1,4]
buffer = []
# out_R[0] = index , [1] = TRUE/FALSE TRUE = ">0" FALSE = "<0" [2] = COUNT 
global out_R
out_R = [0,1,0]

def my_func(out_R,my_list): #out_R - output pamar, my_list -> source list
	if out_R[1] == True:
		if my_list[out_R[0]] > 0:
			out_R[0] +=1
			return out_R
		else:
			out_R[0] += 1
			out_R[1] = 0
			out_R[2] += 1
			return out_R
	elif out_R[1] == False: 
		if my_list[out_R[0]] < 0:
			out_R[0] += 1
			return out_R
		else:
			out_R[0] += 1
			out_R[1] = 1
			out_R[2] += 1
			return out_R
	

def my_Out_Func(list1): #функция возвращяет out_R
	for i in list1:
		my_func(out_R,list1)
	return out_R

	
	
	

print(my_Out_Func(a))
#print(len(a))