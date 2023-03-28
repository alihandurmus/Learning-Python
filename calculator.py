
def calculator(number1,number2,mark):
	if mark == "+":
		print(number1+" + "+number2+" = "+str((int(number1)+int(number2))))
	elif mark == "-":
		print(number1+" - "+number2+" = "+str((int(number1)-int(number2))))
	elif mark == "*":
		print(number1+" * "+number2+" = "+str((int(number1)*int(number2))))
	elif mark == "/":
		print(number1+" / "+number2+" = "+str((int(number1)/int(number2))))
	else:
		print("Please only type one of these characters ""+ , - , * , /"" ")
while True:
	number1 = input("Please type the first number: ")
	number2 = input("Please type the second number: ")
	mark = input("Choose between + , - , * , / : ")
	calculator(number1,number2,mark)			