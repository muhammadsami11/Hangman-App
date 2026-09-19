class Player:
    def __init__(self,player_name):
        self.player_name:str=player_name
        self.guessed_letters:list[str]=[]
        

    def add_guess(self,letter):
        
        self.guessed_letters.append(letter)
    def has_guessed(self,letter):
        return letter in self.guessed_letters
           

