import csv
import random
import time
import pyfiglet
import colored
import datetime


# print ("Today's date:  = %s-%s-%s" % (e.day, e.month, e.year))

# print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))


W = '\033[0m'
R = '\033[31m'


total_1 = 1000
total_2 = 1000
total_3 = 1000

spliter = "-------------------------------------------------------------------------"


def ban():
    print(f"""{colored.stylize(pyfiglet.figlet_format("sensor data (live)"), colored.fg(28))}
{spliter}""" + W)


ban()

print(R + " "*5, "Date", " "*14, "Temp", " "*5, "Hum", " "*4, "Gas", " "*4 + W)
print('')

field_names = ["Date", "price", "humidity", "Gas"]

id = 0

with open("data.csv", 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
    csv_writer.writeheader()

while True:

    e = datetime.datetime.now()

    a = e.strftime("%H%M%S")

    a = int(a)

    id += 1
    
    with open("data.csv", 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)

        x_value = a

        

        info = {
            "Date": id,
            "price": total_1,
            "humidity": total_2,
            "Gas": total_3
        }

        csv_writer.writerow(info)
        print(x_value, " "*5, total_1, " "*5, total_2, " "*3, total_3)

        # x_value += 1
        total_1 = total_1 + random.randint(-6, 8)
        total_2 = total_2 + random.randint(-5, 6)
        total_3 = total_3 + random.randint(-4, 10)

        

    time.sleep(1)
    
