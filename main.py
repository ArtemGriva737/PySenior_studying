import requests
from bs4 import BeautifulSoup
import tkinter as tk


class CurrencyConverter:
    def __init__(self):
        self.dollar_rate = self.get_dollar()

    def get_dollar(self):
        try:
            data_site = requests.get('https://bank.gov.ua/')
            print('site bank.gov.ua status code', data_site.status_code)

            if data_site.status_code == 200:
                print('bank.gov.ua is connected')
                soup = BeautifulSoup(data_site.text, features="html.parser")

                soup_dollar = soup.find_all('div', {'class': 'value index-page'})
                if soup_dollar[3]:
                    dollar_text = soup_dollar[3].get_text(strip=True).replace(',', '.')
                    print(f"Курс долара: {dollar_text}")
                    return float(dollar_text)
        except Exception as e:
            print(f"Помилка: {e}")
            return None

    def convert_to_dollar(self, amount):
        if self.dollar_rate is None:
            return "Не вдалося отримати курс долара."
        return amount / self.dollar_rate


def create_gui():
    converter = CurrencyConverter()

    def convert_currency():
        try:
            amount = float(entry_amount.get())
            dollar_amount = converter.convert_to_dollar(amount)
            if isinstance(dollar_amount, str):
                result_label.config(text=dollar_amount)
            else:
                result_label.config(text=f"Сума в USD: {dollar_amount:.2f}")
        except ValueError:
            result_label.config(text="Будь ласка, введіть коректне число.")

    window = tk.Tk()
    window.title("Конвертер Валюти")

    tk.Label(window, text="Сума у гривнях:").grid(row=0, column=0, padx=10, pady=10)
    entry_amount = tk.Entry(window)
    entry_amount.grid(row=0, column=1, padx=10, pady=10)

    convert_button = tk.Button(window, text="Конвертувати", command=convert_currency)
    convert_button.grid(row=1, column=0, columnspan=2, pady=10)

    result_label = tk.Label(window, text="")
    result_label.grid(row=2, column=0, columnspan=2, pady=10)

    window.mainloop()


if __name__ == "__main__":
    create_gui()


