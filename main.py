import library

first_pay = 410


if __name__ == "__main__":
    count = 0
    while 1:
        count+=1
        times,distance=library.function_input()
        if distance >= 10000:
            if count >= 3:
                library.payment(first_pay,low_times,add_distance,add_night_distance,add_low_times)
                return 0
            else:
                return -1
        if count == 1:
            before_times = times; before_distance = distance
            first_times = times; first_distance = distance
        else:
            library.countdistance(first_distance,before_distance,distance)
        print(times,distance)