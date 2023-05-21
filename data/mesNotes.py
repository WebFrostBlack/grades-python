import os
import json
import sys

json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ratings.json')

mesNotes = []

if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as f:
        try:
            mesNotes = json.load(f)
        except json.decoder.JSONDecodeError:
            pass

def sauvegarderNotes():
    with open(json_file_path, 'w') as f:
        json.dump(mesNotes, f)

def calculerMoyenne():
    notes_valides = [note for note in mesNotes if isinstance(note, (int, float))]
    
    if len(notes_valides) == 0:
        return None
    
    somme = sum(notes_valides)
    moyenne = somme / len(notes_valides)
    return moyenne



def revenirMenuPrincipalAjouterNote():
    RevenirMenu = input('\n\n[.1] Return to the menu         |           [.2] Add a new grade\n\n')
    if RevenirMenu == '1':
        menuPrincipal()
    elif RevenirMenu == '2':
        ajouterNote()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(' ⚠️ Invalid character ! ⚠️')
        revenirMenuPrincipalAjouterNote()

def revenirMenuPrincipalVoirNotes():
    RevenirMenu = input('\n\n[.1] Return to the menu : ')
    if RevenirMenu == '1':
        menuPrincipal()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(' ⚠️ Invalid character ! ⚠️')
        revenirMenuPrincipalVoirNotes()

def revenirMenuPrincipalSupprimerNote():
    RevenirMenu = input('\n\n[.1] Return to the menu          |           [.2] Delete a new grade\n\n')
    if RevenirMenu == '1':
        menuPrincipal()
    elif RevenirMenu == '2':
        supprimerNote()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(' ⚠️ Invalid character ! ⚠️')
        revenirMenuPrincipalAjouterNote()

def ajouterNote():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('[--------------------| ➕ Add a new grade ➕ |----------------]\n\n')
    nouvelleNote = float(input('The grade to be added : '))
    mesNotes.append(nouvelleNote)
    sauvegarderNotes()
    revenirMenuPrincipalAjouterNote()



def voirNotes():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('[--------------------| 📄 My Grades 📄 |----------------]\n\n')
    for note in mesNotes:
        print(note)
    moyenne = calculerMoyenne()
    if moyenne is not None:
        moyenne_arrondie = round(moyenne, 2)
        print(f"\nAverage score : {moyenne_arrondie}")
    else:
        print("No grades recorded.")
    revenirMenuPrincipalVoirNotes()

def supprimerNote():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('[--------------------| ❌ Delete a grade ❌ |----------------]\n\n')
    if not mesNotes:
        print("No grades recorded.")
        revenirMenuPrincipalSupprimerNote()
        return

    print("Grades available :")
    for i, note in enumerate(mesNotes):
        print(f"{i+1}. {note}")

    try:
        index = int(input("Enter the grade number to be deleted : ")) - 1
        if 0 <= index < len(mesNotes):
            del mesNotes[index]
            sauvegarderNotes()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Grade deleted successfully.")
        else:
            print("Invalid grade number.")
    except ValueError:
        print("Invalid grade number.")

    revenirMenuPrincipalSupprimerNote()


def menuPrincipal():
    os.system('cls' if os.name == 'nt' else 'clear')
    inputResponseMenu = input('[---------------------------------------------------------| 🏠 Welcome to the main menu 🏠 |---------------------------------------------------------]\n\n [.1] 📄 View my grades          |           [.2] ➕ Add a grade        |           [.3] ❌ Delete a grade          |           [.4] 📛 Close\n\n')
    if inputResponseMenu == '1':
        voirNotes()
    elif inputResponseMenu == '2':
        ajouterNote()
    elif inputResponseMenu == '3':
        supprimerNote()
    elif inputResponseMenu == '4':
        sys.exit()
    else:
        print(' ⚠️ Invalid character ! ⚠️')
        menuPrincipal()

menuPrincipal()
