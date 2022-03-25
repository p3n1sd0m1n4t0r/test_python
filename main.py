def hello():
    print("Yo! Nigga!")
hello()

messege = "Stop!"
print (messege)

age = int(input("How old are you?"))
if (age>=25):
    print ("Welcome in da club!")
elif (age >= 18) and (age < 25):
    print ("Where's your mama?")
else:
    hello()
    print ("Your peepee is too small!")

print ("Ok, nigga. I'll let you in if you're good at math.")
print ("How much is...")

x = int(input("Enter your first number"))
print ("Pluuus...")
y = int(input("Enter your second number"))

print ("My answer is...")

def sum(a,b):
    return a+b
print(sum(x,y))

print ("Hah, but how good are you with functions?")
print ("For example f(x)=2*a-2?")

def f(a=6):
    return 2*a-2
print(f(13))

print ("'Global' example.")

a=45
b=5
def f():
    global a
    a=a+2
    print(a)
f()
print(a)

i=1
while i<=10:
    if i !=5:
        print(i)
    i=i+1
    continue

