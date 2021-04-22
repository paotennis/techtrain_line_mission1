import re

def function_input():
    st = input()
    if st == '': #blank line
        return 0,10000
    if re.search('^\d{2}:\d{2}:\d{2}.\d{3}',st) == None:
        print("時間の入力形式エラー")
        exit(-3)
    else:
        s = st.split() #s[0]:hh:mm:ss.fff  s[1]:distance(m)
        hour, minute, second = s[0].split(":")
        second, decimal = second.split(".")
        times = int(hour) * 3600000 + int(minute) * 60000 + int(second) * 1000 +int(decimal) #times[ms]
        temp = float(s[1])*10
        distance = int(temp) #distance[10cm]
        if distance >= 1000:
            print("距離の入力形式エラー")
            exit(-6)
        return times,distance

def payment(first_pay,low_times,add_distance,add_night_distance,add_low_times):
    low_pay = low_times + add_low_times #count low speed 
    add_pay = (add_distance // 2370) + (add_night_distance * 1.25) // 2370 #count add
    if (add_distance + add_night_distance * 1.25) % 2370 != 0:
        add_pay+=1
    credit = first_pay + (low_pay + add_pay) * 80 #sum credit
    print(credit)
    return 0

def countdistance(before_distance,distance):
    dist = distance - before_distance #distance calculation
    return dist

def countlowtime(before_distance,distance,before_times,times):
    dist = distance - before_distance #distance calculation
    tim = times - before_times #time calculation
    speed = ((dist * 100 / tim)*3.6) # speed calculation [km/h]
    if speed <= 10.0:
        return tim // 90000
    else:
        return 0

def countnightlowtime(before_distance,distance,before_times,times):
    dist = distance - before_distance
    tim = times - before_times
    speed = ((dist * 100 / tim)*3.6)
    if speed <= 10.0:
        return tim * 1.25 // 90000
    else:
        return 0