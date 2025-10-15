import csv
from passeggero import Passeggero
from cabina import Cabina
from deluxe import Deluxe
from animali import Animali

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self._passeggeri = []
        self._cabine = []

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""

        with open(file_path, 'r', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            for line in reader:
                if line[0][:-1] == "P":
                    passeggero = Passeggero(dato for dato in line)
                    self._passeggeri.append(passeggero)
                elif line[0][:-1] == "CAB":
                    if len(line) == 5:
                        if line[-1].isdigit():
                            cabina = Animali(dato for dato in line)
                        else:
                            cabina = Deluxe(dato for dato in line)

                    cabina.aumenta_prezzo()

                    else:
                        cabina = Cabina(dato for dato in line)

                    self._cabine.append(cabina)


    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

