def BusIDChoice(busName):
    return f"""SELECT DISTINCT BusID
FROM BusData bd 
WHERE BusName = "{busName}"
"""

def busStops(busName, busID):
    return f"""SELECT BusId, BusName, speed, direction, TIME(DATETIME(starttime / 1000, 'unixepoch', 'localtime')) AS starttime, TIME(DATETIME(currtime / 1000, 'unixepoch', 'localtime')) AS currtime, AtBusStop, stopID 
FROM BusData bd
WHERE BusName == "{busName}"
AND BusID == "{busID}"
GROUP BY stopID
ORDER BY currtime 
"""