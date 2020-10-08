#Week 4 Python Exercises for I2P Forum

#Exercise No.1

def convert_to_days():
    hours , minutes , seconds = input("Enter hours: ") , input("Enter minutes: ") , input("Enter seconds: ")
    hours , minutes , seconds = int(hours), int(minutes), int(seconds)
    return get_days(hours , minutes , seconds)

def get_days(hours, minutes , seconds):
    total_seconds_in_day = 86400
    hours , minutes  = hours*3600 , minutes*60 
    total_user = hours + minutes + seconds
    number_of_day = total_user/total_seconds_in_day
    return round(number_of_day, 4)

print("The number of days is:", convert_to_days())


