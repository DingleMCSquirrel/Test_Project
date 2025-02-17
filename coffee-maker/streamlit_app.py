import streamlit as st
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of the classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Page title
st.title("Coffee Maker")

# Display the menu items
st.header("Menu")
options = menu.get_items()

# Let the user enter the coffee choice
choice = st.text_input("Enter the coffee you would like to order:")

# Handle the order submission
if choice:
    drink = menu.find_drink(choice)
    if drink and coffee_maker.is_resource_sufficient(drink)[0] and money_machine.make_payment(drink.cost, {}):
        coffee_maker.make_coffee(drink)
        st.write(f"☕ Enjoy your {choice}!")
    else:
        st.write("❌ Not enough resources or payment failed.")

# Display the current resources and cash
if st.button("Show Report"):
    st.write(f"### Resources Report")
    st.text(coffee_maker.report())
    st.write(money_machine.report())
