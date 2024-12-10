import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, Flatten, InputLayer
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np
import pandas as pd

import sqlite3
import json
from Queries import *




def predict(busName):
    try: 
        conn = sqlite3.connect('BusData.db')
        cursor = conn.cursor()
        print('DB Init')

    except sqlite3.Error as error:
        print('Error occurred - ', error)

    # cursor.execute(BusIDChoice(busName))
    # result = cursor.fetchall()
    # #print('{}'.format(result))
    # busses = [str(id[0]) for id in result]
    # busIds = str()
    # for i in range(len(busses)):
    #     busIds += busses[i]
    #     if i != len(busses)-1:
    #         busIds += ", "
    # t = True
    # while t:
    #     id = input("There are " + str(len(busses))+ f" busses currently on this route. ({busIds})"+ "\nPick one: ")
    #     if id in busses: t = False
    #     else: print("Not a valid bus id.")
    
    # cursor.execute(busStops(busName, id))
    # result = cursor.fetchall()
    # print('{}'.format(result))

    # cursor.execute(BusTimes(busName))
    # result = cursor.fetchall()

    df1 = pd.read_sql_query(BusTimes(busName), conn)
    # print('{}'.format(df1))
    df2 = pd.read_sql_query(scheduledTimes(busName), conn)
    # print('{}'.format(df2))
    conn.close()

    merged_df = pd.merge(df1, df2, left_on=["BusName", "stopID"], right_on=["BusName", "stopID"])

    merged_df['currtime'] = pd.to_datetime(merged_df['currtime'], format='%H:%M:%S')
    merged_df['ExpectedTime'] = pd.to_datetime(merged_df['ExpectedTime'], format='%H:%M:%S')

    merged_df['time_difference'] = (merged_df['currtime'] - merged_df['ExpectedTime']).dt.total_seconds()

    def categorize_time_difference(diff):
        if diff < 0:
            return 0  # Early
        elif diff == 0:
            return 1  # On time
        else:
            return 2  # Late

    merged_df['label'] = merged_df['time_difference'].apply(categorize_time_difference)

    # Feature selection
    features = merged_df[['speed', 'direction', 'stopID']]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    labels = to_categorical(merged_df['label'], num_classes=3)

    X_train, X_test, y_train, y_test = train_test_split(scaled_features, labels, test_size=0.2, random_state=42)

    model = Sequential()
    model.add(InputLayer(shape=(X_train.shape[1],)))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(3, activation='softmax'))  # Use softmax for multi-class classification

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    model.fit(X_train, y_train, epochs=50, batch_size=16, validation_data=(X_test, y_test))

    loss, accuracy = model.evaluate(X_test, y_test)
    print(f"Test accuracy: {accuracy * 100:.2f}%")

    predictions = model.predict(X_test)

    # Convert predictions to class labels
    predictions = model.predict(X_test)
    predicted_labels = np.argmax(predictions, axis=1)
    print(predicted_labels)





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

# busName = input("Select which Bus to get predictions from: ")

predict("HDG")