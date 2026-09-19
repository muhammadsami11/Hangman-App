

class Game:
    def __init__(self,player,word,score):
        self.player=player
        self.word=word
        self.score=score
        self.wrong_guesses: list[str]=[]
        self.game_over: bool=False
        self.attempts_remaining:int=6
        

    def process_guess(self,letter):
        # is p already guessed if not guessed it
        if self.player.has_guessed(letter):
            return "repeated"
        else:
            self.player.add_guess(letter)
        #ask word does p exist

            if self.word.contains_letter(letter):
                self.score.add_point()
                return "correct"
            else:
                self.score.subtract_point()
                self.wrong_guesses.append(letter)
                self.attempts_remaining-=1
                return "wrong"
        
    def check_win(self):
        if self.word.is_complete(self.player.guessed_letters):
            self.game_over=True
            return True
        return False
    def check_lose(self):
        if self.attempts_remaining==0:
            self.game_over=True
            return True
        return False
        

