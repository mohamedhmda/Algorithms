def total_max_speed(blue_drivers, red_drivers):
    num_of_driver = len(blue_drivers)
    total_max_speed = 0
    for n in range(num_of_driver):
        total_max_speed += max(blue_drivers[n], red_drivers[num_of_driver - n - 1])
    return total_max_speed

def total_min_speed(blue_drivers, red_drivers):
    num_of_driver = len(blue_drivers)
    total_min_speed = 0
    for n in range(num_of_driver):
        total_min_speed += max(blue_drivers[n], red_drivers[n])
    return total_min_speed

def tandem_bicycle(blue_drivers, red_drivers, fastest):
    if len(blue_drivers) != len(red_drivers):
        return False
    blue_drivers.sort()
    red_drivers.sort()
    
    if fastest:
        return total_max_speed(blue_drivers, red_drivers)
    else:
        return total_min_speed(blue_drivers, red_drivers)