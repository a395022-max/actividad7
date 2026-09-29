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
    if ph < 6.0 or ph > 7.0:
        resultado = "revisar el ph"
    elif ph < 20.0 or temperatura > 25.0:
        resultado = "revisar temperatura"
    else:
        resultado = "lote aceptable"
    st.write(f"Resultado: {resultado}")
