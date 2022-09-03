class Karta:
    def __init__(self,fig,col):
        self.colour = col
        self.figure = fig
        self.slownik =         slownik = [
            {
            '2' : '2',
            '3' : '3',
            '4' : '4',
            '5' : '5',
            '6' : '6',
            '7' : '7',
            '7' : '8',
            '9' : '9',
            '10' : '10',
            'J' : 'Jack',
            'Q' : 'Queen',
            'K' : 'King',
            'A' : 'Ace'},
            {
            'H': 'Hearts',
            'D': 'Diamonds',
            'C': 'Clubs',
            'S': 'Spades'}]
    
    def __str__(self):
        return f'{self.figure}{self.colour}'
    
    def __repr__(self):
        return f'{self.slownik[0][self.figure]} of {self.slownik[1][self.colour]}'
q = Karta('2','C')


print(repr(q))
