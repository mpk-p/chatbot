"""

Ce fichier gère le mécanisme des mini-jeux.

"""


class RockPaperScissors:
    def __init__(self) -> None:
        pass
def RockPaperScissors1 (move_played) :
    possible_moves = ['Scissors','Rock','Paper']
    assert move_played in possible_moves
    ai_move_played = choice(possible_moves)
    if ai_move_played == move_played : return 'Egalité'
    else :
        if move_played == 'Scissors' and ai_move_played == 'Paper' : return 'Victoire'
        elif move_played == 'Rock' and ai_move_played == 'Scissors' : return 'Victoire'
        elif move_played == 'Paper' and ai_move_played == 'Rock' : return 'Victoire'
        else : return 'Défaite'

def RockPaperScissors2 () :
    possible_moves = ['Scissors','Rock','Paper']
    ai_move_played = choice(possible_moves)
    move_played = str(input('Quel coup voulez vous jouez ?'))
    assert move_played in possible_moves
    if ai_move_played == move_played : return 'Egalité'
    else :
        if move_played == 'Scissors' and ai_move_played == 'Paper' : return 'Victoire'
        elif move_played == 'Rock' and ai_move_played == 'Scissors' : return 'Victoire'
        elif move_played == 'Paper' and ai_move_played == 'Rock' : return 'Victoire'
        else : return 'Défaite'
