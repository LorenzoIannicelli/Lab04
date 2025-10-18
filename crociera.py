import csv
from passeggero import Passeggero
from cabina import Cabina
from deluxe import Deluxe
from animali import Animali

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self.passeggeri = []
        self.cabine = []
        self.prenotazioni = []

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
                    codId, nome, cognome = line
                    passeggero = Passeggero(codId, nome, cognome)
                    self.passeggeri.append(passeggero)
                elif line[0][:-1] == "CAB":
                    if len(line) == 5:
                        if line[-1].isdigit():
                            codId, num_letti, ponte, prezzo, num_animali = line
                            cabina = Animali(codId, num_letti, ponte, float(prezzo), int(num_animali), 'Disponibile')
                        else:
                            codId, num_letti, ponte, prezzo, tipo = line
                            cabina = Deluxe(codId, num_letti, ponte, float(prezzo), tipo, 'Disponibile')

                        cabina.aumenta_prezzo()

                    else :
                        codId, num_letti, ponte, prezzo = line
                        cabina = Cabina(codId, num_letti, ponte, float(prezzo), 'Disponibile')

                    self.cabine.append(cabina)


    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""

        check = False
        prenotazione = []
        for cabina in self.cabine:
            if cabina.codId == codice_cabina and cabina.disponibilita == 'Disponibile':
                prenotazione.append(cabina)
                cabina.disponibilita = 'Non disponibile'
                break

        for passeggero in self.passeggeri:
            if passeggero.codId == codice_passeggero and passeggero.libero :
                prenotazione.append(passeggero)
                passeggero.libero = False
                break

        if len(prenotazione) == 2:
            check = True
            self.prenotazioni.append(prenotazione)

        return check

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""

        cabine_ordinate = sorted(self.cabine, key=lambda cabina: cabina.prezzo)

        return cabine_ordinate


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """

        for p in self.passeggeri:
            found = False
            print(p.__str__(), end=' ')
            for pren in self.prenotazioni:
                if p == pren[1] :
                    print(pren[0].codId)
                    found = True
                    break

            if not found:
                print()