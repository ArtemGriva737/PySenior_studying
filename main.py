import requests
from bs4 import BeautifulSoup
import sqlite3
import time


def give_data():
        data_site = requests.get('https://www.pogodairadar.com/stranitsa-pogodyi/dnepr/4441971')
        if data_site.status_code == 200:
            soup = BeautifulSoup(data_site.text, features="html.parser")
            soup_temperature = soup.find('div', {'class': 'current-conditions-line'})
            soup_time_date = soup.find('div', {'class': 'name-col'})

            if soup_temperature and soup_time_date:
                temperature_text = soup_temperature.get_text(strip=True)
                time_date_text = soup_time_date.get_text(strip=True)

                print(f"Температура у Дніпрі: {temperature_text}")
                print(f"Дата і час: {time_date_text}")

                connection = sqlite3.connect('weather_data.db')
                cursor = connection.cursor()

                cursor.execute('''
                CREATE TABLE IF NOT EXISTS weather (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    temperature TEXT NOT NULL,
                    time_date TEXT NOT NULL
                )
                ''')

                cursor.execute('''
                INSERT INTO weather (temperature, time_date) 
                VALUES (?, ?)
                ''', (temperature_text, time_date_text))

                connection.commit()
                print("Дані успішно збережено в базу даних.")

                cursor.close()
                connection.close()
            else:
                print("Не вдалося знайти дані на сайті.")

def main():
    while True:
        give_data()
        print("\nОчікування 30 хвилин...")
        time.sleep(1800)


if __name__ == "__main__":
    main()

