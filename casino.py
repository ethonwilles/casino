import random
slots = [1,2,3,4,5,6,7]


def initial_welcome(money):
    try: 
        if type(int(money)) == int:
            print('Welcome to the Casino!')
            print(' We will begin to play slots!')
            print("""
            Rules:
                * It costs $3.00 to play.
                * If your wallet hits zero, the game ends.
            """)
            
            game(money,input('Enter Yes to play, Enter No to quit.: '))
    except:
        initial_welcome(input('Invalid Response. Needs to be an integer. Try Again: '))

def game(money,choice):
    if (choice.lower()) == 'yes':
        player_wallet = int(money)
        print(f'You are starting out with ${player_wallet}.00')
        player_wallet -= 3
        slot_nums = []
        for i in range(0,3):
            rannum = random.randint(1,len(slots))
            slot_nums.append(rannum)
        if slot_nums[0] == slot_nums[1] and slot_nums[1] == slot_nums[2] and slot_nums[2] == slot_nums[0]:
            print('You won!! 5 dollars added to wallet.')
            player_wallet = player_wallet + 5
            print(f'\n Your total wallet amount is ${player_wallet}.00')
            game(player_wallet, input('Great job! Play Again??: '))
        elif slot_nums[0] == slot_nums[1] - 1 and slot_nums[0] == slot_nums[2] - 2:
            print('You won!! 4 dollars added to wallet.')
            player_wallet = player_wallet + 4
            print(f'\n Your total wallet amount is ${player_wallet}.00')
            game(player_wallet, input('Great job! Play Again??: '))
        elif player_wallet < 3 or player_wallet - 1 < 3:
            print(player_wallet)
            initial_welcome(input("You don't have enough money to continue! How much more money would you like to add?: "))
        else:
            print(f'\n Your total wallet amount is ${player_wallet}.00')
            game(player_wallet,input('No winnings :/ Play Again??: '))
            
    else:
        print('Thanks for Playing!')






initial_welcome(input('How much money would you like to add?: '))