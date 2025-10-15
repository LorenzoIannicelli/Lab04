from cabina import Cabina

class Deluxe(Cabina):
    def __init__(self, codId, num_letti, ponte, prezzo, disponibilita, tipo):
        super().__init__(codId, num_letti, ponte, prezzo, disponibilita)
        self.tipo = tipo

    def __repr__(self):
        return (f'{type(self).__name__}'
                f'(codId={self.codId},'
                f'num_letti={self.num_letti},'
                f'ponte={self.ponte},'
                f'prezzo={self.prezzo})'
                f'disponibilita={self.disponibilita})'
                f'tipo={self.tipo})')

    def aumenta_prezzo(self):
        self.prezzo = self.prezzo * 1.20