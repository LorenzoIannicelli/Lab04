class Passeggero:
    def __init__(self, codId, nome, cognome):
        self.codId = codId
        self.nome = nome
        self.cognome = cognome
        self.libero = True

    def __str__(self):
        return f'{self.codId} {self.nome} {self.cognome}'

    def __repr__(self):
        return (f'{type(self).__name__} '
                f'(codId={self.codId}, '
                f'nome={self.nome}, '
                f'cognome={self.cognome}, '
                f'libero={self.libero})')

    def __eq__(self, other):
        return self.codId == other.codId and self.nome == other.nome and self.cognome == other.cognome