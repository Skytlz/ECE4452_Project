import json
import sqlite3
import json
from datetime import datetime, timedelta

try: 
        sqliteConnection = sqlite3.connect('BusData.db')
        cursor = sqliteConnection.cursor()
        print('DB Init')

except sqlite3.Error as error:
        print('Error occurred - ', error)
        

hdg_route1 = {
    "1511": "07:00:00",
    "1512": "07:00:00",
    "1513": "07:01:00",
    "1514": "07:01:00",
    "1515": "07:01:00",
    "1516": "07:01:00",
    "1517": "07:02:00",
    "1518": "07:03:00",
    "1519": "07:03:00",
    "1520": "07:03:00",
    "1521": "07:04:00",
    "1628": "07:05:00",
    "1441": "07:05:00",
    "1431": "07:05:00",
    "8003": "07:06:00"
}

# initial_times = {stop: datetime.strptime(time, "%H:%M:%S") for stop, time in hdg_route1.items()}

# start_time = datetime.strptime("07:00:00", "%H:%M:%S")
# end_time = datetime.strptime("18:30:00", "%H:%M:%S")
# time_increment = timedelta(minutes=15)

# extended_times1 = []
# current_time = start_time

# while current_time <= end_time:
#     for stop, time in initial_times.items():
#         adjusted_time = time + (current_time - start_time)
#         if adjusted_time.time() <= end_time.time():
#             extended_times1.append((stop, adjusted_time.strftime("%H:%M:%S")))
#     current_time += time_increment

# query = str()
# for stop, time in extended_times1:
#     #print(f"{stop} {time}")
#     query = f"INSERT INTO ScheduledTimes VALUES(\"HDG\",{stop},\"{time}\")"
#     #print(query)
#     cursor.execute(query)
# sqliteConnection.commit()

# hdg_route_late1 = {
#     "1511": "19:00:00",
#     "1512": "19:00:00",
#     "1513": "19:01:00",
#     "1514": "19:01:00",
#     "1515": "19:01:00",
#     "1516": "19:01:00",
#     "1517": "19:02:00",
#     "1518": "19:03:00",
#     "1519": "19:03:00",
#     "1520": "19:03:00",
#     "1521": "19:04:00",
#     "1628": "19:05:00",
#     "1441": "19:05:00",
#     "1431": "19:05:00",
#     "8003": "19:06:00"
    
# }

# initial_times = {stop: datetime.strptime(time, "%H:%M:%S") for stop, time in hdg_route_late1.items()}

# start_time = datetime.strptime("19:00:00", "%H:%M:%S")
# end_time = datetime.strptime("23:59:00", "%H:%M:%S")
# time_increment = timedelta(minutes=30)

# extended_times1 = []
# current_time = start_time

# while current_time <= end_time:
#     for stop, time in initial_times.items():
#         adjusted_time = time + (current_time - start_time)
#         if adjusted_time.time() <= end_time.time():
#             extended_times1.append((stop, adjusted_time.strftime("%H:%M:%S")))
#     current_time += time_increment

# query = str()
# for stop, time in extended_times1:
#     #print(f"{stop} {time}")
#     query = f"INSERT INTO ScheduledTimes VALUES(\"HDG\",{stop},\"{time}\")"
#     #print(query)
#     cursor.execute(query)
# sqliteConnection.commit()

# hdg_route_late1 = {
#     "1511": "00:00:00",
#     "1512": "00:00:00",
#     "1513": "00:01:00",
#     "1514": "00:01:00",
#     "1515": "00:01:00",
#     "1516": "00:01:00",
#     "1517": "00:02:00",
#     "1518": "00:03:00",
#     "1500": "00:03:00",
#     "1520": "00:03:00",
#     "1521": "00:04:00",
#     "1628": "00:05:00",
#     "1441": "00:05:00",
#     "1431": "00:05:00",
#     "8003": "00:06:00"
# }

# initial_times = {stop: datetime.strptime(time, "%H:%M:%S") for stop, time in hdg_route_late1.items()}

# start_time = datetime.strptime("00:00:00", "%H:%M:%S")
# end_time = datetime.strptime("00:30:00", "%H:%M:%S")
# time_increment = timedelta(minutes=30)

# extended_times1 = []
# current_time = start_time

# while current_time <= end_time:
#     for stop, time in initial_times.items():
#         adjusted_time = time + (current_time - start_time)
#         if adjusted_time.time() <= end_time.time():
#             extended_times1.append((stop, adjusted_time.strftime("%H:%M:%S")))
#     current_time += time_increment

# query = str()
# for stop, time in extended_times1:
#     #print(f"{stop} {time}")
#     query = f"INSERT INTO ScheduledTimes VALUES(\"HDG\",{stop},\"{time}\")"
#     #print(query)
#     cursor.execute(query)
# sqliteConnection.commit()



hdg_route2 = {
    "1511": "07:15:00",
    "1512": "07:15:00",
    "1513": "07:16:00",
    "1514": "07:16:00",
    "1515": "07:16:00",
    "1516": "07:17:00",
    "1517": "07:18:00",
    "1518": "07:19:00",
    "1519": "07:19:00",
    "1520": "07:19:00",
    "1521": "07:20:00",
    "1628": "07:21:00",
    "1441": "07:21:00",
    "1431": "07:21:00",
    "8003": "07:22:00"
}

