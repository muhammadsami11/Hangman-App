from word import Word

from score import Score
from HangmanGame import Game
from player import Player
import random


WORD_BANK = {
    "Programming & Architecture": ["python", "streamlit", "fastapi", "assembly", "emulator", "register", "memory"],
    "Databases & Networking": ["postgres", "database", "schema", "coalesce", "topology", "router", "subnet"],
    "Marketing & E-commerce": ["klaviyo", "copywriting", "commerce", "sequence", "retention", "metric"],
    "Logic & Science": ["physics", "algorithm", "variable", "function", "interface"],
    "Anime & Animation": ["naruto", "uzumaki", "madara", "goku", "kamado"]
}
class GameFactory:

    def __init__(self,player_name,category):
        self.player_name=player_name
        self.word_list=WORD_BANK[category]

    def create_game(self):
        player=Player(self.player_name)
        
        secret_word=random.choice(self.word_list)
        word=Word(secret_word)
        score=Score()
        game=Game(player,word,score)
        return game

