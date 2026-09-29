st.sidebar.title("Comprueba el pH")
st.sidebar.write("Leonardo Eusebio Martinez Manzano"
"3L"
"Facultad de ciencias quimicas")
import streamlit as st

st.title("Evaluación de un lote")

pH = st.number_input(
    "pH",
    value=6.5
)

temperatura = st.number_input(
    "Temperatura (°C)",
    value=23.0
)

if st.button("Evaluar"):

    # Completa aquí la lógica
    if pH < 6.0 or pH > 7.0:
        resultado = "revisar el ph"
    elif pH < 20.0 or temperatura > 25.0:
        resultado = "revisar temperatura"
    else:
        resultado = "lote aceptable"
    st.write(f"Resultado: {resultado}")
