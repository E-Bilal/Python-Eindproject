import Databank as db
import numpy as np


species = np.unique(db.species)
geslacht = np.unique(db.geslacht)
islands = np.unique(db.island)

bek_l_prompt = "Geef de bek lengte in mm:"
bek_h_prompt = "Geef de bek hoogte in mm:"
flipper_l_prompt = "Geef de flipper lengte in mm:"
gewicht_prompt = "Geef het gewicht in g:"
eiland_prompt = "Geef het eiland (1.Biscoe 2.Dream 3.Torgersen):"
geslacht_prompt = "Geef het geslacht in (1.Man 2.Vrouw 3.Ongekend): "
prompt_arr = [bek_l_prompt,bek_h_prompt,flipper_l_prompt,gewicht_prompt]

inputdata_arr = []


def inputvalidatie():
    
    for prompt in prompt_arr:
        while True:
            try:
                inp = float(input(prompt))
            except ValueError:
                print('Je gaf geen getal in')
            else:
                inputdata_arr.append(inp)
                break

    #Geslacht validatie
    while True:
        inp = input(geslacht_prompt)
        if inp in ('1', '2', '3'):
            if (inp == '1'):
                inp = "MALE"
            elif (inp == '2'):
                inp = "FEMALE"
            elif (inp == '3'):
                inp = "UNKNOWN"
            inputdata_arr.append(inp)
            break
    #Eiland validatie     
    while True:
        inp = input(eiland_prompt)
        if inp in ('1', '2', '3'):
            if (inp == '1'):
                inp = 'Biscoe'
            elif (inp == '2'):
                inp = 'Dream'
            elif (inp == '3'):
                inp = 'Torgersen'
            inputdata_arr.append(inp)
            break


def insertData():
    kolomnamen_string = 'culmen_length_mm, culmen_depth_mm, flipper_length_mm , body_mass_g, sex, island,species'
    kolomvalues_string =f"{inputdata_arr[0]},{inputdata_arr[1]},{inputdata_arr[2]},{inputdata_arr[3]},'{inputdata_arr[4]}','{inputdata_arr[5]}','{inputdata_arr[6]}'"

    try:
        db.mydb.execute(f"INSERT INTO penguins ({kolomnamen_string}) VALUES ({kolomvalues_string})")
    except db.myconnection.Error as e:
        print(f"\n{e}")
        input('\nDruk op een toets om door te gaan....')
    else:
        db.myconnection.commit()
        input('\nData successvol toegevoed....')


def voorspellingGemDev(uniquearr, uniquedata,pinguindata, inp , dataindex, printtext, result_arr2D):
    uniqueindex = 0
    dev_arr = np.zeros(3)
    gemiddelde_arr = np.zeros(len(uniquearr))

    for i in uniquearr:
        global afwijking_counter
        data_species = np.stack((pinguindata,uniquedata),axis=1)
        mask = np.isin(data_species , i)
        y = []

        for w in mask:
            y.append(np.any(w))

        pinguindata_gem = np.mean(pinguindata[y])
        pinguindata_dev = np.std(pinguindata[y])
        
        pinguindata_lowerbound = pinguindata_gem - (2* pinguindata_dev)
        pinguindata_higherbound = pinguindata_gem + (2* pinguindata_dev)

        gemiddelde_arr[uniqueindex] = pinguindata_gem
        
        if pinguindata_lowerbound <= inp <= pinguindata_higherbound:
                dev_arr[uniqueindex] = 1
        uniqueindex = uniqueindex +1

    #.T flipt de array zodat het gebruik maken van np.sum makkelijker is.

    if (int(np.sum(dev_arr) == 0)):

        afwijking_counter = afwijking_counter +1 
        print(f"Melding: De ingevoerde data valt buiten de verwachte afwijking van alle {uniqueindex} {printtext}.Input wordt nog steeds verwerkt")
    else:
        idx = (np.abs(gemiddelde_arr - inp)).argmin()

        result_arr2D[idx,dataindex] = 1




