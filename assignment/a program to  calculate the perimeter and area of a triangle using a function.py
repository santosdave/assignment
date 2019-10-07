a = int(input("Enter Length Of One Side \n : "))
b = int(input("Enter Length Of Other Side \n : "))
c = int(input("Enter length of the other side \n : "))
s = (a+b+c)/2
def perimeter():
    per = (a + b + c)
    print("perimeter is : " + str(per))
def area():
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print("area is : " + str(area))
    

def Main():
    perimeter()
    area()
Main()