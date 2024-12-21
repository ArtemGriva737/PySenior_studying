import requests
from bs4 import BeautifulSoup
import sqlite3
import logging

logging.basicConfig(
    filename='weather_date.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DateWeather:
    def __init__(self, db_name='weather_data.db'):
        self.db_name = db_name

    def give_data(self):
        global cursor, connection
        try:
            logging.info("Завантаження даних із сайту.")
            data_site = requests.get('https://www.pogodairadar.com/stranitsa-pogodyi/dnepr/4441971')

            if data_site.status_code == 200:
                soup = BeautifulSoup(data_site.text, features="html.parser")
                soup_time_date = soup.find('div', {'class': 'name-col'})
                soup_temperature = soup.find('div', {'class': 'current-conditions-line'})
                soup_opadi = soup.find('span', {'class': 'divider-text blue-text'})
                soup_wind = soup.find('div', {'class': 'table'})

                if soup_time_date and soup_temperature and soup_opadi and soup_wind:
                    time_date_text = soup_time_date.get_text(strip=True)
                    temperature_text = soup_temperature.get_text(strip=True)
                    opadi_text = soup_opadi.get_text(strip=True)
                    wind_text = soup_wind.get_text(strip=True)

                    print(f"Дата і час: {time_date_text}"
                          f"Температура: {temperature_text}"
                          f"Опади: {opadi_text}"
                          f"Швидкість та напрямок вітру: {wind_text}")

                    try:
                        logging.info("Підключення до бази даних SQLite.")
                        connection = sqlite3.connect(self.db_name)
                        cursor = connection.cursor()

                        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS weather (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            time_date TEXT NOT NULL,
                            temperature TEXT NOT NULL,
                            opadi TEXT NOT NULL,
                            wind TEXT NOT NULL
                        )
                        ''')

                        cursor.execute('''
                        INSERT INTO weather (time_date, temperature, opadi, wind) 
                        VALUES (?, ?, ?, ?)
                        ''', (time_date_text, temperature_text, opadi_text, wind_text))

                        connection.commit()
                        logging.info("Дані успішно збережено в базу даних.")
                        print("Дані успішно збережено в базу даних.\n")
                    except sqlite3.Error as e:
                        logging.error(f"Помилка при роботі з базою даних: {e}")
                        print(f"Помилка при роботі з базою даних: {e}\n")
                    finally:
                        if cursor:
                            cursor.close()
                            logging.info("Курсор успішно закрито.")
                        if connection:
                            connection.close()
                            logging.info("Підключення до бази даних успішно закрито.")
                else:
                    logging.warning("Не вдалося знайти потрібні дані на сайті.")
                    print("Не вдалося знайти дані на сайті.")
            else:
                logging.error(f"Помилка підключення до сайту: {data_site.status_code}")
                print(f"Помилка підключення до сайту: {data_site.status_code}")
        except Exception as e:
            logging.error(f"Непередбачена помилка: {e}")
            print(f"Непередбачена помилка: {e}")

    def get_data_SQLite3(self, date):
        global cursor, connection
        try:
            logging.info(f"Вибірка даних із бази даних за датою: {date}")
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            cursor.execute('''
            SELECT time_date, temperature, opadi, wind 
            FROM weather
            WHERE time_date LIKE ?
            ''', (f"%{date}%",))

            rows = cursor.fetchall()
            if rows:
                print(f"Дані за датою {date}:\n")
                for row in rows:
                    print(f"Дата і час: {row[0]}\n"
                          f"Температура: {row[1]}\n"
                          f"Опади: {row[2]}\n"
                          f"Швидкість вітру: {row[3]}\n")
            else:
                print(f"Дані за датою {date} відсутні.\n")
        except sqlite3.Error as e:
            logging.error(f"Помилка при вибірці даних із бази: {e}")
            print(f"Помилка при вибірці даних із бази: {e}\n")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

if __name__ == "__main__":
    weather = DateWeather()
    weather.give_data()
    query_date = "25.11, 20:00"
    weather.get_data_SQLite3(query_date)

