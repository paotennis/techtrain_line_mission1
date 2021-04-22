import library

first_pay = 410
add_low_times = 0
add_distance = 0
add_night_distance = 0
add_night_low_times = 0


if __name__ == "__main__":
    count = 0
    while 1:
        count+=1
        times,distance=library.function_input()
        if distance >= 10000:
            if count >= 3:
                if add_distance == 0:
                    print("-5")
                    exit(-5)
                add_distance -= 10520
                if add_distance < 0:
                    add_distance = 0
                library.payment(first_pay,add_low_times,add_distance,add_night_distance,add_night_low_times)
                exit(0)
            else:
                print("-1")
                exit(-1)
        if count == 1:
            before_times = times; before_distance = distance
            if distance != 0:
                print("-4")
                exit(-4)
        else:
            if times - before_times <= 0:
                print("-2")
                exit(-2)
            before_hour = before_times // 3600000; times_hour = times // 3600000
            if before_hour < 5 or 22 <= before_hour < 29 or 46 <= before_hour < 53 or 70 <= before_hour < 77 or 94 <= before_hour:
                if times_hour < 5 or 22 <= times_hour < 29 or 46 <= times_hour < 53 or 70 <= times_hour < 77 or 94 <= times_hour:
                    add_night_distance += library.countdistance(before_distance,distance)
                    add_night_low_times += library.countnightlowtime(before_distance,distance,before_times,times)
                    continue
            add_distance += library.countdistance(before_distance,distance)
            add_low_times += library.countlowtime(before_distance,distance,before_times,times)
            before_times = times; before_distance = distance