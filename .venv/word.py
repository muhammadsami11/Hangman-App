class Word:
    def __init__(self,secret_word):
        self.__secret_word: str=secret_word

    def contains_letter(self,letter):
        return letter in self.__secret_word
           
    def get_display(self,guessed_word):
        display_word=""
        for x in self.__secret_word:
            if x in guessed_word:
                display_word+=x
            else:
                display_word+='-'
        return display_word

        
    def is_complete(self,guessed_word):
        for x in self.__secret_word:
            if x not in guessed_word:
                return False
        return True
            
