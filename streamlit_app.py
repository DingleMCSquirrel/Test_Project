import streamlit as st

# Title of the application
st.title("Basic Calculator")

# Get user input for two numbers
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)

# Display operation buttons
operation = st.selectbox("Select an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform the calculation based on selected operation
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."

# Display the result
st.write("Result: ", result)
