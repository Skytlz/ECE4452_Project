import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, Flatten, InputLayer
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import json
from Queries import *


def predict(busName):
    # Connect to Database
    try: 
        conn = sqlite3.connect('BusData.db')
        cursor = conn.cursor()
        print('DB Init')

    except sqlite3.Error as error:
        print('Error occurred - ', error)

    df_actual = pd.read_sql_query(BusTimes(busName), conn)  # Actual bus times
    df_scheduled = pd.read_sql_query(scheduledTimes(busName), conn)  # Scheduled bus times
    conn.close()

    # Merge actual and scheduled dataframes on BusName and stopID
    comparison_df = pd.merge(
        df_actual, df_scheduled, on=["BusName", "stopID"]
    )

    # Parse datetime columns
    comparison_df['currtime'] = pd.to_datetime(comparison_df['currtime'], format='%H:%M:%S')
    comparison_df['ExpectedTime'] = pd.to_datetime(comparison_df['ExpectedTime'], format='%H:%M:%S')

    # Calculate time difference in seconds
    comparison_df['time_difference'] = (
        comparison_df['currtime'] - comparison_df['ExpectedTime']
    ).dt.total_seconds()


    # Create labels: early, on time, or late
    def assign_label(diff):
        if abs(diff) <= 60:  # within 1 minute is "on time"
            return 'on_time'
        elif diff > 60:
            return 'late'
        else:
            return 'early'

    comparison_df['label'] = comparison_df['time_difference'].apply(assign_label)

   # print(comparison_df)

    # Extract features and labels
    features = comparison_df[['BusName', 'stopID', 'ExpectedTime']]
    labels = comparison_df['label']

    # Convert categorical features into numerical using encoding
    features['BusName'] = features['BusName'].astype('category').cat.codes
    features['stopID'] = features['stopID'].astype('category').cat.codes
    features['ExpectedTime'] = features['ExpectedTime'].dt.hour * 3600 + \
                                         features['ExpectedTime'].dt.minute * 60 + \
                                         features['ExpectedTime'].dt.second

    # Encode labels to integers
    label_encoder = LabelEncoder()
    labels_encoded = label_encoder.fit_transform(labels)

    # Scale features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(scaled_features, labels_encoded, test_size=0.2, random_state=42)

    # Build the model
    model = Sequential()
    model.add(InputLayer(input_shape=(X_train.shape[1], )))
    
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(16, activation='relu'))
    model.add(Flatten())
    model.add(Dense(3, activation='softmax'))

    # Compile the model
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    history = model.fit(X_train, y_train, epochs=50, batch_size=16, validation_data=(X_test, y_test))

    # Evaluate the model
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f"Test accuracy: {accuracy * 100:.2f}%")

    # Predict on test set
    predictions = model.predict(X_test)
    predicted_labels = label_encoder.inverse_transform(predictions.argmax(axis=1))

    for i in range(len(predictions)):
        print("=============")
        print("Real Label: ", y_test[i], " - ", np.argmax(y_test[i]))
        print("Predicted: ", predictions[i], " - ", np.argmax(predictions[i]))

    plt.plot(history.history['accuracy'], 'o-', label="Accuracy")

    plt.title('training accuracy')
    plt.ylabel('training accuracy')
    plt.xlabel('epoch')
    plt.legend(loc='lower right')
    plt.savefig("plot.png")

    #print(predicted_labels)




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