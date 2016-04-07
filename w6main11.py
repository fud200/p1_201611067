def sayHello(): 
    print "I say hello!" 
 
def lab6_1(): 
	year=raw_input("input year: ")
	y1=int(year)
	if(y1%4==0) and (y1%100!=0 or y1%400==0): 
		print "This year is leap year"
	else:
		print "This year is not leap year"

def lab6_2(): 
	import random 
	guessesTaken = 0 
	print ('Welcome! What is your name?') 
	myname = raw_input() 
	number = random.randint(1,300) 
	print ('Well,'+myname+',I am thinking of a number between 1 and 300.') 
	while guessesTaken < 100: 
	    print('Take a guess.') 
	    guess = input() 
	    guess = int(guess) 
	    guessesTaken =  guessesTaken + 1 
	    if guess < number: 
	        print('Too low.')  
	    if guess > number: 
	        print('Too high.') 
	    if guess==number: 
	        print("Collect.") 
	        break 
	if guess == number: 
	    guessesTaken = str(guessesTaken) 
	    print('Good job,'+myName+'! You guessed my number in' +guesses-Taken +'guesses!')  
 
	if guess !=number: 
	    number = str(number) 
	    print('Nope. The number I was thinking of was '+number) 


def main():  
	lab6_1() 
	lab6_2() 

 
main() 
raw_input() 
if __name__=="__main__": 
	main() 
wn.exitonclick()