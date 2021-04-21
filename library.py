def function_input():
    st = input()
    if st == '': #blank line
        return 0,10000
    else:
        s = st.split() #s[0]:hh:mm:ss.fff  s[1]:distance(m)
        hour, minute, second = s[0].split(":")
        second, decimal = second.split(".")
        times = int(hour) * 3600000 + int(minute) * 60000 + int(second) * 1000 +int(decimal) #times[ms]
        temp = float(s[1])*10
        distance = int(temp) #distance[10cm]
        return times,distance

def payment(first_pay,low_times,add_distance,add_night_distance,add_low_times):
    low_pay = (low_times + add_low_times * 1.25) // 90000 #count low speed 
    add_pay = (add_distance + add_night_distance * 1.25) // 2370 #count add
    if (add_distance + add_night_distance * 1.25) % 2370 != 0:
        add_pay+=1
    credit = first_pay + (low_pay + add_pay) * 80 #sum credit
    print(low_pay)
    print(add_pay)
    print(credit)
    return 0

def countdistance(first_distance,before_distance,distance):
    dist = distance - before_distance
    return dist
