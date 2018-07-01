#question1
#divide by zero
a=3
try:
    if(a<4):
        a=a/(a-3)
        print(a)
except Exception as e:
    print("error occured ")
    print(e)

#question2
#list index out of range
l=[1,2,3]
try:
    print(l[3])
except Exception as err:
    print("error occured")
    print(err)
#question3
# hi there
# An exception

#question 4
# -5
# a/b result in 0

#question5
#import error
try:
    import prac
except ImportError as err:
    print("no such module")
    print(err)

#value error
try:
    num=int(input("enter a number"))
    print(num)
except ValueError as e:
    print("enter a number ")
    print(e)
    

#index error
l=[1,2,3]
try:
    print(l[4])
except IndexError as e:
    print("out of index range",e)
    
#question6
class Age_too_small(Exception):
        def __init__(self,age):
                self.age=age
        def display(self):
                print("age is %d"%(self.age))

while True:
        try:
                num=int(input("enter your age:-"))
                if(num<18):
                        raise Age_too_small(num)
                else:
                        print("valid age")
                        break
        except Age_too_small :
                print("not appropriate age enter again")

                
print("congratulations your age is greater than 18")
                
