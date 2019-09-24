import random
slots = [1,2,3,4,5,6,7]


def initial_welcome(money):
    try: 
        if type(int(money)) == int and int(money) <= 50:
            print('Welcome to the Casino!')
            print(' We will begin to play slots!')
            print("""
            Rules:
                * It costs $3.00 to play.
                * If your wallet hits zero, the game ends.
                * If your wallet does not have enough to continue the game, the game ends>
                * Max Amount of Money that can be entered is $50
            """)
            
            game(money,input('Enter Yes to play, Enter No to quit.: '))
        elif int(money) >= 1000000:
            print('\n Come on you definitely dont have more than $1,000,000.')
            initial_welcome(input('Try again. Remember, no more than $50: '))
        else:
            print('Too much money.')
            initial_welcome(input('Try again. Remember, no more than $50: '))

    except:
        try:
            if type(money) == str:
                print('Thanks for playing!')
        except:
            initial_welcome(input('Invalid Response. Needs to be an integer. Try Again: '))

def game(money,choice):
    if (choice.lower()) == 'yes':
        player_wallet = int(money)
        print(f'You are starting out with ${player_wallet}.00')
        player_wallet -= 3
        print(f'\n The game cost $3.00 so now your wallet is down to ${player_wallet}.00')
        slot_nums = []
        for i in range(0,3):
            rannum = random.randint(1,len(slots))
            slot_nums.append(rannum)
        if player_wallet < 3 or player_wallet - 1 < 3:
            print(f'Sadly your wallet is at ${player_wallet}.00')
            initial_welcome(input("You don't have enough money to continue! How much more money would you like to add? Or enter no to stop playing.: "))
        elif slot_nums[0] == slot_nums[1] and slot_nums[1] == slot_nums[2] and slot_nums[2] == slot_nums[0]:
            print('Three of the same numbers rolled!! 5 dollars added to wallet.')
            player_wallet = player_wallet + 5
            print(f'\n Your total wallet amount is ${player_wallet}.00')
            game(player_wallet, input('Great job! Play Again??: '))
        elif slot_nums[0] == slot_nums[1] - 1 and slot_nums[0] == slot_nums[2] - 2:
            print('You won!! 4 dollars added to wallet.')
            player_wallet = player_wallet + 4
            print(f'\n Your total wallet amount is ${player_wallet}.00')
            game(player_wallet, input('Great job! Play Again??: '))
        elif slot_nums[0] == 7 or slot_nums[1] == 7 or slot_nums[2] == 7:
            print('One of your rolled numbers was 7!! You get $1.00!!')
            player_wallet += 1
            print(f'\n Your total wallet amount is ${player_wallet}.00')
            game(player_wallet, input('Great job! Play Again??: '))
        
        
        else:
            print(f'\n Your total wallet amount is ${player_wallet}.00')
            game(player_wallet,input('No winnings :/ Play Again?? **Enter yes or no**: '))
            
    else:
        print('Thanks for Playing!')






initial_welcome(input('How much money would you like to add? WARNING** Only a max of $50 can be entered at a time. Thinking you have anything above $50 is just wishful thinking.: '))