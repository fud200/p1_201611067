def charCount():
    sel1=raw_input("What word?:")
    H=dict()
    word=sel1
    for c in word:
        if c not in H:
            H[c]=1
        else:
            H[c]=H[c]+1
    print H
    import matplotlib
    import matplotlib.pyplot as plt

    plt.bar(range(len(H)),H.values(),align='center')
    plt.xticks(range(len(H)),list(H.keys()))
    plt.show()

def adress():
    import matplotlib
    import matplotlib.pyplot as plt

    word = 'Hongji 2gil 20,Jongrogu,Seoul'

    H=dict()
    H['str']=0
    H['int']=0
    for i in word:
        if i.isalpha():
                H['str']=H['str']+1
        elif i.isdigit:
                H['int']=H['int']+1
    print H


    plt.bar(range(len(H)),H.values(),align='center')
    plt.xticks(range(len(H)),list(H.keys()))
    plt.show()
def home():
	import turtle
	wn=turtle.Screen()	
	me=set(['TV','phone','camera','fridger','mixer','audio','cd player','light','computer','notebook','recoder'])
	friend=set(['coffee machine','radio','camera','running machine','ramp','computer','notebook','recoder'])
	print me
	print "my machine"
	print friend
	print "friend machine"
	both= me&friend
	all= me.union(friend)
	print "allmachine"
	print all
	print "both"
	print both
	print "only me"
	print me-both
	print "only myfriend"
	print friend-both
	wn.exitonclick()
def lab8_1():
    charCount()
def lab8_2():
    adress()
def lab8_3():
    home()
def main():
    lab8_1()
    lab8_2()
    lab8_3()
if __name__=="__main__":  
     main()  
 