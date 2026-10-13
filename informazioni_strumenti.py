class Informazioni_strumenti:
    def __init__(self, codice, tipo, marca, anno, valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno = anno
        self.valore = valore

    def __str__(self):
        # Metodo speciale per stampare lo strumento in modo leggibile
        return f"[{self.codice}] {self.tipo} {self.marca} (Anno: {self.anno} - Valore: {self.valore}€)"
