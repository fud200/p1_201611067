h=list() 
def sumList(h): 
    	for i in range(0,1001): 
		if(i%4==0 and i%5>0): 
			h.append(i) 
	sum=0 
	for j in range(0,len(h)): 
		sum=sum+h[j] 
	return sum	 
def main(): 
	print sumList(h) 
main() 

input("enter to end")
if __name__=="__main__": 
	main() 
