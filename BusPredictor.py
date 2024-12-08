# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Embedding, Flatten, Input
# from tensorflow.keras.optimizers import Adam
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler, OneHotEncoder
# import numpy as np

import sqlite3
import json
from Queries import *




def retrieveBusData(busName):
    try: 
        sqliteConnection = sqlite3.connect('BusData.db')
        cursor = sqliteConnection.cursor()
        print('DB Init')

    except sqlite3.Error as error:
        print('Error occurred - ', error)

    cursor.execute(BusIDChoice(busName))
    result = cursor.fetchall()
    #print('{}'.format(result))
    busses = [str(id[0]) for id in result]
    busIds = str()
    for i in range(len(busses)):
        busIds += busses[i]
        if i != len(busses)-1:
            busIds += ", "
    t = True
    while t:
        id = input("There are " + str(len(busses))+ f" busses currently on this route. ({busIds})"+ "\nPick one: ")
        if id in busses: t = False
        else: print("Not a valid bus id.")
    
    cursor.execute(busStops(busName, id))
    result = cursor.fetchall()
    print('{}'.format(result))

    for x in result:
        print(x[1] + " " + x[5] + " " + str(x[7]) + "\n")
    

print("""|BusName|
|-------|
|  TCR  |
|  CAS  |
|  CRC  |
|  SMS  |
|  TTT  |
|  CRB  |
|  HWB  |
|  BLU  |
|  NMG  |
|  UCB  |
|  PRG  |
|  PHB  |
|  HWA  |
|  PHD  |
|  HDG  |
|  SMA  |
|  GLD  |
|  HXP  |
""")

busName = input("Select which Bus to get predictions from: ")

retrieveBusData(busName.upper())