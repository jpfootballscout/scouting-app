import streamlit as st

st.title("⚽ Football Scouting Platform")

st.write("Witaj w systemie scoutingowym.")

zawodnik = st.text_input("Imię i nazwisko zawodnika")

pozycja = st.selectbox(
    "Pozycja",
    ["BR", "LO", "PO", "ŚO", "6", "8", "10", "Skrzydło", "9"]
)

ocena = st.slider("Ocena zawodnika", 1, 10)

if st.button("Zapisz raport"):
    st.success("Raport został zapisany!")
