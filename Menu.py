import os
import Numpy
import Databank as db
import Matplotlib
import Machine_Learning  as ML

while True:
    os.system("cls")
    print('PINGUIN MENU')
    print('~~~~~~~~~~~~~~~')
    main_menu = input('1.Numpy\n2.Matplotlib \n3.Machine Learning \nq.Einde Programma\n')

    if main_menu == "1":
        while True:
            os.system("cls")
            print('NUMPY')
            print('~~~~~~~~~~~~~~~~~~~~')
            sub_menu1= input('1.Hoeveel pinguïns zijn er van elke soort? \n2.Totaal mannelijke en vrouwelijke pinguïns ?'+ 
                             '\n3.Totaal mannelijke en vrouwelijke pinguïns van elke soort?. \n4.Op welk eiland wonen de meeste pinguïns?'+
                             '\n5.Tot welke soort behoort de zwaarste pinguïn?\n6.Welke soort heeft de langste gemeten bek?' +
                             '\n7.Verschil tussen de zwaarste mannetjes pinguïnen de zwaarste vrouwelijke pinguïn van elke soort.'+
                             '\n8.Naar vorige menu.\n')
            if sub_menu1 == '1':
                Numpy.pinguinsoort()
            elif sub_menu1 == "2":
                Numpy.totaalpinguinsgeslacht()
            elif sub_menu1 == "3":
                Numpy.soortpinguinsgelacht() 
            elif sub_menu1 == "4":
                Numpy.meestepinguinseiland()
            elif sub_menu1 == "5":
                Numpy.zwaarstepinguin() 
            elif sub_menu1 == "6":
                Numpy.langstebek()
            elif sub_menu1 == "7":
                Numpy.pinguingewichtverschil()                                            
            elif sub_menu1 == "8":
                break
            input("Druk op een toets om door te gaan....")

    elif main_menu == "2":
        while True:
            os.system("cls")
            print('MATPLOTLIB')
            print('~~~~~~~~~~~~~~~~~~~~')
            sub_menu2= input('1.Staafdiagram van hoeveel pinguïns er zijn van elke soort \n2.Een dubbele staafdiagram per soort opgesplitst in geslacht.' + 
                             '\n3.Taartdiagram per soort metonderverdeling in geslacht.\n4.Taartdiagram Per eiland de soorten, met onderverdeling in geslacht.'+
                             '\n5.Histogram per soort met 15 bins.\n6.Scatter verhouding lengte flipper en gewichtt.\n7.Scatter lengte en hoogte van de bek\n8.Naar vorige menu.\n')
            if sub_menu2 == '1':
                Matplotlib.staafdiagram()
            elif sub_menu2 == "2":
                Matplotlib.dubblestaafdiagram()
            elif sub_menu2 == "3":
                Matplotlib.taartdiagramsoort()
            elif sub_menu2 == "4":
                Matplotlib.taartdiagrameiland()
            elif sub_menu2 == "5":
                Matplotlib.histogram()
            elif sub_menu2 == "6":
                Matplotlib.scatter(db.flipper_len , db.weight , 'Lengte Flipper in mm','Gewicht in gram' ,'Verhouding tuseen gewicht en lengte flipper' , 168 , 2550)
            elif sub_menu2 == "7":
                Matplotlib.scatter (db.culmen_len , db.culmen_depth , 'Hoogte bek in mm','Lengte bek in mm' ,'Verhouding tuseen lengte en hoogte van de bek.',0 ,0)   
            elif sub_menu2 == "8":
                break
            input("Druk op een toets om door te gaan....")

    elif main_menu == "3":
        while True:
            os.system('cls')
            print('MACHINE LEARNING')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            sub_menu3= input('1.Machine Learning\n2.Naar vorige menu.\n')
            if sub_menu3 == '1':
                ML.ML()
            elif sub_menu3 == "2":
                break
            input("Druk op een toets om door te gaan....")

    elif main_menu == "q":
         break