from datetime import datetime

def time_diff():
    current_time = datetime.now()
    with open('time.txt','r') as obj:
        line = obj.readline()

    prev_time = datetime(int(line[6:10]),int(line[3:5]),int(line[0:2]),int(line[12:14]),int(line[15:17]),int(line[18:20]))

    time_difference = current_time - prev_time

    if time_difference.days == 0:
        if time_difference.total_seconds()/60 < 720:
            duration = 720 - (time_difference.total_seconds()/60)
        else:
            duration = 720
    else:
        duration = 720
    
    return duration