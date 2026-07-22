import streamlit as st
import pandas as pd
import numpy as np

# =========================
# Configuración inicial
# =========================
st.sidebar.image("logodmc_2.png")
st.set_page_config(page_title="Proyecto 1 - Fundamentos de Programación", layout="wide")

# =========================
# Menú lateral
# =========================
menu = st.sidebar.selectbox(
    "Navegación",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# =========================
# HOME
# =========================
if menu == "Home":
    st.title("Proyecto Aplicado en Streamlit – Fundamentos de Programación")
    st.subheader("Módulo 1 - Curso Python DMC")
    st.image("https://www.python.org/static/community_logos/python-logo.png", width=200)
    st.write("**Nombre del estudiante:** Marcial")
    st.write("**Año:** 2026")
    st.markdown("""
    ### Descripción
    Esta aplicación integra los conceptos fundamentales de programación en Python:
    - Variables  
    - Estructuras de datos  
    - Control de flujo  
    - Funciones  
    - Programación funcional  
    - Programación orientada a objetos (POO)  

    **Tecnologías utilizadas:** Python, Streamlit, NumPy, Pandas
    """)

# =========================
# EJERCICIO 1 – Flujo de caja con listas
# =========================
elif menu == "Ejercicio 1":
    st.markdown("### Ejercicio 1 – Flujo de Caja con Listas")

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    concepto = st.text_input("Concepto")
    tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor", min_value=0.0, step=10.0)

    if st.button("Agregar movimiento"):
        st.session_state.movimientos.append({"Concepto": concepto, "Tipo": tipo, "Valor": valor})
        st.success("Movimiento agregado correctamente")

    df = pd.DataFrame(st.session_state.movimientos)
    if not df.empty:
        st.dataframe(df)

        ingresos = df[df["Tipo"] == "Ingreso"]["Valor"].sum()
        gastos = df[df["Tipo"] == "Gasto"]["Valor"].sum()
        saldo = ingresos - gastos

        st.metric("Total Ingresos", ingresos)
        st.metric("Total Gastos", gastos)
        st.metric("Saldo Final", saldo)

        if saldo >= 0:
            st.success("El flujo de caja está a favor ✅")
        else:
            st.error("El flujo de caja está en contra ❌")

# =========================
# EJERCICIO 2 – Registro con NumPy y DataFrame
# =========================
elif menu == "Ejercicio 2":
    st.markdown("### Ejercicio 2 – Registro con NumPy y DataFrame")

    if "productos" not in st.session_state:
        st.session_state.productos = []

    nombre = st.text_input("Nombre del producto")
    categoria = st.selectbox("Categoría", ["Tecnología", "Alimentos", "Ropa", "Otros"])
    precio = st.number_input("Precio", min_value=0.0, step=1.0)
    cantidad = st.number_input("Cantidad", min_value=1, step=1)

    if st.button("Agregar producto"):
        total = precio * cantidad
        st.session_state.productos.append([nombre, categoria, precio, cantidad, total])
        st.success("Producto agregado correctamente")

    if st.session_state.productos:
        arr = np.array(st.session_state.productos)
        df = pd.DataFrame(arr, columns=["Producto", "Categoría", "Precio", "Cantidad", "Total"])
        st.dataframe(df)

# =========================
# EJERCICIO 3 – Uso de funciones externas
# =========================
elif menu == "Ejercicio 3":
    st.markdown("### Ejercicio 3 – Uso de Funciones desde Librería Externa")

    # Ejemplo: Supongamos que la librería tiene una función para calcular interés simple
    from libreria_funciones_proyecto1 import calcular_interes_simple

    capital = st.number_input("Capital", min_value=0.0)
    tasa = st.number_input("Tasa de interés (%)", min_value=0.0)
    tiempo = st.number_input("Tiempo (años)", min_value=0.0)

    if "historico_funciones" not in st.session_state:
        st.session_state.historico_funciones = []

    if st.button("Calcular interés"):
        resultado = calcular_interes_simple(capital, tasa, tiempo)
        st.write(f"El interés calculado es: {resultado}")
        st.session_state.historico_funciones.append([capital, tasa, tiempo, resultado])

    if st.session_state.historico_funciones:
        df = pd.DataFrame(st.session_state.historico_funciones, columns=["Capital", "Tasa", "Tiempo", "Resultado"])
        st.dataframe(df)

# =========================
# EJERCICIO 4 – Uso de clases externas con CRUD
# =========================
elif menu == "Ejercicio 4":
    st.markdown("### Ejercicio 4 – Uso de Clases con CRUD")

    from libreria_clases_proyecto1 import Cliente

    if "clientes" not in st.session_state:
        st.session_state.clientes = []

    nombre = st.text_input("Nombre del cliente")
    edad = st.number_input("Edad", min_value=0, step=1)
    correo = st.text_input("Correo electrónico")

    if st.button("Crear cliente"):
        nuevo = Cliente(nombre, edad, correo)
        st.session_state.clientes.append(nuevo)
        st.success("Cliente creado correctamente")

    if st.session_state.clientes:
        data = [{"Nombre": c.nombre, "Edad": c.edad, "Correo": c.correo} for c in st.session_state.clientes]
        df = pd.DataFrame(data)
        st.dataframe(df)

        # Actualizar y eliminar (ejemplo simple)
        seleccion = st.selectbox("Seleccionar cliente para eliminar", [c.nombre for c in st.session_state.clientes])
        if st.button("Eliminar cliente"):
            st.session_state.clientes = [c for c in st.session_state.clientes if c.nombre != seleccion]
            st.warning(f"Cliente {seleccion} eliminado")
