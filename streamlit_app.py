import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Google Sheets auth
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=scope
)

client = gspread.authorize(creds)

# Open sheet
sheet = client.open("scouting_reports").sheet1

# UI
st.title("⚽ Football Scouting Platform")

st.write("Witaj w systemie scoutingowym.")

zawodnik = st.text_input("Imię i nazwisko zawodnika")

pozycja = st.selectbox(
    "Pozycja",
    ["BR", "ŚO", "LO", "PO", "DP", "ŚP", "10", "LS", "PS", "N"]
)

ocena = st.slider("Ocena zawodnika", 1, 10)

if st.button("Zapisz raport"):

    data = datetime.now().strftime("%Y-%m-%d")

    sheet.append_row([
        data,
        zawodnik,
        pozycja,
        ocena
    ])

    st.success("Raport został zapisany!")
