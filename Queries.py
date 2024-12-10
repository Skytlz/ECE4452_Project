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

def BusTimes(busName):
    return f"""WITH StopOccurrences AS (
    SELECT 
        BusID,
        BusName,
        speed,
        direction,
        TIME(DATETIME(starttime / 1000, 'unixepoch', 'localtime')) AS starttime,
        TIME(DATETIME(currtime / 1000, 'unixepoch', 'localtime')) AS currtime,
        AtBusStop,
        stopID,
        ROW_NUMBER() OVER (
            PARTITION BY stopID, DATE(DATETIME(currtime / 1000, 'unixepoch', 'localtime')) 
            ORDER BY currtime
        ) AS RowNum
    FROM 
        BusData
    WHERE 
        BusName = "{busName}"
        --AND BusID = "6401"
        AND AtBusStop = "Y" -- Assuming 'AtBusStop' indicates the bus is at the stop
)
SELECT 
    BusID,
    BusName,
    speed,
    direction,
    starttime,
    currtime,
    AtBusStop,
    stopID
FROM 
    StopOccurrences
WHERE 
    RowNum = 1;
"""

def scheduledTimes(busName):
    return f"""SELECT *
    FROM ScheduledTimes st
    WHERE BusName = "{busName}"
    """