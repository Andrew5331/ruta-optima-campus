import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.image as mpimg
from datetime import datetime
import pytz
import requests

# Coordenadas de los nodos actualizadas
pos = {
    "Entrada principal 1": (10.5, 10.5),
    "Ad portas": (8.6, 9.6),
    "Parqueadero 2": (9.5, 9.8),
    "Puente rojo": (7.6, 9.4),
    "Villa de Leyva": (6.3, 8.6),
    "Puente gris": (5.6, 8.9),
    "Punto wok": (5.6, 8.2),
    "Biblioteca": (6.8, 7.6),
    "Embarcadero y G": (7.6, 7.1),
    "Edificio E": (8.2, 6.4),
    "E1": (8.5, 5.8),
    "E2": (7.9, 6.0),
    "Puente madera": (7.5, 4.8),
    "Atelier y Medicina": (6.0, 5.0),
    "CAF": (4.6, 4.0),
    "Arcos y Nason": (3.8, 3.6),
    "Ingeniería A, B, C": (3.5, 6.6),
    "Parqueadero 1": (1.8, 7.7),
    "Quioscos": (2.5, 8.0),
    "Salida K": (4.4, 9.6),
    "Hospital Sabana": (10.2, 0.7),
    "INALDE": (9.1, 1.5),
    "Parqueadero 3": (8.5, 2.2)
}

# Crear grafo base
G_original = nx.Graph()
G_original.add_nodes_from(pos.keys())

