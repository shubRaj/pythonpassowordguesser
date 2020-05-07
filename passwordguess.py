from itertools import product
import string
def guess_pass(password):
    chars = string.ascii_letters+string.digits+string.punctuation
    attempts = 0
    for password_length in range(1,9):
        for guess in product(chars,repeat=password_length):
            attempts +=1
            guess = "".join(guess)
            if guess == password:
                return f"Your password is {guess}.Found in {attempts} attempts."
            print(guess)
print(guess_pass(input("please enter your password: ")))