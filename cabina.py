class Cabina:
    def __init__(self, codId, num_letti, ponte, prezzo, disponibilita):
        self.codId = codId
        self.num_letti = num_letti
        self.ponte = ponte
        self.prezzo = prezzo
        self.disponibilita = disponibilita

    def __str__(self):
        return (f'{self.codId} '
                f'{self.num_letti} '
                f'{self.ponte} '
                f'{self.prezzo} '
                f'{self.disponibilita} ')

    def __repr__(self):
        return (f'{self.codId}: {type(self).__name__} | '
                f'{self.num_letti} letti - '
                f'Ponte {self.ponte} - '
                f'Prezzo {self.prezzo:.2f} - '
                f'{self.disponibilita}')
