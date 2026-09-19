class Score:
    def __init__(self):
        self.__score=0
    def add_point(self):
        self.__score+=10
        
    def subtract_point(self):
        self.__score-=5
    @property
    def get_score(self):
        return self.__score
