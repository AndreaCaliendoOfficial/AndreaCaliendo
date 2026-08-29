import streamlit as st
import pandas as pd
import base64

# Configurazione della pagina Streamlit
st.set_page_config(
    page_title="Andrea Caliendo | Ufficiale Hub Creativo",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Integrazione Google Analytics (GA4)
GA_TRACKING_ID = "G-E0YL99K55W"
ga_script = f"""
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_TRACKING_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_TRACKING_ID}');
</script>
"""
st.markdown(ga_script, unsafe_allow_html=True)

# Stile grafico personalizzato e pulito
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #e6edf3;
    }
    .stButton>button {
        background: linear-gradient(90deg, #1f6feb, #238636);
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: none;
        font-weight: bold;
    }
    .card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #30363d;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Caricamento del Catalogo Excel
@st.cache_data
def load_data():
    try:
        df = pd.read_excel("CATALOGO.xlsx")
        return df
    except Exception as e:
        return None

df = load_data()

# Intestazione Principale
st.title("🎵 Andrea Caliendo - Official Creator Hub")
st.markdown("### Produttore Indipendente | Musica, Audiolibri, Podcast & Favole")
st.write("Benvenuto nel portale ufficiale. Esplora tutti i progetti, le produzioni e i canali dedicati.")

st.divider()

# Barra laterale di navigazione
st.sidebar.image("https://img.icons8.com/fluency/96/musical-notes.png", width=80)
st.sidebar.header("Esplora Hub")
menu = st.sidebar.radio("Scegli sezione:", [
    "🏠 Home & Progetti", 
    "🎧 Musicalando", 
    "📖 AudioCalAI & Viaggi", 
    "🎙️ Storie nell'Ombra (True Crime)", 
    "👶 Il Mondo di Nonno Andrea",
    "📂 Catalogo Completo", 
    "ℹ️ Chi Sono"
])

# SEZIONE HOME
if menu == "🏠 Home & Progetti":
    st.subheader("I Nostri Universi Creativi")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>🎧 Musicalando</h3>
            <p>Musica d'autore, pop, urban napoletano e sonorità uniche prodotte con cura sartoriale.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card">
            <h3>📖 AudioCalAI</h3>
            <p>Racconti di viaggio, romanzi sonori immersivi e saghe on the road.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="card">
            <h3>🎙️ Storie nell'Ombra</h3>
            <p>Podcast True Crime, inchieste e vicende misteriose dal taglio cinematografico.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info("💡 Usa il menu laterale per navigare tra i singoli progetti e consultare il catalogo completo.")

# SEZIONE MUSICALANDO
elif menu == "🎧 Musicalando":
    st.subheader("🎧 Musicalando - Canale Musicale")
    st.write("Spazio dedicato alla musica d'autore, alle uscite discografiche e ai singoli pubblicati.")
    st.markdown("---")
    st.markdown("Ascolta i brani e scopri le ultime novità discografiche direttamente sulle piattaforme di streaming.")

# SEZIONE AUDIOCALAI
elif menu == "📖 AudioCalAI & Viaggi":
    st.subheader("📖 AudioCalAI - Audiolibri e Viaggi")
    st.write("Progetti narrativi e romanzi sonori, tra cui la saga 'Siberia On The Road: La Formula del Silenzio'.")
    st.markdown("---")
    st.markdown("Immergiti nei racconti di viaggio e nelle avventure sonore.")

# SEZIONE STORIE NELL'OMBRA
elif menu == "🎙️ Storie nell'Ombra (True Crime)":
    st.subheader("🎙️ Storie nell'Ombra")
    st.write("Podcast True Crime, inchieste e ricostruzioni di casi celebri (come Ted Bundy e Kenyel Brown).")
    st.markdown("---")
    st.markdown("Indagini e profili psicologici raccontati con un'atmosfera audio immersiva.")

# SEZIONE NONNO ANDREA
elif menu == "👶 Il Mondo di Nonno Andrea":
    st.subheader("👶 Il Mondo di Nonno Andrea")
    st.write("Favole della buonanotte, ninne nanne e contenuti dedicati ai più piccoli e alle famiglie.")
    st.markdown("---")
    st.markdown("Un angolo di dolcezza e fantasia con storie pensate per accompagnare i bambini nel mondo dei sogni.")

# SEZIONE CATALOGO
elif menu == "📂 Catalogo Completo":
    st.subheader("📂 Catalogo Ufficiale delle Opzioni e Produzioni")
    
    if df is not None:
        search_query = st.text_input("🔍 Cerca nel catalogo per brano, genere o progetto:", "")
        
        if search_query:
            mask = df.astype(str).apply(lambda x: x.str.contains(search_query, case=False, na=False)).any(axis=1)
            filtered_df = df[mask]
        else:
            filtered_df = df
            
        st.dataframe(filtered_df, use_container_width=True)
        st.caption(f"Totale elementi visualizzati: {len(filtered_df)}")
    else:
        st.warning("⚠️ Il file 'CATALOGO.xlsx' non è attualmente disponibile o risulta vuoto nel repository.")

# SEZIONE CHI SONO
elif menu == "ℹ️ Chi Sono":
    st.subheader("Informazioni sull'Artista")
    st.write("""
    Andrea Caliendo è un produttore indipendente, autore e sound designer attivo nella creazione di contenuti digitali avanzati, 
    musica multipiattaforma e narrazioni audio immersive.
    """)
    st.markdown("---")
    st.write("🌐 **Canali ufficiali:** Musicalando | AudioCalAI | Storie nell'Ombra")

# Footer in basso
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2026 Andrea Caliendo Official - Tutti i diritti riservati</p>", unsafe_allow_html=True)
