import Databank as db
import numpy as np


unique_species = np.unique(db.species)
unique_gelsacht = np.unique(db.geslacht)
unique_islands = np.unique(db.island)


def pinguinsoort ():
    for spec in unique_species:
        print(f'{spec}: {np.size(np.where(db.species == spec))} ')


def totaalpinguinsgeslacht():
    print(f'Aantal mannelijke gemeten penguins : {np.size(np.where(db.geslacht == "MALE"))}')
    print(f'Aantal vrouwelijke gemeten penguins : {np.size(np.where(db.geslacht == "FEMALE"))}')


def soortpinguinsgelacht():
    value_arr = []
    species_gelsacht = np.stack((db.species,db.geslacht), axis=1)
    for specie in unique_species:
        for geslacht in unique_gelsacht:
            filteritems = [specie ,geslacht]
            mask = np.isin(species_gelsacht , filteritems)

            filtered_arr = []
            for w in mask:
                filtered_arr.append(np.all(w))
            print(f'{geslacht} {specie}:  {len(db.species[filtered_arr])}')
            value_arr.append(len(db.species[filtered_arr]))
    return value_arr

            


def meestepinguinseiland():
    meeste_penguins = np.unique(db.island ,return_counts=True)
    print (f'Eiland met meeste penguins is : {meeste_penguins[0][0]} aantal- {meeste_penguins[1][0]}')


def zwaarstepinguin():
    max_gewicht = np.max(db.weight)/1000
    max_gewicht_soort = db.species[np.argmax(db.weight)]
    print(f'Zwaarste penguin hoort bij de {max_gewicht_soort} soort en weegt {max_gewicht}kg')


def langstebek():
    langste_bek = np.max(db.culmen_len)/10
    langste_bek_soort = db.species[np.argmax(db.culmen_len)]
    print(f'Langste gemeten penguin bek hoort bij de {langste_bek_soort} soort en is {langste_bek}cm')


def pinguingewichtverschil():
    species_gewicht_geslacht = np.stack((db.species,db.weight,db.geslacht),axis=0)
    for spec in unique_species:
        m= np.where((species_gewicht_geslacht[0] == spec) & (species_gewicht_geslacht[2] == 'MALE'))
        f=np.where((species_gewicht_geslacht[0] == spec) & (species_gewicht_geslacht[2] == 'FEMALE'))
        print(f'Het gewichtsverschil tussen de mannelijke en vrouwelijke penguin van de soort {spec} is {np.max(db.weight[m])-np.max(db.weight[f])}g')


