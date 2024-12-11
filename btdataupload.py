import sqlite3
import json
import sched
import time
import urllib.request

scheduler = sched.scheduler(time.time, time.sleep)
try: 
        sqliteConnection = sqlite3.connect('BusData.db')
        cursor = sqliteConnection.cursor()
        print('DB Init')

except sqlite3.Error as error:
        print('Error occurred - ', error)


def uploadToDB(cursor):

    with urllib.request.urlopen("https://ridebt.org/index.php?option=com_ajax&module=bt_map&format=json&Itemid=101&method=getBuses") as f:
        j = json.load(f)
        d = j["data"]
        # print(j["data"][0])
        for i in range(len(d)):
            Id = str(d[i]["id"])
            routeId = str(d[i]["routeId"])
            stopId = str(d[i]["stopId"])
            capacity = str(d[i]["capacity"])
            percentOfCapacity = str(d[i]["percentOfCapacity"])
            starttime = str(d[i]["tripStartOn"])
            currtime = str(d[i]["states"][0]["version"])
            direction = str(d[i]["states"][0]["direction"])
            speed = str(d[i]["states"][0]["speed"])
            latitude = str(d[i]["states"][0]["latitude"])
            longitude = str(d[i]["states"][0]["longitude"])
            atStop = str(d[i]["states"][0]["isBusAtStop"])
            

            if not Id: Id = "NULL"
            if not routeId: routeId = "NULL"
            if not stopId: stopId = "NULL"
            if not capacity: capacity = "NULL"
            if not percentOfCapacity: percentOfCapacity = "NULL"
            if not starttime: starttime = "NULL"
            if not currtime: currtime = "NULL"
            if not direction: direction = "NULL"
            if not speed: speed = "NULL"
            if not latitude: latitude = "NULL"
            if not longitude: longitude = "NULL"
            if not atStop: atStop = "NULL"

            query = "INSERT INTO BusData VALUES (" + Id + ",\""+ routeId + "\"," + capacity + "," + percentOfCapacity + "," + starttime + "," + currtime + "," + direction + "," + speed + "," + latitude + "," + longitude + ",\"" + atStop + "\"," + stopId +")"
            #print(query)
            cursor.execute(query)
            # result = cursor.fetchall()
            # print('{}'.format(result))

        # query = "SELECT * FROM BusData db"
        # cursor.execute(query)
        # result = cursor.fetchall()
        # print('{}'.format(result))
        print("Inserted " + str(len(d)) + " rows")

        cursor.execute(query)

        sqliteConnection.commit()
        scheduler.enter(1, 1, uploadToDB, argument=(cursor,))
        #cursor.close()

scheduler.enter(1, 1, uploadToDB, argument=(cursor,))

scheduler.run()
    # finally:
    #     if sqliteConnection:
    #         sqliteConnection.close()
    #         print('SQLite Connection closed')



