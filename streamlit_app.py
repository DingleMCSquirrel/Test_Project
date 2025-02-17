import streamlit as st
import pandas as pd
import io

def convert_xlsx_to_csv(xlsx_file):
    # Read the uploaded Excel file
    df = pd.read_excel(xlsx_file)
    
    # Convert to CSV format in-memory
    csv_data = df.to_csv(index=False)
    
    # Return the CSV data as a byte stream
    return io.BytesIO(csv_data.encode())

def main():
    st.title("XLSX to CSV Converter")

    # Step 1: Upload .xlsx file
    uploaded_file = st.file_uploader("Choose an XLSX file", type="xlsx")
    
    if uploaded_file is not None:
        # Step 2: Convert the uploaded XLSX file to CSV
        converted_csv = convert_xlsx_to_csv(uploaded_file)
        
        # Step 3: Provide the option to download the converted CSV
        st.download_button(
            label="Download CSV",
            data=converted_csv,
            file_name="converted_file.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()
