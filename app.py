import streamlit as st
import pandas as pd
import numpy as np
from librería_funciones_proyecto1 import calcular_cuota_prestamo_frances

#Aplicando CSS - Hojas de estilo
color_sidebar_text = "#032457"  #Color del fondo del logo

st.markdown(
    f"""
    <style>
        [data-testid="stSidebar"] * {{
            color: {color_sidebar_text} !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.image("logodmc_2.png")
st.set_page_config(page_title="Proyecto 1 - Fundamentos de Programación", layout="wide")

menu = st.sidebar.selectbox(
    "Menú de navegación...",
    ["Principal", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# Principal
if menu == "Principal":
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

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []
    
    st.title("Ejercicio 1 – Flujo de Caja con Listas")
    
    st.markdown("""
    Este módulo permite registrar movimientos financieros (ingresos y gastos) 
    y calcular el flujo de caja final.
    """)
    
    # Ingreso de datos
    concepto = st.text_input("Ingrese el concepto")
    tipo_movimiento = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Ingrese el valor", min_value=0.0, step=0.1)
    
    # Botón para agregar movimiento
    if st.button("Agregar movimiento"):
        if concepto.strip() == "" or valor == 0:
            st.error("Debe ingresar un concepto y un valor mayor a 0.")
        else:
            st.session_state.movimientos.append({
                "Concepto": concepto,
                "Movimiento": tipo_movimiento,
                "Valor": valor
            })
            st.success("Movimiento agregado correctamente.")
    
    # Mostrar tabla de movimientos
    if st.session_state.movimientos:
        df = pd.DataFrame(st.session_state.movimientos)
        st.markdown("### Detalle de movimientos registrados")
        st.dataframe(df)
    
        total_ingresos = df[df["Movimiento"] == "Ingreso"]["Valor"].sum()
        total_gastos = df[df["Movimiento"] == "Gasto"]["Valor"].sum()
        saldo = total_ingresos - total_gastos
    
        # Mostramos los resultados
        st.metric("Total ingresos", f"{total_ingresos:.2f}")
        st.metric("Total gastos", f"{total_gastos:.2f}")
        st.metric("Saldo final", f"{saldo:.2f}")
    
        if saldo >= 0:
            st.success("Flujo de caja: A FAVOR")
        else:
            st.error("Flujo de caja: EN CONTRA")
            
# =========================
# EJERCICIO 2 – Registro con NumPy y DataFrame
# =========================
elif menu == "Ejercicio 2":
    
    # Inicialización de los Arrays
    if "Productos" not in st.session_state:
        st.session_state.Productos = np.array([])
        st.session_state.Categorias = np.array([])
        st.session_state.Precios = np.array([])
        st.session_state.Cantidades = np.array([])
        st.session_state.Totales = np.array([])
    
    st.title("Ejercicio 2 – Registro con NumPy, Arrays y DataFrame")
    
    st.markdown("""
    Este módulo permite registrar productos con su categoría, precio y cantidad,
    almacenarlos en arrays de NumPy y mostrar un DataFrame actualizado.
    """)
    
    # Formulario de ingreso
    producto = st.text_input("Nombre del producto")
    categoria = st.selectbox("Categoría", ["Alimentos", "Bebidas", "Electrónicos", "Otros"])
    precio = st.number_input("Precio", min_value=0.0, step=0.1)
    cantidad = st.number_input("Cantidad", min_value=0, step=1)
    
    # Botón para agregar registro
    if st.button("Agregar producto"):
        if producto.strip() == "" or precio == 0 or cantidad == 0:
            st.error("Debe ingresar un producto, precio mayor a 0 y cantidad mayor a 0.")
        else:
            total = precio * cantidad
            st.session_state.Productos = np.append(st.session_state.Productos, producto)
            st.session_state.Categorias = np.append(st.session_state.Categorias, categoria)
            st.session_state.Precios = np.append(st.session_state.Precios, precio)
            st.session_state.Cantidades = np.append(st.session_state.Cantidades, cantidad)
            st.session_state.Totales = np.append(st.session_state.Totales, total)
            st.success("Producto agregado correctamente.")
    
    # Mostrar DataFrame actualizado
    if st.session_state.Productos.size > 0:
        df = pd.DataFrame({
            "Producto": st.session_state.Productos,
            "Categoría": st.session_state.Categorias,
            "Precio": st.session_state.Precios,
            "Cantidad": st.session_state.Cantidades,
            "Total": st.session_state.Totales
        })
    
        st.markdown("### Registro Actualizado")
        st.dataframe(df)
# =========================
# EJERCICIO 3 – Uso de funciones externas
# =========================
elif menu == "Ejercicio 3":
    if "historico_prestamos" not in st.session_state:
        st.session_state.historico_prestamos = []
    
    st.title("Ejercicio 3 – Uso de funciones desde librería externa")
    
    st.markdown("""
    Este módulo conecta la función **calcular_cuota_prestamo_frances** con widgets en Streamlit.
    Permite ingresar parámetros, ejecutar el cálculo y mantener un histórico de resultados.
    """)
    
    # =========================
    # Selector de función
    # =========================
    funcion = st.selectbox("Seleccione la función a ejecutar", ["calcular_cuota_prestamo_frances"])
    
    # =========================
    # Widgets de parámetros
    # =========================
    monto = st.number_input("Monto del préstamo", min_value=0.0, step=100.0)
    tasa = st.number_input("Tasa anual (%)", min_value=0.0, step=0.1)
    plazo = st.number_input("Plazo en meses", min_value=1, step=1)
    
    # =========================
    # Botón para ejecutar
    # =========================
    if st.button("Calcular"):
        if funcion == "calcular_cuota_prestamo_frances":
            resultado = calcular_cuota_prestamo_frances(monto, tasa, plazo)
    
            # Mostrar resultado en pantalla
            st.markdown("### Resultado del cálculo")
            st.write(f"**Cuota mensual:** {resultado['cuota_mensual']}")
            st.write(f"**Total pagado:** {resultado['total_pagado']}")
            st.write(f"**Interés total:** {resultado['interes_total']}")
    
            # Guardar en histórico
            st.session_state.historico_prestamos.append({
                "Monto": monto,
                "Tasa (%)": tasa,
                "Plazo (meses)": plazo,
                "Cuota mensual": resultado["cuota_mensual"],
                "Total pagado": resultado["total_pagado"],
                "Interés total": resultado["interes_total"]
            })
    
    # =========================
    # Mostrar histórico acumulado
    # =========================
    if st.session_state.historico_prestamos:
        df = pd.DataFrame(st.session_state.historico_prestamos)
        st.markdown("### Histórico de cálculos")
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
