import sys
import os


DBarbitri = "arbitri.txt"
DBsedinte = "sedinte.txt"
DBraliuri = "raliuri.txt"
DBmateriale = "materiale.txt"

class arbitru:
    def __init__(self, id, nume, an_inscriere, nr_raliuri, competente):
        self.id = id
        self.nume = nume
        self.an_inscriere = an_inscriere
        self.nr_raliuri = nr_raliuri
        self.competente = competente

class sedinta:
    def __init__(self, id, data, subiect, participanti, locatie):
        self.id = id
        self.data = data
        self.subiect = subiect
        self.participanti = participanti
        self.locatie = locatie

class raliu:
    def __init__(self, nume, data, locatie, arbitri_delegati):
        self.nume = nume
        self.data = data
        self.locatie = locatie
        self.arbitri_delegati = arbitri_delegati

class material:
    def __init__(self, id, nume, an_dare_in_folosinta, nr_folosiri, stare):
        self.id = id    
        self.nume = nume
        self.an_dare_in_folosinta = an_dare_in_folosinta
        self.nr_folosiri = nr_folosiri
        self.stare = stare

def open_file(filename, mode):
    try:
        file=open(filename, mode)
        return file
    except FileNotFoundError:
        print(f"Eroare: fisierul {filename} nu a fost gasit.")
        return None
    
def add_entry(filename, entry):
    with open(filename, "a") as file:
        file.write(entry + "\n")

def arbitri():
    
    print("Gestionare arbitri")
    selectie=input("Alegeti o optiune: \n1. Adauga arbitru\n2. Afiseaza arbitri\n3. Sterge arbitru\n4. Meniu Anterior\n\n")
    match selectie:
        case "1":
            with open("arbitri", "a", encoding="utf-8") as data:
                id = input("Introduceti ID-ul arbitru: ")
                nume = input("Introduceti numele arbitru: ")
                an_inscriere = input("Introduceti anul inscrierii: ")
                nr_raliuri = input("Introduceti numarul de raliuri: ")
                competente = input("Introduceti competentele arbitru: ")

                entry = f"{id} | {nume} | {an_inscriere} | {nr_raliuri} | {competente}\n"
                data.write(entry)
                data.close()
        case "2":
            with open("arbitri", "r", encoding="utf-8") as data:
                content = data.read()
                print(content)
                data.close()

        case "3":
            with open("arbitri", "w", encoding="utf-8") as data:
                id_sters = input("Introduceti ID-ul arbitru de sters: ")
                lines = data.readlines()
                data.seek(0)
                for line in lines:
                    if not line.startswith(id_sters):
                        data.write(line)
                data.truncate()
                data.close()

        case "4":
            return

def sedinte():
    pass

def raliuri():
    pass

def materiale():
    pass

def main():
    print("Bine ati venit la aplicatia de gestionare a colegiului Moldova!")
    selectie=""
    while selectie not in ["1", "2", "3", "4", "5"]:
        selectie=input("Acesati baza de date pentru: \n1. Arbitri\n2. Sedinte\n3. Raliuri\n4. Materiale\n5. Inchideti aplicatia\n\n")
        match selectie:
            case "1":
                arbitri()
            case "2":
                sedinte()
            case "3":
                raliuri()
            case "4":
                materiale()
            case "5":
                print("Aplicatia se va inchide.")
                return
        selectie=""
main()