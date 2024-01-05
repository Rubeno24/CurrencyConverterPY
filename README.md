Currency Converter App
This is a simple currency converter app built in Python using the Tkinter library. The app allows users to convert an amount from one currency to another based on the latest exchange rates obtained from the ExchangeRatesAPI.

Features
Converts currency from one selected option to another.
Displays the converted amount and currencies in a user-friendly format.
Supports popular currencies such as USD, MXN, EUR, GBP, JPY, AUD, CAD, CHF, CNY.
Validates user input to ensure it is a valid number.
Prerequisites
Python 3.x
Tkinter library
Requests library
Installation
Clone or download the repository.
Install the required libraries by running the following command:
bash
Copy code
pip install requests
Run the Python script:
bash
Copy code
python currency_converter.py
Usage
Enter the amount you want to convert in the "Amount" field.
Select the currency you want to convert from in the "From" dropdown menu.
Select the currency you want to convert to in the "To" dropdown menu.
Click the "Convert" button to calculate and display the converted amount.
Important Note
Ensure that you have an internet connection to fetch the latest exchange rates from the ExchangeRatesAPI.

API Information
The app uses the ExchangeRatesAPI to obtain the latest exchange rates. The API key used in the code is for demonstration purposes. If you plan to use this app frequently, consider obtaining your own API key from ExchangeRatesAPI.

Credits
ExchangeRatesAPI for providing free exchange rate data.
Feel free to customize and enhance the app based on your needs. Happy coding!