# Definición de aristas con pesos específicos por tipo de usuario
pesos_por_usuario = {
    "Niño": {
        ("Entrada principal 1", "Ad portas"): 2,
        ("Ad portas", "Parqueadero 2"): 2,
        ("Ad portas", "Puente rojo"): 2,
        ("Puente rojo", "Villa de Leyva"): 3,
        ("Villa de Leyva", "Puente gris"): 2,
        ("Villa de Leyva", "Punto wok"): 2,
        ("Villa de Leyva", "Biblioteca"): 2,
        ("Biblioteca", "Embarcadero y G"): 2,
        ("Embarcadero y G", "Edificio E"): 2,
        ("Edificio E", "E1"): 1,
        ("Edificio E", "E2"): 1,
        ("Edificio E", "Puente madera"): 3,
        ("Puente madera", "Atelier y Medicina"): 2,
        ("Atelier y Medicina", "CAF"): 3,
        ("CAF", "Arcos y Nason"): 2,
        ("Arcos y Nason", "Ingeniería A, B, C"): 3,
        ("Ingeniería A, B, C", "Parqueadero 1"): 2,
        ("Ingeniería A, B, C", "Quioscos"): 2,
        ("Ingeniería A, B, C", "Salida K"): 3,
        ("Puente madera", "Hospital Sabana"): 4,
        ("Puente madera", "INALDE"): 2,
        ("INALDE", "Parqueadero 3"): 2,
        ("Parqueadero 3", "Hospital Sabana"): 3
    },
    "Adolescente": {
        ("Entrada principal 1", "Ad portas"): 1,
        ("Ad portas", "Parqueadero 2"): 1,
        ("Ad portas", "Puente rojo"): 1,
        ("Puente rojo", "Villa de Leyva"): 2,
        ("Villa de Leyva", "Puente gris"): 1,
        ("Villa de Leyva", "Punto wok"): 1,
        ("Villa de Leyva", "Biblioteca"): 1,
        ("Biblioteca", "Embarcadero y G"): 1,
        ("Embarcadero y G", "Edificio E"): 1,
        ("Edificio E", "E1"): 1,
        ("Edificio E", "E2"): 1,
        ("Edificio E", "Puente madera"): 2,
        ("Puente madera", "Atelier y Medicina"): 1,
        ("Atelier y Medicina", "CAF"): 2,
        ("CAF", "Arcos y Nason"): 1,
        ("Arcos y Nason", "Ingeniería A, B, C"): 2,
        ("Ingeniería A, B, C", "Parqueadero 1"): 1,
        ("Ingeniería A, B, C", "Quioscos"): 1,
        ("Ingeniería A, B, C", "Salida K"): 2,
        ("Puente madera", "Hospital Sabana"): 3,
        ("Puente madera", "INALDE"): 1,
        ("INALDE", "Parqueadero 3"): 1,
        ("Parqueadero 3", "Hospital Sabana"): 2
    },
    "Adulto": {
        ("Entrada principal 1", "Ad portas"): 2,
        ("Ad portas", "Parqueadero 2"): 2,
        ("Ad portas", "Puente rojo"): 2,
        ("Puente rojo", "Villa de Leyva"): 3,
        ("Villa de Leyva", "Puente gris"): 2,
        ("Villa de Leyva", "Punto wok"): 2,
        ("Villa de Leyva", "Biblioteca"): 2,
        ("Biblioteca", "Embarcadero y G"): 2,
        ("Embarcadero y G", "Edificio E"): 2,
        ("Edificio E", "E1"): 1,
        ("Edificio E", "E2"): 1,
        ("Edificio E", "Puente madera"): 3,
        ("Puente madera", "Atelier y Medicina"): 2,
        ("Atelier y Medicina", "CAF"): 3,
        ("CAF", "Arcos y Nason"): 2,
        ("Arcos y Nason", "Ingeniería A, B, C"): 3,
        ("Ingeniería A, B, C", "Parqueadero 1"): 2,
        ("Ingeniería A, B, C", "Quioscos"): 2,
        ("Ingeniería A, B, C", "Salida K"): 3,
        ("Puente madera", "Hospital Sabana"): 4,
        ("Puente madera", "INALDE"): 2,
        ("INALDE", "Parqueadero 3"): 2,
        ("Parqueadero 3", "Hospital Sabana"): 3
    },
    "Tercera Edad": {
        ("Entrada principal 1", "Ad portas"): 4,
        ("Ad portas", "Parqueadero 2"): 3,
        ("Ad portas", "Puente rojo"): 3,
        ("Puente rojo", "Villa de Leyva"): 4,
        ("Villa de Leyva", "Puente gris"): 3,
        ("Villa de Leyva", "Punto wok"): 3,
        ("Villa de Leyva", "Biblioteca"): 3,
        ("Biblioteca", "Embarcadero y G"): 3,
        ("Embarcadero y G", "Edificio E"): 3,
        ("Edificio E", "E1"): 2,
        ("Edificio E", "E2"): 2,
        ("Edificio E", "Puente madera"): 4,
        ("Puente madera", "Atelier y Medicina"): 3,
        ("Atelier y Medicina", "CAF"): 4,
        ("CAF", "Arcos y Nason"): 3,
        ("Arcos y Nason", "Ingeniería A, B, C"): 4,
        ("Ingeniería A, B, C", "Parqueadero 1"): 3,
        ("Ingeniería A, B, C", "Quioscos"): 3,
        ("Ingeniería A, B, C", "Salida K"): 4,
        ("Puente madera", "Hospital Sabana"): 5,
        ("Puente madera", "INALDE"): 3,
        ("INALDE", "Parqueadero 3"): 3,
        ("Parqueadero 3", "Hospital Sabana"): 4
    }
}

# Definir aristas generales
edges = list(pesos_por_usuario["Niño"].keys())
G_original.add_edges_from(edges)


# Función para obtener hora y clima
def obtener_info_bogota():
    zona_horaria = pytz.timezone("America/Bogota")
    hora_actual = datetime.now(zona_horaria).strftime("%H:%M:%S")
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=4.7&longitude=-74.1&current=temperature_2m"
        r = requests.get(url)
        temperatura = r.json()["current"]["temperature_2m"]
        clima = f"Temperatura actual: {temperatura}°C"
    except:
        clima = "No se pudo obtener la información del clima."
    return hora_actual, clima


# Configuración de Streamlit
st.set_page_config(page_title="Rutas Óptimas Campus", layout="centered", page_icon="🧭")

st.markdown("""
<h1 style='text-align: center;'>🧭 Rutas Óptimas en el Campus - Universidad de La Sabana</h1>
<div style='background-color: #1f2c3c; padding: 20px; border-radius: 10px;'>
    <p style='color: white;'>
    Bienvenido a la aplicación de rutas óptimas en el campus de la Universidad de La Sabana.
    <ol>
        <li><b>Selecciona tu tipo de usuario:</b> Niño, Adolescente, Adulto o Tercera Edad.</li>
        <li><b>Elige el punto de inicio y destino:</b> Los edificios disponibles están listados.</li>
        <li><b>Visualiza la ruta más corta:</b> Se mostrará la ruta más eficiente según el tiempo estimado de desplazamiento.</li>
        <li><b>Observa el mapa del campus:</b> La ruta se destacará en el mapa para tu referencia.</li>
        <li><b>Consulta la hora local y el clima:</b> Información actualizada de Bogotá.</li>
    </ol>
    </p>
</div>
""", unsafe_allow_html=True)

