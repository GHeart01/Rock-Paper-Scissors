#Rockpaperscissors
import random
rounds_played = 0
playing = True

while playing:

    def play():
        user = input("what is your choice? ('r' for rock, 'p' for paper, 's' for scissors): ").lower()
        while user not in ['r', 'p', 's']:
            print("Invalid input try again")
            user = input("what is your choice? ('r' for rock, 'p' for paper, 's' for scissors): ").lower()

        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            return 'It\'s a tie'
        
        if is_win(user, computer):
            return 'You won!'
        
        return 'You lost!'
        
        # rock > scissors, scissors > paper, paper > rock

    def is_win(player, opponent):

        if  ( player == 'r' and opponent == 's') or \
            ( player == 's' and opponent == 'p') or \
            ( player == 'p' and opponent == 'r'):
            return True
        
    print(play())
    rounds_played += 1

    if rounds_played >= 5:
        play_again = input("Would you like to play again? (Y) for yes (N) for no: ").lower()
        if play_again == 'n':
            playing = False
        else:
            rounds_played = 0

print("Thank you for playing!")

    
