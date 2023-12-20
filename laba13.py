#12.	Определить количество пассажиров на борту в возрастном интервале мода  5 лет и сколько из них выжило
import pandas as pd

# Загрузка данных из файла CSV
data = pd.read_csv('titanic.csv')

# Выборка только необходимых столбцов: Выжил и Возраст
selected_columns = ['Survived', 'Age']
filtered_data = data[selected_columns]

# Очистка данных от пропущенных значений
filtered_data = filtered_data.dropna()

# Вычисление моды возраста
mode_age = filtered_data['Age'].mode()[0]

# Определение возрастного интервала моды ± 5 лет
lower_limit = mode_age - 5
upper_limit = mode_age + 5

# Фильтрация данных по возрастному интервалу
age_filtered_data = filtered_data[(filtered_data['Age'] >= lower_limit) & (filtered_data['Age'] <= upper_limit)]

# Вычисление количества пассажиров в возрастном интервале
passengers_count = len(age_filtered_data)

# Вычисление количества выживших пассажиров в возрастном интервале
survived_count = age_filtered_data['Survived'].sum()

print("Мода: ", mode_age)
print("Количество пассажиров в возрастном интервале моды ± 5 лет:", passengers_count)
print("Количество выживших пассажиров в возрастном интервале моды ± 5 лет:", survived_count)