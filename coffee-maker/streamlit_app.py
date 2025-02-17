import streamlit as st
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of the classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Streamlit UI setup
st.title("Coffee Maker Machine")

# Display menu items
options = menu.get_items()
choice = st.selectbox("What would you like?", options)

# Button for ordering
if st.button("Order Coffee"):
    if choice == "report":
        st.text(coffee_maker.report())
        st.text(money_machine.report())
    else:
        drink = menu.find_drink(choice)
        if drink and coffee_maker.is_resource_sufficient(drink):
            coin_data = {
                "quarters": st.number_input("How many quarters?", min_value=0),
                "dimes": st.number_input("How many dimes?", min_value=0),
                "nickles": st.number_input("How many nickles?", min_value=0),
                "pennies": st.number_input("How many pennies?", min_value=0)
            }
            payment_successful, change = money_machine.make_payment(drink.cost, coin_data)
            if payment_successful:
                coffee_maker.make_coffee(drink)
                st.success(f"Enjoy your {choice}! Change: ${change}")
            else:
                st.error("Not enough money!")
        else:
            st.error("Not enough resources to make this drink!")
