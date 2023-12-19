from pathlib import Path
from tkinter import Label, OptionMenu, StringVar, Text, Tk, Canvas, Entry, Button, PhotoImage, messagebox
import requests

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"  # Assuming images are in the "assets" directory

# Specify the API endpoint URL
api_url = "http://api.exchangeratesapi.io/v1/latest?access_key=a576ac8b9d1a1facf132dcb24e42b07b"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Make a GET request to the API endpoint
response = requests.get(api_url)
data = response.json()
# store the json file into a dict named rates
rates = data.get("rates", {})

# create an empty list named all_exchange_rates
all_exchange_rates = []



# itterate through rates and assign the first value as currencyName and the second value as rate and append it to the list named all_exchange_rates
for x, y in rates.items():
    all_exchange_rates.append({"currencyName": x, "rate": y})


# created a list of popular currencies, if you want to add a currecny to the converter add it to this list and make sure its 
# included with the api 
popular_currencies = ["USD", "MXN", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY"]

# loop through all_exchange_rates and store a dictionary into currency_info
# use an if statement to check if currencyName field is in popular_currencies
# if it is store that inside filtered_exchange_rates list
filtered_exchange_rates = []
for currency_info in all_exchange_rates:
    if currency_info["currencyName"] in popular_currencies:
        filtered_exchange_rates.append(currency_info)


# make a list named options and loop through each value filtered_exchange_rates and assign that to x and name that currencyName
options = [x["currencyName"] for x in filtered_exchange_rates]

# create a window object
window = Tk()
window.title("Currency Converter")


# set the window height and length and make the background white
window.geometry("350x350")
window.configure(bg="#FFFFFF")

# Set the window size
window_width = 350
window_height = 350

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2

window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate-200}")


# creating a canvas same size and color as the window
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=550,
    width=750,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

# method name ButtonClicked called when styled_button is clicked
def ButtonClicked():
    try:
        # Try to convert the entered text to a float
        float_value = float(entry.get())
    except ValueError:
        # If the conversion fails, show an error message
        messagebox.showerror("Error", "Invalid input. Please enter a number.")

    # two variables that store the selected option from 2 drop down menus that have currecy names 
    from_currency = selected_option.get()
    to_currency = selected_option1.get()

    # Find the exchange rate for the selected currencies
    
    for item in filtered_exchange_rates:
        if item["currencyName"] == from_currency:
            from_exchange_rate = item["rate"]
            break
    

    for x in  filtered_exchange_rates:
        if x['currencyName']==to_currency:
            to_exchange_rate = x["rate"]
            break

    # Calculate the converted amount
    converted_amount = float_value * (to_exchange_rate / from_exchange_rate)

    print(f"{float_value} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    

    label.config(text=f"{float_value:,.2f} {from_currency}\n is equal to\n{converted_amount:,.2f} {to_currency}")

    

def on_menu_selection(value, dropdown_identifier):
    print(f"Selected value from {dropdown_identifier} dropdown: {value}")

button_style = {
    'text': "Convert",
    'bg': "#4CAF50",  # Background color (green)
    'fg': "#FFFFFF",  # Foreground color (white)
    'font': ('Helvetica', 12),
    'width': 10,
    'height': 2,
    'command': ButtonClicked
}

# Create a text entry for the user to input an amount
entry_label = Label(window, text="Amount:")
entry_label.grid(row=0, column=1, padx=10, pady=10)

# creating a text entry
entry = Entry(window, width=30)
entry.grid(row=0, column=2, padx=10, pady=10)

# create a varaible of type StringVar and sets the default value to USD
selected_option = StringVar(window)
selected_option.set("USD")

# creates the first drop down menu with the most popular currencies store in options
dropdown_menu_label = Label(window, text="From:")
dropdown_menu_label.grid(row=2, column=1, padx=10, pady=10)

dropdown_menu = OptionMenu(window, selected_option, *options, command=lambda value: on_menu_selection(value, "first"))
dropdown_menu.grid(row=2, column=2, padx=10, pady=10, columnspan=1,)


# create a varaible of type StringVar and sets the default value to MXN
selected_option1 = StringVar(window)
selected_option1.set("MXN")

# Create a text entry for the user to input an amount
entry_label1 = Label(window, text="To:")
entry_label1.grid(row=3, column=1, padx=10, pady=10)

# creates the second drop down menu with the most popular currencies store in options
dropdown_menu1 = OptionMenu(window, selected_option1, *options, command=lambda value: on_menu_selection(value, "second"))
dropdown_menu1.grid(row=3, column=2, padx=10, pady=10, columnspan=1,)


# create a button named styler_button and adds some styles to it
styled_button = Button(window, **button_style)
styled_button.grid(row=4, column=2, padx=10, pady=10, columnspan=1, )

# blank label that will be updated with the converted currency in the ButtonClicked function
label = Label(window, text="",font=('Helvetica', 10))
label.grid(row=5, column=2, padx=0, pady=10)



canvas.place(x=0, y=0)





window.resizable(True, True)
window.mainloop()
