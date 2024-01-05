# Currency Converter App

This is a simple currency converter app built in Python using the Tkinter library. The app allows users to convert an amount from one currency to another based on the latest exchange rates obtained from the [ExchangeRatesAPI](http://api.exchangeratesapi.io/).

## Features
- Converts currency from one selected option to another.
- Displays the converted amount and currencies in a user-friendly format.
- Supports popular currencies such as USD, MXN, EUR, GBP, JPY, AUD, CAD, CHF, CNY.
- Validates user input to ensure it is a valid number.

## Prerequisites
- Python 3.x
- Tkinter library
- Requests library

## Installation
1. Clone or download the repository.
2. Install the required libraries by running the following command:
    ```bash
    pip install requests
    ```
3. Run the Python script:
    ```bash
    python currency_converter.py
    ```

## Usage
1. Enter the amount you want to convert in the "Amount" field.
2. Select the currency you want to convert from in the "From" dropdown menu.
3. Select the currency you want to convert to in the "To" dropdown menu.
4. Click the "Convert" button to calculate and display the converted amount.

## Important Note
Ensure that you have an internet connection to fetch the latest exchange rates from the [ExchangeRatesAPI](http://api.exchangeratesapi.io/).

## API Information
The app uses the ExchangeRatesAPI to obtain the latest exchange rates. The API key used in the code is for demonstration purposes. If you plan to use this app frequently, consider obtaining your own API key from [ExchangeRatesAPI](http://api.exchangeratesapi.io/).

## Credits
- [ExchangeRatesAPI](http://api.exchangeratesapi.io/) for providing free exchange rate data.

Feel free to customize and enhance the app based on your needs. Happy coding!
