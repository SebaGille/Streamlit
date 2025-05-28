import streamlit as st
from PIL import Image

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

    st.subheader("1. Source des données")
    st.markdown(
        """
        Les données utilisées dans ce projet proviennent de sources publiques telles que les images satellites de Google Earth 
        et les cartes cadastrales disponibles via les services de l'État. Ces données ont été prétraitées pour correspondre aux 
        besoins du modèle d’apprentissage.
        """
    )

    st.subheader("2. Exploration des modèles")
    st.markdown(
        """
        Plusieurs approches ont été envisagées pour détecter les bâtiments illégaux, incluant :
        - des réseaux de neurones convolutifs (CNN)
        - des modèles pré-entraînés de segmentation comme U-Net
        - des modèles de détection comme YOLOv5 et YOLOv8

        Des comparaisons ont été faites selon la précision, le rappel et la vitesse d'exécution.
        """
    )

    st.subheader("3. Choix du modèle")
    st.markdown(
        """
        Le modèle retenu est **YOLOv8**, car il présente un bon équilibre entre performance et rapidité, 
        et permet une détection temps réel avec un faible taux de faux positifs.
        """
    )

    st.header("Illustrations du contexte")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Image aérienne")
        st.image("assets/aerienne_exemple.jpg", caption="Vue aérienne d'une zone urbaine", use_container_width=True)
    with col2:
        st.subheader("Carte cadastrale")
        st.image("assets/cadastral_exemple.jpg", caption="Carte cadastrale officielle", use_container_width=True)


def page_modele_selectione():
    """
    Page 2: Modele selectione
    - Saisie manuelle des coordonnées
    - Lancement de l’analyse YOLO
    """
    st.title("Modele selectione")

    st.markdown(
        """
        **Étapes d'utilisation** :
        1. Saisir la latitude et la longitude de la zone à analyser.
        2. Cliquer sur **Analyser la zone avec YOLO**.
        """
    )

    lat = st.number_input("Latitude", value=48.856600, format="%.6f")
    lon = st.number_input("Longitude", value=2.352200, format="%.6f")

    if st.button("Analyser la zone avec YOLO"):
        # Appel de la fonction backend : analyse_yolo(latitude, longitude)
        st.info("Analyse en cours...")
        # result = analyse_yolo(lat, lon)
        # st.write(result)
        st.write(f"Résultat simulé : 3 bâtiments détectés dont 1 illégal sur le secteur géré par {lat:.6f}, {lon:.6f}.")


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
        img = Image.open("assets/demo_image.jpg")
        mask = Image.open("assets/demo_mask.png")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Image originale")
            st.image(img, use_container_width=True)
        with col2:
            st.subheader("Masque de détection")
            st.image(mask, use_container_width=True)

        st.success("Détection fictive terminée : zone illégale mise en évidence en rouge.")


# --- Navigation ---
PAGES = {
    "Contexte et Exploration": page_contexte_exploration,
    "Modele selectione": page_modele_selectione,
    "Detection demo": page_detection_demo,
}

st.sidebar.title("Navigation")
st.sidebar.radio("Aller à", list(PAGES.keys()), index=0, key="page_selector")
selection = st.session_state.page_selector

# Exécution de la page sélectionnée
PAGES[selection]()