# Simulación
st.sidebar.title("🔧 Simulación")
simular = st.sidebar.checkbox("Activar simulación")

nodos_excluidos = []
peso_personalizado = False

if simular:
    nodos_excluidos = st.sidebar.multiselect("Selecciona edificios cerrados:", list(pos.keys()))
    peso_personalizado = st.sidebar.checkbox("Comparar peso por distancia en lugar de tiempo")

# Crear copia del grafo
G = G_original.copy()

# Selecciones del usuario
tipo_usuario = st.selectbox("Selecciona tu tipo de usuario", list(pesos_por_usuario.keys()))
inicio = st.selectbox("Selecciona el punto de inicio", list(pos.keys()))
destino = st.selectbox("Selecciona el punto de destino", list(pos.keys()))

# Aplicar pesos
for u, v in edges:
    if u in nodos_excluidos or v in nodos_excluidos:
        if G.has_edge(u, v):
            G.remove_edge(u, v)
    else:
        if not peso_personalizado:
            peso = pesos_por_usuario[tipo_usuario].get((u, v), 1)
        else:
            x1, y1 = pos[u]
            x2, y2 = pos[v]
            peso = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        G.add_edge(u, v, weight=peso)

if inicio != destino:
    try:
        ruta = nx.dijkstra_path(G, source=inicio, target=destino, weight="weight")
        tiempo_total = nx.dijkstra_path_length(G, source=inicio, target=destino, weight="weight")
        st.success(
            f"Ruta más corta de **{inicio}** a **{destino}** con un tiempo estimado de {tiempo_total:.2f} unidades.")

        img = mpimg.imread("Grafo universidad3.jpg")
        edge_colors = ['red' if (u in ruta and v in ruta and abs(ruta.index(u) - ruta.index(v)) == 1) else 'gray' for
                       u, v in G.edges()]

        # Configuración mejorada para la visualización del grafo
        fig, ax = plt.subplots(figsize=(16, 12))  # Tamaño más grande

        # Mostrar imagen de fondo con transparencia
        ax.imshow(img, extent=[0, 11, 0, 11], alpha=0.4)

        # Dibujar nodos y aristas con parámetros optimizados
        nx.draw_networkx_nodes(
            G, pos,
            node_size=2500,  # Nodos más grandes
            node_color='lightblue',
            edgecolors='darkblue',
            linewidths=2,
            alpha=0.9,
            ax=ax)

        # Dibujar aristas
        nx.draw_networkx_edges(
            G, pos,
            width=2.5,  # Aristas más gruesas
            edge_color=edge_colors,
            alpha=0.7,
            ax=ax)

        # Dibujar etiquetas de nodos optimizadas
        nx.draw_networkx_labels(
            G, pos,
            font_size=9,  # Tamaño de fuente ajustado
            font_weight='bold',
            font_color='darkblue',
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, boxstyle='round,pad=0.3'),
            ax=ax)

        # Dibujar pesos de las aristas
        nx.draw_networkx_edge_labels(
            G, pos,
            edge_labels={(u, v): f"{d['weight']:.1f}" for u, v, d in G.edges(data=True)},
            font_size=8,
            font_color='darkred',
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.7),
            ax=ax,
            rotate=False)  # Evitar rotación para mejor legibilidad

        # Ajustes finales
        plt.axis('off')
        plt.tight_layout()

        st.pyplot(fig)

    except nx.NetworkXNoPath:
        st.error("No existe una ruta posible con las condiciones actuales.")
else:
    st.warning("Selecciona dos puntos distintos para ver la ruta.")

# Mostrar hora y clima
hora, clima = obtener_info_bogota()
st.info(f"🕒 Hora local en Bogotá: {hora}")
st.warning(f"🌡️ {clima}")