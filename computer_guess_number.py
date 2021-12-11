import random 

low = int(input("Enter the lower number in the range: "))
high = int(input("Enter the higher number in the range: "))
user_reply = ''

while user_reply != 'c':
    if low != high:
        computer_guess = random.randint(low, high)
        
    else:
        computer_guess = low #can be high too as low = high
    user_reply = input(f"Is {computer_guess} right guess by the  computer? reply 'h' for high, 'l' for low,'c' for a correct guess: ")
    if user_reply == 'h':
        high = computer_guess - 1
    elif user_reply =='l':
        low = computer_guess + 1
print(f"Yaay! {computer_guess} is the correct number I though of!!")
         