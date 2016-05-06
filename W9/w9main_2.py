import math
h=tuple()
h=[(74425,76326),(61164,61636),(109688,115744),(144796,146776),(174996,181676),(177841,177434),(204630,205980),(223373,232245),(161055,166130),(171576,176735),(279169,293772),(239450,251066),(148690,156510),(182977,196992),(237792,242641),(283869,296762),(209344,210282),(118965,114441),(186503,186856),(195734,203014),(254381,249472),(212401,229111),(271654,295354),(319197,335045),(229829,231671)]
len(h)
a=0
b=0
c=0
sum=list()
for i in h:
    a=a+i[0]
    b=b+i[1]
    c=i[0]+i[1]
    sum.append(c)
print a
male= a/len(h)
print "male average in seoul is %s"%male
print b
female=b/len(h)
print "female average in seoul is %s"%female
import matplotlib
import matplotlib.pyplot as plt
print sum
plt.bar(range(len(sum)),sum,align='center')
plt.show()