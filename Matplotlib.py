import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import Databank as db
import Numpy 

unique_species = np.unique(db.species)
unique_gelsacht = np.unique(db.geslacht)
unique_islands = np.unique(db.island)


def staafdiagram ():
    x =[]
    y= [] 

    for spec in unique_species:
        x.append(spec)
        y.append(np.size(np.where(db.species == spec)))

    # function to add value labels
    def addlabels(x,y):
        for i in range(len(y)):
            plt.text(i, y[i], y[i], ha = 'center', va = 'bottom')

    addlabels(x, y)
    kleuren = ['blue','magenta' , 'orange']    
    plt.bar(x, y, color=kleuren,width=0.4)

    ylimit_arr = []
    for x in range(3):
        ylimit_arr.append(np.size(np.where(db.species == unique_species[x])))

    plt.ylim(0,np.max(ylimit_arr)+25)    
    plt.title("Aantal pinguïns per soort")
    plt.ylabel("Aantal")
    plt.show()

def dubblestaafdiagram():
    x =[]
    y= []
    soort_geslacht = Numpy.soortpinguinsgelacht()
    for i in range (0,5,2):
        x.append(soort_geslacht[i])
        y.append(soort_geslacht[i+1])
    
    penguin_means = {'Male': (y),'Female': (x)}

    x = np.arange(len(unique_species))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in penguin_means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1


    ax.set_ylabel('Aantal Pinguïns')
    ax.set_title('Pinguïns per soort opgesplitst in geslacht')
    ax.set_xticks(x + width, unique_species)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, np.max(soort_geslacht)+20)

    plt.show()

def taartdiagramsoort ():

    size = 0.4
    vals = np.array([[73,73],[34,34],[61,58]])

    cmap = plt.colormaps["tab20c"]
    outer_colors = cmap(np.arange(3)*4)
    inner_colors = cmap([1, 5])

    plt.pie(vals.sum(axis=1), radius=1, colors=outer_colors,autopct='%1.1f%%', pctdistance=0.8,
        wedgeprops=dict(width=size, edgecolor='w'),labels=unique_species)

    plt.pie(vals.flatten(), radius=1-size, colors=inner_colors,
        wedgeprops=dict(width=size, edgecolor='w'))
    
    custom = [
        Line2D([], [], marker='o', color=cmap([1]), fillstyle="full",linestyle='None'),
        Line2D([], [], marker='o', color=cmap([5]), fillstyle="full", linestyle='None')
            ]
    plt.legend(handles = custom, labels=['Man', 'Vrouw'],  loc= "upper left")
    plt.show()

def taartdiagrameiland():
    indexsubplot = 1
    species_gelsacht_eiland = np.stack((db.species,db.geslacht,db.island), axis=1)
    for island in unique_islands:
        z = []
        for species in unique_species:
            x = []
            for geslacht in unique_gelsacht:
                test_elements = [island,species,geslacht]
                mask = np.isin(species_gelsacht_eiland, test_elements)
                
                y = []
                for w in mask:
                    y.append(np.all(w))
                
                x.append(np.shape(species_gelsacht_eiland[y])[0])        
            z.append(x)
        
        aantalspecies_eiland = np.array(z)
        filteredspecies = np.array([])
        filteredaantalspecies = np.array([])


        for x, values in enumerate(aantalspecies_eiland):
            if (sum(values != 0)):

                filteredaantalspecies = np.append(filteredaantalspecies , np.array([values]))
                filteredspecies = np.append(filteredspecies, unique_species[x])

        filteredaantalspecies = filteredaantalspecies.reshape(-1,2)

        size = 0.4
        cmap = plt.colormaps["tab20c"]
        outer_colors = cmap(np.arange(3)*4)
        inner_colors = cmap([5,1])

        plt.subplot(2,2,indexsubplot)
        indexsubplot = indexsubplot +1

        plt.pie(filteredaantalspecies.sum(axis=1), radius=1, colors=outer_colors,autopct='%1.1f%%', pctdistance=0.8,
            wedgeprops=dict(width=size, edgecolor='w'),labels=filteredspecies)

        plt.pie(filteredaantalspecies.flatten(), radius=1-size, colors=inner_colors,autopct='%1.1f%%', 
            wedgeprops=dict(width=size, edgecolor='w'))


        custom = [
            Line2D([], [], marker='o', color=cmap([1]), fillstyle="full",linestyle='None'),
            Line2D([], [], marker='o', color=cmap([5]), fillstyle="full", linestyle='None')
                ]
        plt.legend(handles = custom, labels=['Man', 'Vrouw'],  loc= "upper left")
        plt.title(f'Per soort, met onderverdeling in geslacht op eiland {island}.')
    plt.gcf().set_size_inches(13, 10)
    plt.show()



def scatter (x_axis , y_axis , xlabel , ylabel , title, xlim , ylim):
    colors = []

    for soort in db.species:
        if (soort == "Adelie"):
            colors.append("blue")
        elif (soort =="Chinstrap"):
            colors.append("magenta")
        else:
            colors.append("orange")
    fig, ax = plt.subplots()

    for z, geslacht in enumerate(db.geslacht):
        if (geslacht == "MALE"):
            ax.scatter(x_axis[z], y_axis[z], c=colors[z],marker="o",alpha=0.5)
        else:
            ax.scatter(x_axis[z], y_axis[z], c=colors[z],marker=">",alpha=0.5)


    custom = [
                Line2D([], [], marker='o', color='black', fillstyle="none",linestyle='None'),
                Line2D([], [], marker='>', color='black', fillstyle="none", linestyle='None'),
                Line2D([], [], marker='o', color='blue', linestyle='None'),
                Line2D([], [], marker='o', color='magenta', linestyle='None'),
                Line2D([], [], marker='o', color='orange', linestyle='None'),
            ]

    plt.legend(handles = custom, labels=['Man', 'Vrouw' ,"Adelie", "Chinstrap", "Gentoo" ],  loc= "upper left")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.show()

def histogram():
    pinguindata = [db.culmen_len,db.culmen_depth, db.flipper_len, db.weight]
    ylabel = ["Lengte bek in mm" , "Hoogte bek in mm" , "Lengte flipper in mm" , "Gewicht in gr"]

    for i in range(4):
        m = np.stack((db.species,pinguindata[i]), axis=1)
        for specie in unique_species:
            mask = np.isin(m , specie)
            y = []
            for w in mask:
                y.append(np.any(w))
            filtereddata = pinguindata[i][y]
            plt.subplot(2,2,i+1)
            plt.hist(filtereddata, bins=15, alpha=0.5, label=specie)
        plt.legend(loc='upper right')
        plt.ylabel("Aantal pinguïns")
        plt.xlabel(ylabel[i])
        plt.title(f"Histogram van {ylabel[i][:-6]}")

    plt.gcf().set_size_inches(11, 10)
    plt.show()
















