import streamlit as st
from PIL import Image
import folium
from streamlit_folium import st_folium

# Configuration de la page
st.set_page_config(
    page_title="Detection illegale de batiment",
    layout="wide",
)

# --- Définition des pages ---

def page_contexte_exploration():
    """
    Page 1: Contexte et Exploration
    - Présentation du projet
    - Texte descriptif
    - Images explicatives
    """
    st.title("Contexte et Exploration")

    st.header("Présentation du projet")
    st.markdown(
        """
        Le projet **Detection illégale de bâtiment** vise à identifier automatiquement, à partir d'images aériennes ou satellites, 
        les constructions réalisées sans autorisation administrative. 

        Pour cela, nous utilisons un modèle YOLO pré-entraîné adapté à la détection d’indices architecturaux.
        """
    )

    st.header("Illustrations du contexte")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Image aérienne")
        st.image("assets/aerienne_exemple.jpg", caption="Vue aérienne d'une zone urbaine", use_column_width=True)
    with col2:
        st.subheader("Carte cadastrale")
        st.image("assets/cadastral_exemple.jpg", caption="Carte cadastrale officielle", use_column_width=True)


def page_modele_selectione():
    """
    Page 2: Modele selectione
    - Sélection d’un lieu via carte interactive
    - Récupération des coordonnées
    - Lancement de l’analyse YOLO
    """
    st.title("Modele selectione")

    st.markdown(
        """
        **Étapes d'utilisation** :
        1. Choisir un point sur la carte pour obtenir ses coordonnées.
        2. Valider pour lancer l'analyse YOLO sur la zone sélectionnée.
        """
    )

    # Création de la carte Folium avec popup de coordonnées
    m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
    m.add_child(folium.LatLngPopup())  # Permet de cliquer et d'obtenir lat/lng
    st.subheader("Sélectionnez un lieu (Cliquez sur la carte)")
    map_data = st_folium(m, width=700, height=500)

    # Récupération des dernières coordonnées cliquées
    if map_data and map_data.get("last_clicked"):
        coords = map_data["last_clicked"]
        lat, lon = coords['lat'], coords['lng']
        st.success(f"Coordonnées sélectionnées : **{lat:.6f}, {lon:.6f}**")

        # Bouton de validation pour lancer l'analyse
        if st.button("Analyser la zone avec YOLO"):
            # Ici, on appellerait la fonction backend : analyse_yolo(latitude, longitude)
            # Pour l'instant, placeholder :
            st.info("Analyse en cours...")
            # result = analyse_yolo(lat, lon)
            # st.write(result)
            st.write(f"Résultat simulé : 3 bâtiments détectés dont 1 illégal sur le secteur.")
    else:
        st.info("Cliquez sur la carte pour sélectionner un point puis validez.")


def page_detection_demo():
    """
    Page 3: Detection demo
    - Démonstration rapide avec une image pré-enregistrée
    """
    st.title("Detection demo")
    st.markdown(
        """
        Cliquez sur **Démarrer la démo** pour voir une analyse fictive d'un bâtiment illégal.
        """
    )

    if st.button("Démarrer la démo"):
        # Chargement d'une image et d'un masque préenregistrés
        img = Image.open("assets/demo_image.jpg")
        mask = Image.open("assets/demo_mask.png")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Image originale")
            st.image(img, use_column_width=True)
        with col2:
            st.subheader("Masque de détection")
            st.image(mask, use_column_width=True)

        st.success("Détection fictive terminée : zone illégale mise en évidence en rouge.")


# --- Navigation ---
PAGES = {
    "Contexte et Exploration": page_contexte_exploration,
    "Modele selectione": page_modele_selectione,
    "Detection demo": page_detection_demo,
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Aller à", list(PAGES.keys()))

# Exécution de la page sélectionnée
PAGES[selection]()
