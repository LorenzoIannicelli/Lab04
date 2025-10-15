class Passeggero:
    def __init__(self, codId, nome, cognome):
        self.codId = codId
        self.nome = nome
        self.cognome = cognome

    def __repr__(self):
        return (f'{type(self).__name__}'
                f'(codId={self.codId}',
                f'nome={self.nome},'
                f'cognome={self.cognome})')