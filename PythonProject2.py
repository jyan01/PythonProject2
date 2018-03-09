Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello")

 

print("Hello World")

 

print("Hello\nWorld")

 

print("'Hello'")

 

print('"Hello World"')

 

print('"!@#$%^&*()"')

 

print('"C:\Download\hello.cpp"')

 

a = input()

a = int(a)

print(a)

 

a = input()

print(a)

 

a = input()

a = float(a)

print("%f" % a)

 

a, b = input().split()

a = int(a)

b = int(b)

print(a, b)

 

a, b = input().split()

print(b, a)

 

a = input()

a = float(a)

print("%.2f" % a)

 

a = input()

a = int(a)

print(a, a, a)

 

a, b = input().split(':')

a = int(a)

b = int(b)

print(a, b, sep = ':')

 

a, b, c= input().split('.')

a = int(a)

b = int(b)

c = int(c)

print("%04d" % a, "%02d" % b, "%02d" % c, sep = '.')

 

a, b = input().split('-')

a = int(a)

b = int(b)

print("%06d" % a , b, sep = '')

 

a = input()

print(a)

 

a = input()

print(a)

 

a, b = input().split('.')

a = int(a)

b = int(b)

print(a)

print(b, sep = '')

 

a = input()

a = int(a)

print("[", a//10000, "0000]", sep = "")

a = a % 10000

print("[", a//1000, "000]", sep = "")

a = a % 1000

print("[", a//100, "00]", sep = "")

a = a % 100

print("[", a//10, "0]", sep = "")

a = a % 10

print("[", a, "]", sep = "")

 

a, b, c = input().split(':')

a = int(a)

b = int(b)

c = int(c)

print(b)

 

a, b, c = input().split('.')

a = int(a)

b = int(b)

c = int(c)

print("%02d" % c, "%02d" % b, "%04d" % a, sep = '-')

 

a = input()

a = int(a)

print(a)

 

a = input()

a = float(a)

print("%.11f" % a)

 

a = input()

a = int(a)

print(a)

 

a, b = input().split()

a = int(a)

b = int(b)

print(a + b)

 

a, b = input().split()

a = int(a)

b = int(b)

print(a + b)

 

a = input()

a = int(a)

print(-a)

 

a, b = input().split()

a = int(a)

b = int(b)

print(int(a / b))

 

a, b = input().split()

a = int(a)

b = int(b)

print(a % b)

 

a = input()

a = int(a)

print(a + 1)

 

a, b = input().split()

a = int(a)

b = int(b)

print(a + b)

print(a - b)

print(a * b)

print("%d" % (a / b))

print(a % b)

print("%.2f" % (a / b))

 

a, b, c = input().split()

a = int(a)

b = int(b)

c = int(c)

print(a + b + c)

print("%.1f" % ((a + b + c) / 3))

 

a , b = input().split()

a = int(a)

b = int(b)

if a>b:

	print(1)

else: 

	print(0)