pinguindata_arr= [db.culmen_len,db.culmen_depth,db.flipper_len,db.weight]
# result_arr2D = np.array([])
afwijking_counter = 0

def ML():
    global inputdata_arr
    inputdata_arr = []
    inputvalidatie()
    
    dataindex = 0
    result_arr2D = np.array([])
    global afwijking_counter 

    #Resetten van values
    result_arr2D = np.zeros((3,4))
    afwijking_counter = 0

    for x in range(4):
        voorspellingGemDev(species,db.species,pinguindata_arr[x], inputdata_arr[x] , dataindex, "soorten", result_arr2D)
        dataindex = dataindex + 1 

    #Som van de metingen per soort.    
    result_arr1D = np.zeros(3)    
    for x in range(3):
        result_arr1D[x] = np.sum(result_arr2D[x])

    occurences = np.where(result_arr1D == result_arr1D.max())[0]

    #Nakijken of er teveel afwijkingen zijn. Als 2 van 4 metingen afwijkt bij de soort pinguin wordt de data niet gebruikt.    
    if(afwijking_counter >= 2):
        print("Er zijn te veel afwijkingen bij de ingegeven data. Deze metingen worden niet toegevoegd in de database")
        return  
    
    #Database niet groot genoeg om te bepalen over welke soort het gaat.    
    elif (len(occurences) > 1 ):
        print(f"Er is geen hoge waarschijnlijkheid over welke soort pinguin het gaat. Dus zullen deze metingen worden niet toegevoegd in de database")
        print(f"Mogelijk pinguins:")
        i = 0
        for item in occurences:
            print(f'{species[occurences[i]]}')    
            i = i +1    
        return
    
    #Metingen specifiek genoeg om te bepalen over welke soort het gaat.Soort word geapend aan de inputdata_arr
    elif (len(occurences) == 1 ):
        inputdata_arr.append(species[occurences[0]])
        print(f"De soort pinguin is hoogstwaarschijnlijk een {species[occurences[0]]}")

    #Als er geen geslacht werd ingegeven wordt deze hier bepaald door gewicht.
    if(inputdata_arr[4] != "MALE" and inputdata_arr[4] != "FEMALE" ):
        
        #Resetten van values
        result_arr2D = np.zeros((2,1))
        afwijking_counter = 0
        dataindex = 0

        for x in range(1):
            voorspellingGemDev(geslacht,db.geslacht,pinguindata_arr[3], inputdata_arr[3] , dataindex , "geslachten", result_arr2D)
            dataindex = dataindex + 1

        result_arr1D = result_arr2D.reshape([1,2])
        if(afwijking_counter == 0):
            inputdata_arr[4] = geslacht[np.argmax(result_arr1D)]
        elif(afwijking_counter == 1):
            if (inputdata_arr[3] >np.mean(db.weight) + (2* np.std(db.weight))):
                inputdata_arr[4] = "MALE"
            else:
                inputdata_arr[4] = "FEMALE"
        print(f"De waarschijnlijke geslacht is : {inputdata_arr[4]}")

    insertData()
    while True:
        keuze = input("Extra voorspelling op welk eiland deze meeting waarschijnlijk heeft plaatsgevonden (y/n)?")
        if (keuze.capitalize() == 'Y' ):
            eilandvoorspelling()
            break
        elif(keuze.capitalize() =='N'):
            break





def eilandvoorspelling ():
    specie = inputdata_arr[6]
    result = []
    totaalpinguinsoort = len(np.where(db.species == specie)[0])
    island_species = np.stack((db.island,db.species),axis=0)

    for island in islands:
         result.append(len(np.where((island_species[0] == island) & (island_species[1] == specie))[0]))

    for x in range(3) :
        if (result[x] == 0): 
            print(f"Deze pinguin heeft 0% kans om op de eiland {(islands[x])} te leven")
        else:
            print(f"{specie} pinguin heeft {round((result[x]/totaalpinguinsoort)*100,2)}% kans om op de eiland {islands[x]} te leven")






