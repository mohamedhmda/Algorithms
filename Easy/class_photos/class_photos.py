def height_verification(front_row, back_row):
    for i in range(len(front_row)):
        if front_row[i] > back_row[i]:
            return False
    return True

def class_photos(red_row, blue_row):
    if len(red_row) != len(blue_row):
        return False
    red_row.sort()
    blue_row.sort()
    if red_row[0] <= blue_row[0]:
        return height_verification(red_row, blue_row)
    else:
        return height_verification(blue_row, red_row)
