import turtle
wn=turtle.Screen()
def milk():
	alldata= [
	    ["Coffee","Water","Milk","Icecream"],
	    ["Espresso","No","No","No"],
	    ["Long Black","Yes","No","No"],
	    ["Flat White","No","Yes","No"],
	    ["Cappuccino","No","Yes","No"],
	    ["Affogatto","No","No","Yes"]
	]
	data= alldata[1:]
	sum=0
	for i in data:
	    if i[2].upper()=='YES':
	        sum=sum+1
	print "percent:",(float(sum)/float(len(data)))*100,"%"

def everage():
	score=[
	    ["English",100,"Math",200],
	    ["English",200,"Math",200],
	    ["English",100,"Math",300],
	]
	x=0
	for i in score:
	    x=i[1]+x
	print "English_everage:",float(x)/float(len(score))
	y=0
	for i in score:
	    y=i[3]+y
	print "Math_everage:",float(y)/float(len(score))

def letitbe():
    lyrics=["When I find myself in times of trouble"
	    "Mother Mary comes to me "
	    "Speaking words of wisdom, let it be"
	    "And in my hour of darkness "
	    "She is standing right in front of me "
	    "Speaking words of wisdom, let it be "
	    "Let it be, let it be, let it be, let it be "
	    "Whisper words of wisdom, let it be "
	    "And when the broken hearted people "
	    "Living in the world agree "
	    "There will be an answer, let it be "
	    "For though they may be parted "
	    "there is still a chance that they will see "
	    "There will be an answer, let it be "
	    "Let it be, let it be, let it be ,let it be "
	    "There will be an answer let it be "
	    "Let it be, let it be, let it be, let it be "
	    "Whisper words of wisdom, let it be "
	    "Let it be, let it be, let it be, let it be "
	    "Whisper words of wisdom, let it be"
	    "And when the night is cloudy "
	    "There is still a light that shines on me "
	    "Shine until tomorrow, let it be "
	    "I wake up to the sound of music "
	    "Mother Mary comes to me "
	    "Speaking words of wisdom, let it be"
	    "Let it be, let it be, let it be, let it be"
	    "There will be an answer let it be"
	    "Let it be, let it be, let it be, let it be "
	    "Whisper words of wisdom let it be"
	        ]

    d=dict()
    for h in lyrics[0].split():
        if h not in d:
                d[h]=1
        else:
                d[h]=d[h]+1
    print d
    for h in d:
            if(d[h]>=20):
                print "word", h,"num", d[h]
def lab10():
    milk()
    everage()
    letitbe()
def main():
    lab10()
if __name__=="__main__": 
     main() 
wn.exitonclick()