from cabina import Cabina

class Animali(Cabina):
    def __init__(self, codId, num_letti, ponte, prezzo, disponibilita, num_animali):
        super().__init__(codId, num_letti, ponte, prezzo, disponibilita)
        self.num_animali = num_animali

    def __repr__(self):
        return (f'{type(self).__name__}'
                f'(codId={self.codId},'
                f'num_letti={self.num_letti},'
                f'ponte={self.ponte},'
                f'prezzo={self.prezzo})'
                f'disponibilita={self.disponibilita})'
                f'num_animali={self.num_animali})')

    def aumenta_prezzo(self):
        self.prezzo = self.prezzo * (1 + 0.1 * self.num_animali)