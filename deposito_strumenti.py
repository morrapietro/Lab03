import csv
from informazioni_strumenti import Informazioni_strumenti

class Prestito:
    def __init__(self, codice, data, id_strumento, cognome_allievo):
        self.codice = codice
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        return f"Prestito {self.codice}: Strumento {self.id_strumento} a {self.cognome_allievo} (Data: {self.data})"

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = {}  # Dizionario {codice: oggetto InformazioniStrumenti}
        self.prestiti = {}  # Dizionario {codice: oggetto Prestito}
        self.progressivo_prestito = 1

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file. open() lancia in automatico FileNotFoundError se non lo trova."""
        with open(file_path, 'r', encoding='utf-8') as file:
            # Se il tuo file ha spazi al posto delle virgole usa delimiter=' '
            reader = csv.reader(file, delimiter=',')
            for riga in reader:
                if not riga:
                    continue

                # Se il file usa spazi singoli al posto delle virgole decommenta questa riga:
                # se len(riga) == 1: riga = riga[0].split()

                codice = riga[0].strip()
                tipo = riga[1].strip()
                marca = riga[2].strip()
                anno = int(riga[3].strip())
                valore = float(riga[4].strip())

                nuovo_strumento = InformazioniStrumenti(codice, tipo, marca, anno, valore)
                self.strumenti[codice] = nuovo_strumento

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        max_id = 0
        for codice in self.strumenti.keys():
            if codice.startswith('S'):
                numero = int(codice[1:])  # Prende il numero dopo la 'S'
                if numero > max_id:
                    max_id = numero

        nuovo_codice = f"S{max_id + 1}"
        nuovo_strumento = InformazioniStrumenti(nuovo_codice, tipo, marca, anno_acquisto, valore)
        self.strumenti[nuovo_codice] = nuovo_strumento
        return nuovo_strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        lista_strumenti = list(self.strumenti.values())
        lista_strumenti.sort(key=lambda strumento: strumento.marca)
        return lista_strumenti

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        if id_strumento not in self.strumenti:
            raise Exception("Errore: Lo strumento richiesto non è presente nel deposito.")

        for prestito in self.prestiti.values():
            if prestito.id_strumento == id_strumento:
                raise Exception("Errore: Lo strumento è già in prestito.")

        codice_prestito = f"P{self.progressivo_prestito}"
        self.progressivo_prestito += 1

        nuovo = Prestito(codice_prestito, data, id_strumento, cognome_allievo)
        self.prestiti[codice_prestito] = nuovo
        return nuovo

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        if id_prestito not in self.prestiti:
            raise Exception("Errore: Codice prestito inesistente.")

        del self.prestiti[id_prestito]
