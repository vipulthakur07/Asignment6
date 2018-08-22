#question-1 (Area of sphere)
def calculate(rad):
    return(4*3.14*rad*rad)
radius=int(input("enter radius of sphere :"))
print(calculate(radius))


#question-2 (Perfect Number)
def perfect(num):
    sum=0
    for a in range(1,num):
        if num%a==0:
            sum=sum+a
    if sum==num:
        print(num)
for i in range(1,1000):
    perfect(i)
    

#question-3 (Multiplication table)
def table(num):
    for i in range(0,21):
        print(num,"*",i,"=",num*i)
num=int(input("enter a number you need multiplication table for :"))
table(num)

#question-4 (Power of number)
def cal(num,pow):
    if pow!= 0:
        return (num*cal(num, pow-1))
    else:
        return 1
num=int(input("enter a number :"))
pow=int(input("enter the power :"))
print(cal(num,pow))
