x = 'dillip'
print(x.capitalize)
y = x.capitalize
print(y)
print(x.lower)
print(x.upper)
x = 1
y = 2.5
z = x+y
s = ('hello,world')
print(s)


dryfriut = 91.00
wovenbag = 2.00
tea =24.50
perfum =186.20
total = dryfriut + wovenbag + tea + perfum
print(total)


item=("mixdry","non-wovenbag","tea","perfum")
Qty=(1,1,1,1)
Price=(91.00,2.00,24.50,186.20)
myfile=open("recipt.txt","wt")
myfile.write("__________________\n")
# myfile.write("ITEM\t\tqty\tprice\n")
myfile.write("___________________\n")
for i in range(0,len(item)):
  myfile.write(item[i]+"\t\t")
  myfile.write(str(Qty[i])+"\t\t")
  # myfile.write(str(price[i])+"\n")
  # myfile.write("_____________\n")

total = 0

for j in range(0,len(item)):
  temp=Qty[j]*Price[j]
  total=total+temp
  myfile.write("\t\t\tTOTAL\t"+str(total)+"\n")
  myfile.write("_____________\n")


# string billl

bill_id = input("Please enter Bill id > ") 
customer_id = input("Please enter Customer id > ") 
bill_amount = input("Please enter bill Amount > ") 
customer_name = input("Please enter Customer Name > ") 

if ((len(customer_name) >= 3) and (len(customer_name) <= 20)) is True: 
    print("Bill Id: ",bill_id) 
    print("Customer Id: ",customer_id) 
    print("Bill Amount:Rs. ",bill_amount) 
    print("Customer Name: ",customer_name) 
else: 
    print("Invalid customer name. Customer name must be between 3 and 20 characters");


print("ADITYA BIRLA".center(30))
print("SHOPING MALL".center(30,'*'))
print("DATE 11 FEB 2019".center(40))
print("_"*30)
a,b,c,d =1,1,1,1
x,y,z,p = 91,2,24.50,186.20
print("  1  " + " Mix-dry fruit               " + " {}   {}".format(str(a),a*x))
print("  2  " +  " Non Woven Bag              " + " {}   {}".format(str(b),b*y))
print("  3  " + " Plax Mouthfresh             " + " {}   {}".format(str(c),c*z))
print("  4  " + " Axe Signature Men Body Perfum" + " {}  {}".format(str(d),d*p))
print("_"*30)
n= (a*x) +(b*y) + (c*z)
GST= n*0.03
total =n + GST
print("sub total".center(23),n)
print("GST@ 3%".center(23),GST)
print("-"*30)
print("TOTAL".center(23),n)
