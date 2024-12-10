import streamlit as st

st.title("¡Hola!")

st.write("Esta es una aplicación de prueba que usa Streamlit.")

n1 = st.number_input("Escribe el primer numero", 0)
n2 = st.number_input("Escribe el segundo numero", 0)

st.write("La suma de ", n1, "  y de ", n2, " es ", n1 + n2)
