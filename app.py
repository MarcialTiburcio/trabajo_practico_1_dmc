import streamlit as st
import pandas as pd
import numpy as np
from libreria_funciones_proyecto1 import calcular_cuota_prestamo_frances
from libreria_clases_proyecto1 import Empleado

# =========================
# Configuración de estilos
# =========================
color_sidebar_bg = "#032457"   # azul corporativo
color_sidebar_text = "#FFFFFF" # texto blanco
color_button = "#1E90FF"       # azul dinámico
color_success = "#28a745"      # verde éxito
color_error = "#dc3545"        # rojo error

st.set_page_config(page_title="Proyecto 1 - Fundamentos de Programación", layout="wide")

st.markdown(
    f"""
    <style>
        /* Sidebar */
        [data-testid="stSidebar"] * {{
            color: {color_sidebar_text} !important;
        }}

        /* Botones */
        div.stButton > button {{
            background-color: {color_button};
            color: white;
            border-radius: 8px;
            font-weight: bold;
            padding: 0.5em 1em;
        }}
        div.stButton > button:hover {{
            background-color: #104E8B;
            color: #FFD700;
        }}

        /* DataFrame */
        .stDataFrame {{
            border: 2px solid {color_sidebar_bg};
            border-radius: 5px;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# Sidebar
# =========================
st.sidebar.image("logodmc_2.png")
menu = st.sidebar.selectbox(
    "Menú de navegación...",
    ["Principal", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# =========================
# Principal
# =========================
if menu == "Principal":
    st.title("Trabajo Práctico 1 - Especialización de Python for Analytics")
    st.image("logo-python.png")
    st.subheader("Módulo 1 - Curso Python DMC")
    st.write("**Nombre del estudiante:** TIBURCIO TOTOS, Reyes Marcial")
    st.write("**Año:** 2026")
    st.markdown("""
    ### Descripción
    En el proyecto "Trabajo Práctico 1" se aplicó los conocimientos básicos de programación en Python adquiridos en este curso; esta aplicación integra los conceptos fundamentales de:
    - Variables
    - Listas, Diccionarios
    - Estructuras de datos  
    - Control de flujo  
    - Funciones  
    - Programación funcional y Programación orientada a objetos (POO)  

    **Tecnologías utilizadas:** Python, Streamlit, NumPy, Pandas
    """)

# =========================
# Ejercicio 1 – Flujo de caja
# =========================
elif menu == "Ejercicio 1":
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    st.title("Ejercicio 1 – Flujo de Caja con Listas")
    concepto = st.text_input("Ingrese el concepto")
    tipo_movimiento = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Ingrese el valor", min_value=0.0, step=0.1)

    if st.button("➕ Agregar movimiento"):
        if concepto.strip() == "" or valor == 0:
            st.error("Debe ingresar un concepto y un valor mayor a 0.")
        else:
            st.session_state.movimientos.append({
                "Concepto": concepto,
                "Movimiento": tipo_movimiento,
                "Valor": valor
            })
            st.success("Movimiento agregado correctamente ✅")

    if st.session_state.movimientos:
        df = pd.DataFrame(st.session_state.movimientos)
        st.markdown("### 📋 Detalle de movimientos registrados")
        st.dataframe(df)

        total_ingresos = df[df["Movimiento"] == "Ingreso"]["Valor"].sum()
        total_gastos = df[df["Movimiento"] == "Gasto"]["Valor"].sum()
        saldo = total_ingresos - total_gastos

        st.metric("💰 Total ingresos", f"{total_ingresos:.2f}")
        st.metric("📉 Total gastos", f"{total_gastos:.2f}")
        st.metric("📊 Saldo final", f"{saldo:.2f}")

        if saldo >= 0:
            st.success("Flujo de caja: A FAVOR ✅")
        else:
            st.error("Flujo de caja: EN CONTRA ❌")

# =========================
# Ejercicio 2 – Registro con NumPy
# =========================
elif menu == "Ejercicio 2":
    if "Productos" not in st.session_state:
        st.session_state.Productos = np.array([])
        st.session_state.Categorias = np.array([])
        st.session_state.Precios = np.array([])
        st.session_state.Cantidades = np.array([])
        st.session_state.Totales = np.array([])

    st.title("Ejercicio 2 – Registro con NumPy, Arrays y DataFrame")
    producto = st.text_input("Nombre del producto")
    categoria = st.selectbox("Categoría", ["Alimentos", "Bebidas", "Electrónicos", "Otros"])
    precio = st.number_input("Precio", min_value=0.0, step=0.1)
    cantidad = st.number_input("Cantidad", min_value=0, step=1)

    if st.button("➕ Agregar producto"):
        if producto.strip() == "" or precio == 0 or cantidad == 0:
            st.error("Debe ingresar un producto, precio mayor a 0 y cantidad mayor a 0.")
        else:
            total = precio * cantidad
            st.session_state.Productos = np.append(st.session_state.Productos, producto)
            st.session_state.Categorias = np.append(st.session_state.Categorias, categoria)
            st.session_state.Precios = np.append(st.session_state.Precios, precio)
            st.session_state.Cantidades = np.append(st.session_state.Cantidades, cantidad)
            st.session_state.Totales = np.append(st.session_state.Totales, total)
            st.success("Producto agregado correctamente ✅")

    if st.session_state.Productos.size > 0:
        df = pd.DataFrame({
            "Producto": st.session_state.Productos,
            "Categoría": st.session_state.Categorias,
            "Precio": st.session_state.Precios,
            "Cantidad": st.session_state.Cantidades,
            "Total": st.session_state.Totales
        })
        st.markdown("### 📋 Registro Actualizado")
        st.dataframe(df)

# =========================
# Ejercicio 3 – Funciones externas
# =========================
elif menu == "Ejercicio 3":
    if "historico_prestamos" not in st.session_state:
        st.session_state.historico_prestamos = []

    st.title("Ejercicio 3 – Uso de funciones desde librería externa")
    funcion = st.selectbox("Seleccione la función a ejecutar...", ["calcular_cuota_prestamo_frances"])
    monto = st.number_input("Monto del préstamo", min_value=0.0, step=100.0)
    tasa = st.number_input("Tasa anual (%)", min_value=0.0, step=0.1)
    plazo = st.number_input("Plazo en meses", min_value=1, step=1)

    if st.button("⚡ Calcular"):
        if funcion == "calcular_cuota_prestamo_frances":
            resultado = calcular_cuota_prestamo_frances(monto, tasa, plazo)
            st.markdown("### 📊 Resultado del cálculo")
            st.metric("Cuota mensual", resultado['cuota_mensual'])
            st.metric("Total pagado", resultado['total_pagado'])
            st.metric("Interés total", resultado['interes_total'])

            st.session_state.historico_prestamos.append({
                "Monto": monto,
                "Tasa (%)": tasa,
                "Plazo (meses)": plazo,
                "Cuota mensual": resultado["cuota_mensual"],
                "Total pagado": resultado["total_pagado"],
                "Interés total": resultado["interes_total"]
            })

    if st.session_state.historico_prestamos:
        df = pd.DataFrame(st.session_state.historico_prestamos)
        st.markdown("### 📋 Histórico de cálculos")
        st.dataframe(df)

# =========================
# Ejercicio 4 – Clases con CRUD
# =========================
elif menu == "Ejercicio 4":
    if "empleados" not in st.session_state:
        st.session_state.empleados = []

    st.title("Ejercicio 4 – Uso de clases con CRUD")
    st.markdown("Este módulo conecta la clase **Empleado** con widgets en Streamlit. Permite crear, visualizar, actualizar y eliminar registros de empleados.")

    # Tabs para CRUD
    tab1, tab2, tab3, tab4 = st.tabs(["➕ Crear", "📋 Leer", "✏️ Actualizar", "🗑️ Eliminar"])

    # -------------------------
    # Crear
    # -------------------------
    with tab1:
        st.subheader("Crear empleado")
        nombre = st.text_input("Nombre")
        salario_base = st.number_input("Salario base", min_value=0.0, step=100.0)
        bono = st.number_input("Porcentaje de bono (%)", min_value=0.0, step=1.0)
        descuento = st.number_input("Porcentaje de descuento (%)", min_value=0.0, step=1.0)

        if st.button("➕ Agregar empleado"):
            if nombre.strip() == "" or salario_base <= 0:
                st.error("Debe ingresar un nombre y un salario base mayor a 0.")
            else:
                empleado = Empleado(nombre, salario_base, bono, descuento)
                st.session_state.empleados.append(empleado)
                st.success("Empleado agregado correctamente ✅")

    # -------------------------
    # Leer
    # -------------------------
    with tab2:
        st.subheader("Lista de empleados")
        if st.session_state.empleados:
            lista_empleados = [emp.resumen() for emp in st.session_state.empleados]
            df = pd.DataFrame(lista_empleados)
            st.dataframe(df)

            st.markdown("### 📊 Métricas ejecutivas por empleado")
            for emp in st.session_state.empleados:
                resumen = emp.resumen()
                st.markdown(f"#### 👤 {resumen['nombre']}")
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Salario base", resumen["salario_base"])
                col2.metric("Bono", resumen["bono"])
                col3.metric("Descuento", resumen["descuento"])
                col4.metric("Salario neto", resumen["salario_neto"])
                st.divider()
        else:
            st.info("No hay empleados registrados.")

    # -------------------------
    # Actualizar
    # -------------------------
    with tab3:
        st.subheader("Actualizar empleado")
        if st.session_state.empleados:
            nombres = [emp.nombre for emp in st.session_state.empleados]
            seleccionado = st.selectbox("Seleccione empleado", nombres)

            empleado_seleccionado = next((e for e in st.session_state.empleados if e.nombre == seleccionado), None)

            if empleado_seleccionado:
                nuevo_salario = st.number_input("Nuevo salario base", value=empleado_seleccionado.salario_base, step=100.0)
                nuevo_bono = st.number_input("Nuevo porcentaje de bono (%)", value=empleado_seleccionado.porcentaje_bono, step=1.0)
                nuevo_descuento = st.number_input("Nuevo porcentaje de descuento (%)", value=empleado_seleccionado.porcentaje_descuento, step=1.0)

                if st.button("✏️ Actualizar"):
                    empleado_seleccionado.salario_base = nuevo_salario
                    empleado_seleccionado.porcentaje_bono = nuevo_bono
                    empleado_seleccionado.porcentaje_descuento = nuevo_descuento
                    st.success("Empleado actualizado correctamente ✅")
        else:
            st.info("No hay empleados para actualizar.")

    # -------------------------
    # Eliminar
    # -------------------------
    with tab4:
        st.subheader("Eliminar empleado")
        if st.session_state.empleados:
            nombres = [emp.nombre for emp in st.session_state.empleados]
            seleccionado = st.selectbox("Seleccione empleado a eliminar", nombres)

            if st.button("🗑️ Eliminar"):
                st.session_state.empleados = [e for e in st.session_state.empleados if e.nombre != seleccionado]
                st.success(f"Empleado {seleccionado} eliminado correctamente ❌")
        else:
            st.info("No hay empleados para eliminar.")
