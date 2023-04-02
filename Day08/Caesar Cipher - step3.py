# step 3
# ----------------------------------------------

alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

if (direction == 'encode') or (direction == 'decode'):
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))

	#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
	def caesar(start_text, shift_amount, cipher_direction):
		end_text = ""
		
		if cipher_direction == 'decode':
			shift_amount *= -1		# dhyaan se	
			
		for eachletter in start_text:
			index = alphabet.index(eachletter)
			# if cipher_direction == 'decode':
			# 	shift_amount *= -1		# yaha nahi rakh sakte		
			index_after_shift = index + shift_amount 
			end_text += alphabet[index_after_shift]
		print(f"The {cipher_direction}d text is {end_text}")

		
	#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
	caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
	
else:
	print("Wrong command.")