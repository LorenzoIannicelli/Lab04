from cabina import Cabina

class Deluxe(Cabina):
    def __init__(self, codId, num_letti, ponte, prezzo, tipo, disponibilita):
        super().__init__(codId, num_letti, ponte, prezzo, disponibilita)
        self.tipo = tipo

    def __str__(self):
        return (f'{self.codId} '
                f'{self.num_letti} '
                f'{self.ponte} '
                f'{self.prezzo} '
                f'{self.tipo} '
                f'{self.disponibilita}')

    def __repr__(self):
        return (f'{self.codId}: {type(self).__name__} | '
                f'{self.num_letti} letti - '
                f'Ponte {self.ponte} - '
                f'Prezzo {self.prezzo:.2f} - '
                f'Tipo {self.tipo} - '
                f'{self.disponibilita}')

    def aumenta_prezzo(self):
        self.prezzo = self.prezzo * 1.20