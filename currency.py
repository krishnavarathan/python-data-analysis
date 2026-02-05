import streamlit as st
import requests

base_url = "https://api.frankfurter.dev/v1"
st.title("💱 Currency Converter")

date = st.text_input(
    "Enter date (YYYY-MM-DD) or type 'latest'",
    value="latest"
)
base = st.text_input("Convert from (currency)", value="EUR")
curr = st.text_input("Convert to (currency)", value="USD")
amt = st.number_input(f"How much {base} would you like to convert?", min_value=0)

if st.button("Convert"):
    url = f"{base_url}/{date}?base={base}&symbols={curr}"
    response = requests.get(url)

    if not response.ok:
        st.error(f"Error {response.status_code}: {response.json()['error']}")
    else:
        data = response.json()
        rate = data["rates"][curr]
        result = amt * rate

        st.success(
            f"{1} {base} = {rate:.2f} {curr} (Date: {data['date']}) \n\n"
            f"{amt} {base} = {result:.2f} {curr} (Date: {data['date']})"

        )