# hdg_route3 = {
#     "8003": "07:15:00",
#     "1334": "07:16:00",
#     "1422": "07:17:00",
#     "1440": "07:17:00",
#     "1600": "07:18:00",
#     "1500": "07:19:00",
#     "1501": "07:19:00",
#     "1502": "07:19:00",
#     "1503": "07:20:00",
#     "1504": "07:21:00",
#     "1505": "07:21:00",
#     "1506": "07:22:00",
#     "1507": "07:22:00",
#     "1508": "07:22:00",
#     "1509": "07:22:00",
#     "1510": "07:23:00"
# }

# initial_times = {stop: datetime.strptime(time, "%H:%M:%S") for stop, time in hdg_route3.items()}

# start_time = datetime.strptime("07:15:00", "%H:%M:%S")
# end_time = datetime.strptime("18:15:00", "%H:%M:%S")
# time_increment = timedelta(minutes=15)

# extended_times1 = []
# current_time = start_time

# while current_time <= end_time:
#     for stop, time in initial_times.items():
#         adjusted_time = time + (current_time - start_time)
#         if adjusted_time.time() <= end_time.time():
#             extended_times1.append((stop, adjusted_time.strftime("%H:%M:%S")))
#     current_time += time_increment

# query = str()
# for stop, time in extended_times1:
#     #print(f"{stop} {time}")
#     query = f"INSERT INTO ScheduledTimes VALUES(\"HDG\",{stop},\"{time}\")"
#     #print(query)
#     cursor.execute(query)
# sqliteConnection.commit()

hdg_route_late3 = {
    "8003": "00:15:00",
    "1334": "00:16:00",
    "1422": "00:17:00",
    "1440": "00:17:00",
    "1600": "00:18:00",
    "1500": "00:19:00",
    "1501": "00:19:00",
    "1502": "00:19:00",
    "1503": "00:20:00",
    "1504": "00:21:00",
    "1505": "00:21:00",
    "1506": "00:22:00",
    "1507": "00:22:00",
    "1508": "00:22:00",
    "1509": "00:22:00",
    "1510": "00:23:00"
}

initial_times = {stop: datetime.strptime(time, "%H:%M:%S") for stop, time in hdg_route_late3.items()}

start_time = datetime.strptime("00:15:00", "%H:%M:%S")
end_time = datetime.strptime("00:30:00", "%H:%M:%S")
time_increment = timedelta(minutes=30)

extended_times1 = []
current_time = start_time

while current_time <= end_time:
    for stop, time in initial_times.items():
        adjusted_time = time + (current_time - start_time)
        if adjusted_time.time() <= end_time.time():
            extended_times1.append((stop, adjusted_time.strftime("%H:%M:%S")))
    current_time += time_increment

query = str()
for stop, time in extended_times1:
    #print(f"{stop} {time}")
    query = f"INSERT INTO ScheduledTimes VALUES(\"HDG\",{stop},\"{time}\")"
    #print(query)
    cursor.execute(query)
sqliteConnection.commit()




# initial_times = {stop: datetime.strptime(time, "%H:%M:%S") for stop, time in hdg_route1.items()}

# start_time = datetime.strptime("07:00:00", "%H:%M:%S")
# end_time = datetime.strptime("18:30:00", "%H:%M:%S")
# time_increment = timedelta(minutes=15)

# extended_times1 = []
# current_time = start_time

# while current_time <= end_time:
#     for stop, time in initial_times.items():
#         adjusted_time = time + (current_time - start_time)
#         if adjusted_time.time() <= end_time.time():
#             extended_times1.append((stop, adjusted_time.strftime("%H:%M:%S")))
#     current_time += time_increment

# query = str()
# for stop, time in extended_times1:
#     query = f"INSERT INTO ScheduledTimes VALUES(\"HDG\",{stop},\"{time}\")"
#     print(query)
#     cursor.execute(query)
# sqliteConnection.commit()

# if sqliteConnection:
#     sqliteConnection.close()
#     print('SQLite Connection closed')


# initial_times = {stop: datetime.strptime(time, "%H:%M:%S") for stop, time in hdg_route3.items()}

# start_time = datetime.strptime("07:00:00", "%H:%M:%S")
# end_time = datetime.strptime("18:15:00", "%H:%M:%S")
# time_increment = timedelta(minutes=15)


# extended_times2 = []
# current_time = start_time

# while current_time <= end_time:
#     for stop, time in initial_times.items():
#         adjusted_time = time + (current_time - start_time)
#         if adjusted_time.time() <= end_time.time():
#             extended_times2.append((stop, adjusted_time.strftime("%H:%M:%S")))
#     current_time += time_increment

# # Output the list of tuples
# for stop, time in extended_times2:
#     query = f"INSERT INTO ScheduledTimes VALUES(\"HDG\",{stop},\"{time}\")"
#     cursor.execute(query)

# sqliteConnection.commit()

# if sqliteConnection:
#     sqliteConnection.close()
#     print('SQLite Connection closed')



if sqliteConnection:
    sqliteConnection.close()
    print('SQLite Connection closed')