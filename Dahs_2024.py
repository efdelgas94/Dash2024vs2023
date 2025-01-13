import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Datos reales
datos = {
    "Canal": ["APP", "CAR", "IFI", "INHOUSE", "PORTAL", "REDES"],
    "2023": [
        [42866, 35156, 36004, 32414, 33573, 31228, 30773, 30369, 28491, 29785, 28344, 27868],
        [200614, 179989, 206921, 195246, 202014, 191791, 191887, 198217, 191871, 196714, 191537, 184392],
        [871230, 776400, 899560, 863006, 891736, 877311, 910114, 966361, 920688, 913890, 901452, 922955],
        [233914, 217881, 252085, 233037, 236766, 238754, 242479, 246328, 239779, 239110, 231107, 233027],
    ],
    "2024": [
        [29613, 28235, 29531, 33670, 30349, 27434, 26144, 26021, 26623, 29061, 26129, 25692],
        [186913, 176177, 186368, 183217, 190890, 184099, 198499, 194917, 186994, 187269, 169688, 171453],
        [1020008, 920377, 966413, 925961, 932369, 906495, 965177, 946290, 902701, 943883, 886073, 950733],
        [222393, 230555, 236394, 226471, 232625, 216070, 222723, 223191, 210609, 240412, 256438, 262935],
    ]
}

# Meses y canales
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
canales = datos["Canal"]
transacciones_2023 = datos["2023"]
transacciones_2024 = datos["2024"]

# Preparar los datos para crear un DataFrame
data = []
for canal, trans_2023, trans_2024 in zip(canales, transacciones_2023, transacciones_2024):
    for i, mes in enumerate(meses):
        data.append({"Año": 2023, "Mes": mes, "Canal": canal, "Transacciones": trans_2023[i]})
        data.append({"Año": 2024, "Mes": mes, "Canal": canal, "Transacciones": trans_2024[i]})

# Crear el DataFrame
df = pd.DataFrame(data)

# Título
st.title("Comparación de transacciones por canal y año")

# Selección del canal
canal_seleccionado = st.selectbox(
    "Seleccione el canal:",
    options=df["Canal"].unique(),
    index=0  # default to the first canal
)

# Selección de los años
años_seleccionados = st.multiselect(
    "Seleccione el/los año(s):",
    options=[2023, 2024],
    default=[2023, 2024]
)

# Filtrar los datos
datos_filtrados = df[(df["Canal"] == canal_seleccionado) & (df["Año"].isin(años_seleccionados))]

# Crear el gráfico
fig = go.Figure()
for año in años_seleccionados:
    datos_año = datos_filtrados[datos_filtrados["Año"] == año]
    fig.add_trace(go.Scatter(
        x=datos_año["Mes"],
        y=datos_año["Transacciones"],
        mode="lines+markers",
        name=f"{canal_seleccionado} - {año}"
    ))

fig.update_layout(
    title=f"Transacciones en {canal_seleccionado} (Comparación de años)",
    xaxis_title="Mes",
    yaxis_title="Transacciones",
    legend_title="Año"
)

# Mostrar el gráfico
st.plotly_chart(fig)
