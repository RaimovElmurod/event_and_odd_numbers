#A four-digit integer is given. Find the sum of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
n = 5637

n1 = n%10
n = n//10

n2 =n%10
n = n//10

n3 = n%10
n = n//10

n4 = n%10
x = ( n1%2*n1 +  n2%2 * n2 +  n3%2* n3 +  n4%2 * n4)
#Create a variable "sum_even" and assign it 0.
print(x)
#Find the sum of the even digits in the variable "var_int".
