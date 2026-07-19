d=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
d2={
    'Monday':1,
    'Tuesday':2,
    'Wednesday':3,
    'Thursday':4,
    'Friday':5,
    'Saturday':6,
    'Sunday':7
}
def day_from_number(day_number):
    if day_number>7 or day_number<1:
        return None
    return d[day_number-1]

def day_to_number(day):
    if day not in d:
        return None
    return d2[day]


