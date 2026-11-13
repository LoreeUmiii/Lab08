from dataclasses import dataclass
from database import prezzo_DAO


'''
    DTO (Data Transfer Object) dell'entità Distributore
'''

@dataclass()
class Distributore:
    id: int
    nome: str
    indirizzo: str

    # RELAZIONI
    lista_prezzi: list = None

    def get_prezzi(self):
        """ Aggiorna e Restituisce la lista di prezzi (self.lista_prezzi) associati al distributore"""

        # Controllare il warning
        self.lista_prezzi = prezzo_DAO.PrezzoDAO.get_prezzi(self.id)
        # print(self.lista_prezzi)
        return self.lista_prezzi

    def __eq__(self, other):
        return isinstance(other, Distributore) and self.id == other.id

    def __str__(self):
        return f"{self.id} | {self.nome} | Indirizzo: {self.indirizzo}"

    def __repr__(self):
        return f"{self.id} | {self.nome} | Indirizzo: {self.indirizzo}"
