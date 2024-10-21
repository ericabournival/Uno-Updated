import random

colours: tuple[str] = ("Red", "Yellow", "Blue", "Green")

ranks = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "+2")

deck = [(rank, colour) for rank in ranks for colour in colours]

random.shuffle(deck)

def start_game(deck: list[tuple[int, str]]) -> None: 
	"""
	Initally called function, begins a new game of uno by 15 taking cards from the deck and assigning 7 of them to player 1, 
	7 to player 2, and 1 card to face_up. Then it begins the main loop function which is the core of gameplay.
	"""

	p1: list[tuple[int, str]] = [deck.pop(0) for _ in range(7)]
	p2: list[tuple[int, str]] = [deck.pop(0) for _ in range(7)]

	face_up: list[tuple[int, str]] = [deck.pop(0)]
	main_loop(p1, p2, face_up, deck)

def valid_play(face_up: tuple[int, str], card: tuple[int, str]) -> bool:
	"""
	Verifies if the card played is valid and returns a True/False so main_loop can execute code as needed.
	Has a message warning that because the player picked an invalid card, main_loop will add one card to their hand.
	"""
	if face_up[0] == card[0] or face_up[1] == card[1]:
		return True
	else:
		print("Invalid card selection, adding one card to your deck.")
		return False

def main_loop(p1: list[tuple[int, str]], p2: list[tuple[int, str]], face_up: list[tuple[int, str]], deck: list[tuple[int, str]]) -> None:
    """
    The core of the gameplay, uses the deck and the hands/face_up from start_game to play a game of Uno.
    States what current turn it is and runs a loop forever until at least one of the players have a hand of 0 cards.
    Prints a message explaining who is the winner once the loop has finished.
    """
    current: int = 0

    while len(p1) > 0 and len(p2) > 0:

        input(f"It is player {current + 1}'s turn, give computer to that player. Player {current + 1}, press enter to continue.")
        print(f"The face up card is {face_up[-1]}") #Tells the player what the current face_up is so they can plan their next move.
        print(f"Player {current + 1}'s cards are {p1}") #Tells the player what their cards are.
        print(f"Player {current+1}'s hand is {p1}")

        ans: int = int(input("Type '1' to play a card and type '2' to pick up a card.")) #Asks the user what they'll be doing turing their turn.
            
        if ans == 1: #If they choose to play a card.
            index: int = int(input("What is the index of the card you want to play? (starting at 1)")) - 1
            is_valid: bool = valid_play(face_up[-1], p1[index]) #Validates the card played.
            if is_valid:
                if p1[index][0] == "+2":
                    face_up.append(p1.pop(index))
                    p2.append(deck.pop(0))
                    p2.append(deck.pop(0))
                else:
                    face_up.append(p1.pop(index)) #Removes card from hand and assigns it as the latest face_up card.
                    
            else:
                p1.append(deck.pop(0)) #Forces the user to pick up a card.
        else: #If they choose to pick up a card.
            p1.append(deck.pop(0)) 

        if len(deck) == 0: #In case the entirety of the deck has been used up, this should act as a failsafe.
            deck: list[tuple[int, str]] = [face_up.pop(0) for _ in range(len(face_up))] #Assigns the empty 'deck' to the cards in face_up and removes all of the face_up cards
            random.shuffle(deck) #Shuffles deck
            print("Deck has been reshuffled")
            face_up: list[tuple[int, str]] = [deck.pop(0)] #Takes a new face_up card.
        
            p1, p2 = p2, p1 #Switches players, during 'current = 0' p1 is player 1 and p2 is player 2, and during 'current = 1' p1 is player 2 and p1 is player 1.
            current: int = (current + 1) % 2 #Switches the current state to the opposite current.

            current: int = (current + 1) % 2 #Switches the current state to the opposite current.
            print("Player 2 has won the game! Better luck next time Player 1!")
        else: #The opposite is also true, current turns into 1 as player 1 places down their last card.
            print("Player 1 has won the game! Better luck next time Player 2!")

start_game(deck) #function call to start the game when the program is run
