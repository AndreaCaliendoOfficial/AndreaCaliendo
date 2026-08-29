import streamlit as st
import pandas as pd
import base64

# Configurazione della pagina Streamlit
st.set_page_config(
    page_title="Andrea Caliendo | Hub Ufficiale",
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

# Stile grafico personalizzato (Dark Theme elegante con dettagli oro/blu)
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
    .stButton>button:hover {
        opacity: 0.9;
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
st.title("🎵 Andrea Caliendo - Official Hub")
st.markdown("### Creator Artist AI | Produttore Indipendente | Audiolibri & Podcast")
st.write("Hub ufficiale di Andrea Caliendo: Creator Artist AI e produttore indipendente. Esplora Musicalando, AudioCalAI e Storie nell'Ombra tra musica d'autore, podcast True Crime, romanzi sonori e favole.")

st.divider()

# Barra laterale di navigazione
st.sidebar.image("https://img.icons8.com/fluency/96/musical-notes.png", width=80)
st.sidebar.header("Navigazione")
menu = st.sidebar.radio("Scegli una sezione:", ["🏠 Home & Progetti", "📂 Catalogo Completo", "ℹ️ Chi Sono"])

# SEZIONE HOME
if menu == "🏠 Home & Progetti":
    st.subheader("I Nostri Universi Creativi")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>🎧 Musicalando</h3>
            <p>Musica d'autore, pop, urban napoletano e sonorità uniche prodotte con intelligenza artificiale e rifinite con cura sartoriale.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card">
            <h3>📖 AudioCalAI</h3>
            <p>Favole per bambini, racconti di viaggio e romanzi sonori immersivi (come 'Siberia On The Road').</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="card">
            <h3>🎙️ Storie nell'Ombra</h3>
            <p>Podcast True Crime, inchieste e vicende misteriose narrate con una cura audio cinematografica.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info("💡 **Novità:** Usa il menu a sinistra per navigare all'interno del catalogo completo delle produzioni.")

# SEZIONE CATALOGO
elif menu == "📂 Catalogo Completo":
    st.subheader("📂 Catalogo delle Opzioni e Produzioni")
    
    if df is not None:
        # Filtro di ricerca testuale avanzato
        search_query = st.text_input("🔍 Cerca per brano, genere o progetto:", "")
        
        if search_query:
            mask = df.astype(str).apply(lambda x: x.str.contains(search_query, case=False, na=False)).any(axis=1)
            filtered_df = df[mask]
        else:
            filtered_df = df
            
        st.dataframe(filtered_df, use_container_width=True)
        st.caption(f"Totale elementi visualizzati: {len(filtered_df)}")
    else:
        st.warning("⚠️ Il file 'CATALOGO.xlsx' non è stato trovato o non contiene dati corretti nel repository.")

# SEZIONE CHI SONO
elif menu == "ℹ️ Chi Sono":
    st.subheader("Informazioni sull'Artista")
    st.write("""
    Andrea Caliendo è un produttore indipendente, autore e sound designer attivo nella creazione di contenuti digitali avanzati, 
    musica multipiattaforma e narrazioni audio immersive.
    
    Tutti i brani e i podcast sono realizzati combinando tecniche di IA all'avanguardia con un meticoloso lavoro di mastering e post-produzione audio.
    """)
    st.markdown("---")
    st.write("🌐 **Canali ufficiali attivi:** Musicalando | AudioCalAI | Storie nell'Ombra")

# Footer in basso
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2026 Andrea Caliendo Official - Tutti i diritti riservati</p>", unsafe_allow_html=True)
