import streamlit as st
import pandas as pd
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Charger les données depuis un fichier CSV
df_comptes = pd.read_csv("comptes_donnees.csv")

# Transformer le DataFrame en dictionnaire structuré
lesDonneesDesComptes = {"usernames": {}}
for _, row in df_comptes.iterrows():
    lesDonneesDesComptes["usernames"][row["username"]] = {
        "name": row["name"],
        "password": row["password"],
        "email": row["email"],
        "failed_login_attempts": row.get("failed_login_attempts", 0),
        "logged_in": row.get("logged_in", False),
        "role": row.get("role", "utilisateur"),
    }

# Authentification
authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "app_cookie",          # Le nom du cookie
    "secret_key",          # La clé du cookie
    30                     # Le nombre de jours avant expiration du cookie
)

authenticator.login()

# Fonction d'accueil
def accueil():
    st.title("Bienvenue sur ma page")
# Gestion de l'état d'authentification
if st.session_state["authentication_status"]:
    accueil()
    authenticator.logout("Déconnexion", "sidebar")
elif st.session_state["authentication_status"] is False:
    st.error("Le nom d'utilisateur ou le mot de passe est incorrect.")
elif st.session_state["authentication_status"] is None:
    st.warning("Veuillez remplir les champs nom d'utilisateur et mot de passe.")

# Options du menu
with st.sidebar:
    selection = option_menu(
            menu_title=None,
            options = ["🏠 Accueil", "🐱 Les photos de mon chat"]
        )
# Affichage basé sur la page sélectionnée
if selection == "🏠 Accueil":
    st.sidebar.write("bienvenue root.")
    st.header("Bienvenue sur ma page ")
    st.image("https://gifdb.com/images/high/standing-ovation-crowd-applause-oscar-awards-ai72icmh1ac7apdz.gif")
elif selection == "🐱 Les photos de mon chat":
    st.subheader("Voici les magnifiques photos de mon chat")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Chat")
        st.image("https://static.streamlit.io/examples/cat.jpg", caption="Un chat mignon")

    with col2:
        st.header("Chat joueur")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col3:
        st.header("Chat endormi")
        st.image("https://static.streamlit.io/examples/cat.jpg", caption="Chat endormi")


