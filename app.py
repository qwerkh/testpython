#Test with github
#Test collaborator
# str="Hello world!"
# print(str)
# print(str[0])
# print("Welcom"[0])
# print(str[2:5])
# print(str[2:])
# print(str*3)
# print(str+" Test")

#=====number
# a=10
# b=2.5
# c=a/b
# print(c)
# print(type(a))
# print(type(b))
# print(type(c))

#==Type
# a="500"
# print(len(a))
# print(type(a))
# print(40+int(a))

#Boolean
#True,False
# a=False
# print(type(a))
# print(int(a))
# b=-0.2
# print(bool(b))
# c=10
# d=20
# print(bool(a==b))
# e=None
# print(bool(e))
# f=()
# print(bool(f))
# g="Dara"
# print(bool(g))

#===Practice
# value=input("Input two digit number =")
# total=int(value[0])+int(value[1])
# print("Result ="+ str(total))


# a=7
# a|=20
# # a=a&0 , a=7 | 0
# print(a)

# a=[1,2,3,4,5]
# b=[1,2,3,4,5]
# c=a
# c=b
# print(a is c)
# print(a is b)

# w=float(input("Input Weight ="))
# h=float(input("Input your height="))
# bmi=w//h**2
# welcome="Welcome to Your Result"
# # print("{} Your BMI ={}".format(welcome,bmi))
# print(f'{welcome} Your BMI= {bmi}')

print("===Welcome to the tip Calculator===")
bill = float(input("What was the total bill ?"))
tip = float(input("How much tip would you like to give? 10, 12, 15"))
people = int(input("How many people to split the bill?"))
total = (bill+((tip/100)*bill))/people
print(f'Each Person should pay : {total}')







