import mariadb
import numpy as np


myconnection= mariadb.connect(host="localhost",user="root",password="",database="penguins")
mydb = myconnection.cursor()
mydb.execute("SELECT * FROM penguins WHERE sex != 'NA' AND sex != '.' AND sex != '' ")



penguin = mydb.fetchall()
penguinArr = np.array(penguin)


species = penguinArr[:,0].astype(str)
island = penguinArr[:,1].astype(str)
culmen_len = penguinArr[:,2].astype(float)
culmen_depth = penguinArr[:,3].astype(float)
flipper_len = penguinArr[:,4].astype(int)
weight = penguinArr[:,5].astype(int)
geslacht = penguinArr[:,6].astype(str)

