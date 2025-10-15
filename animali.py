from cabina import Cabina

class Animali(Cabina):
    def __init__(self, codId, num_letti, ponte, prezzo, num_animali, disponibilita):
        super().__init__(codId, num_letti, ponte, prezzo, disponibilita)
        self.num_animali = num_animali

    def __str__(self):
        return (f'{self.codId} '
                f'{self.num_letti} '
                f'{self.ponte} '
                f'{self.prezzo} '
                f'{self.num_animali} '
                f'{self.disponibilita} ')

    def __repr__(self):
        return (f'{type(self).__name__} '
                f'(codId={self.codId}, '
                f'num_letti={self.num_letti}, '
                f'ponte={self.ponte}, '
                f'prezzo={self.prezzo}, '
                f'num_animali={self.num_animali}, '
                f'disponibilita={self.disponibilita})')

    def aumenta_prezzo(self):
        self.prezzo = self.prezzo * (1 + 0.1 * self.num_animali)