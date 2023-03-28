name = input("Name :")
print(f"Hello {name} time to play hangman")
can = 10
secret_word = "metallica"
guess_word = ""


while can>0:
	character_left = 0
	for element in secret_word:
		if element in guess_word:
			print(element)
		else:
			character_left += 1
			print("-")
	if character_left == 0:
		print("You Won!!")
		exit();

      
			
	guess = input("Guess a word:")
	guess_word += guess		
	if guess not in secret_word:
		can = can-1
		print("Wrong!!")
		print(f"You have {can} left")
print("You Die!!")
	
		
		