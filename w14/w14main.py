def lab14():
    class Dog(object):
        def talk(self):
            print "Dog's barking sound is mung mung..."
        
    class ShihtzuDog(Dog):
        def talk(self):
            print "ShihtzuDog's barking sound is si si..."
        
    class Maltese(Dog):
        def talk(self):
            print "Maltese's barking sound is mal mal..."
    mydog1=Dog()
    mydog2=ShihtzuDog()
    mydog3=Maltese()
    mydog1.talk()
    mydog2.talk()
    mydog3.talk()
    
lab14()
sel1=raw_input()