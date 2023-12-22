#12.	Определить количество пассажиров на борту в возрастном интервале мода  5 лет и сколько из них выжило
import csv
from statistics import mode

with open('titanic.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)

    age_intervals = {}

    for row in reader:
        age = float(row[4])

        age_interval = int(age // 5) * 5
        print(age, " - ", age_interval)

        if age_interval in age_intervals:
            age_intervals[age_interval]['passengers'] += 1

            if int(row[0]) == 1:
                age_intervals[age_interval]['survived'] += 1
        else:
            age_intervals[age_interval] = {'passengers': 1, 'survived': int(row[0])}

age_mode = mode(age_intervals.keys())

passengers_in_mode_interval = age_intervals[age_mode]['passengers']
survived_in_mode_interval = age_intervals[age_mode]['survived']

print("Мода: ", age_mode)
print("Количество пассажиров в возрастном интервале моды ± 5 лет:", passengers_in_mode_interval)
print("Количество выживших в данном интервале:", survived_in_mode_interval)
