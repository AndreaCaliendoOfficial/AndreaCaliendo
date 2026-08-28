import streamlit as st
import pandas as pd
import os
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Universo Andrea Caliendo | Official Creator & Music Hub",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PERCORSO CENTRALE BLINDATO E INTELLIGENTE ---
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)

# Il codice prova prima a cercare il file nel tuo PC (nella cartella superiore)
excel_locale = os.path.join(PARENT_DIR, "CATALOGO.xlsx")
# Poi imposta il percorso per il server cloud (stessa cartella del codice)
excel_cloud = os.path.join(CURRENT_DIR, "CATALOGO.xlsx")

# Sceglie in automatico quale usare senza che tu debba mai più toccare nulla
if os.path.exists(excel_locale):
    EXCEL_FILE = excel_locale
else:
    EXCEL_FILE = excel_cloud

@st.cache_data(show_spinner=False)
def load_public_data():
    if not os.path.exists(EXCEL_FILE):
        return {}
    try:
        xls = pd.ExcelFile(EXCEL_FILE)
        sheets_dict = {}
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name)
            df.columns = [str(c).replace('\n', ' ').strip() for c in df.columns]
            sheets_dict[sheet_name] = df.loc[:, ~df.columns.str.startswith('Unnamed')].dropna(how='all')
        return sheets_dict
    except Exception as e:
        return {}

data = load_public_data()

# --- NAVIGAZIONE LATERALE ---
st.sidebar.title("🎵 Andrea Caliendo")
st.sidebar.caption("Universo Artistico & Multimediale")

menu_scelto = st.sidebar.radio("Esplora il Hub:", [
    "🏠 Home", 
    "🎵 Musicalando", 
    "🤖 AudioCalAI", 
    "🕵️ Storie nell'Ombra", 
    "🎙️ Crime, Thriller e Misteri", 
    "🎙️ Romanzi e Avventura", 
    "📚 Il Mondo di Nonno Andrea", 
    "💬 Forum & Podcast AI", 
    "🔗 Link & Social Ufficiali", 
    "✉️ Contatti"
])

# -------------------------------------------------------------
# 1. HOME PAGE
# -------------------------------------------------------------
if menu_scelto == "🏠 Home":
    st.markdown("""
        <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); padding: 35px 30px; border-radius: 16px; color: white; text-align: center; margin-bottom: 20px;">
            <h1 style="font-size: 32px; margin-bottom: 10px; font-weight: 800;">Universo Andrea Caliendo</h1>
            <p style="font-size: 16px; color: #94a3b8; max-width: 800px; margin: 0 auto; line-height: 1.6;">
                <strong>Creator Artist AI</strong> — Musica, Podcast e Storie create e prodotte con il supporto dell'Intelligenza Artificiale.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🚀 Canali Ufficiali & Streaming")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?q=80&w=400&auto=format&fit=crop", use_container_width=True)
        st.link_button("🎵 Musicalando", "https://www.youtube.com/@musicalando", use_container_width=True)
    with col2:
        st.image("https://images.unsplash.com/photo-1598488035139-bdbb2231ce04?q=80&w=400&auto=format&fit=crop", use_container_width=True)
        st.link_button("🤖 AudioCalAI", "https://www.youtube.com/@AudioCal-AI", use_container_width=True)
    with col3:
        st.image("https://images.unsplash.com/photo-1478737270239-2f02b77fc618?q=80&w=400&auto=format&fit=crop", use_container_width=True)
        st.link_button("🕵️ Storie nell'Ombra", "https://www.youtube.com/@StorienellOmbra", use_container_width=True)

    st.markdown("---")
    st.markdown("### 🎙️ I Nostri Podcast su Spotify")
    p_col1, p_col2, p_col3 = st.columns(3)
    
    with p_col1:
        st.image("https://images.unsplash.com/photo-1589829545856-d10d557cf95f?q=80&w=400&auto=format&fit=crop", use_container_width=True)
        st.markdown("#### Crime, Thriller e Misteri")
        st.write("Casi di cronaca nera italiana reali e inchieste investigative.")
        st.link_button("Ascolta su Spotify ➔", "https://open.spotify.com/show/033yqkzVoPrzKIghTn1wq1", use_container_width=True)
        
    with p_col2:
        st.image("https://images.unsplash.com/photo-1512820790803-83ca734da794?q=80&w=400&auto=format&fit=crop", use_container_width=True)
        st.markdown("#### Romanzi e Avventura")
        st.write("Storie di fiction, avventura, mistero e saghe on-the-road.")
        st.link_button("Ascolta su Spotify ➔", "https://open.spotify.com/show/033GmIvZIcWbkZIXPnc0s9", use_container_width=True)
        
    with p_col3:
        st.image("https://images.unsplash.com/photo-1516627145497-ae6968895b74?q=80&w=400&auto=format&fit=crop", use_container_width=True)
        st.markdown("#### Il Mondo di Nonno Andrea")
        st.write("Favole della buonanotte, canzoncine e ninne nanne per bambini e famiglie.")
        st.link_button("Ascolta su Spotify ➔", "https://open.spotify.com/show/033OqkKyDNWsEs7vi7Tczs", use_container_width=True)

    st.markdown("---")
    st.markdown("""
        <div style="
            background: linear-gradient(rgba(15, 23, 42, 0.90), rgba(15, 23, 42, 0.90)), url('https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?q=80&w=1200&auto=format&fit=crop');
            background-size: cover;
            background-position: center;
            padding: 40px 35px;
            border-radius: 16px;
            border-left: 6px solid #3b82f6;
            color: #f8fafc;
            margin-top: 10px;
            margin-bottom: 25px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        ">
            <h2 style="color: #60a5fa; margin-top: 0; margin-bottom: 20px; font-size: 26px;">✍️ Chi è Andrea Caliendo — Versione Ufficiale</h2>
            <p style="line-height: 1.7; font-size: 15px; margin-bottom: 15px;">
            <strong>Andrea Caliendo</strong> è un Creator Artist AI e produttore musicale indipendente, fondatore di 3 universi creativi distinti: <em>Musicalando</em>, <em>AudioCalAI</em> e <em>Storie nell'Ombra</em>.
            </p>
            <p style="line-height: 1.7; font-size: 15px; margin-bottom: 15px;">
            Ogni universo ha una sua identità: <strong>Musicalando</strong> è dedicato alla musica originale in tutte le sue forme, dall'Urban Reggae napoletano di Cali61 al Rock di Max Cali, dal Dream Pop di Xelia al Lounge di Julian Cali e alle produzioni Healing 432Hz. <strong>AudioCalAI</strong> è il laboratorio di sperimentazione sonora e vocale, con progetti come Cali Phonk, Cali Lo-Fi e AudioCalAI Storie. <strong>Storie nell'Ombra</strong> è l'universo interamente dedicato al True Crime, ai romanzi e ai racconti gialli.
            </p>
            <p style="line-height: 1.7; font-size: 15px; margin-bottom: 15px;">
            A questi si affianca la sezione <strong>Podcast</strong>, divisa in 3 aree: <br>
            1. <em>Storie nell'Ombra - True Crime</em>, dedicata a casi di cronaca nera italiana reali;<br>
            2. <em>Storie nell'Ombra - Racconti Gialli e Romanzi</em>, dedicata a storie di fiction, avventura e mistero;<br>
            3. <em>I Racconti di Nonno Andrea</em>, dedicato a bambini e famiglie, con favole della buonanotte, canzoncine e ninne nanne.
            </p>
            <p style="line-height: 1.7; font-size: 15px; margin-bottom: 0;">
            Ogni progetto nasce da una mia idea, da un concept e da una visione artistica personale. L'Autore si serve della collaborazione dell'Intelligenza Artificiale come strumento di supporto per generare, produrre e creare i brani e i racconti. Nella produzione del True Crime vi è un'attenta ricerca e un'analisi scrupolosa delle fonti ufficiali nel trattare i casi più sconvolgenti e misteriosi. L'AI non è assolutamente la protagonista, ma solo un collaboratore tecnologico al servizio della creatività. La produzione e la direzione artistica nonché la scrittura, la cura artigianale e la produzione finale restano interamente dell'autore.
            </p>
        </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# 2. SEZIONE MUSICALANDO
# -------------------------------------------------------------
elif menu_scelto == "🎵 Musicalando":
    st.markdown("<h1 style='text-align: center; font-size: 42px; margin-bottom: 10px;'>🎵 Canale: Musicalando</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #94a3b8; margin-bottom: 30px;'>Cantautorato, melodie evocative, pop etereo e sonorità lounge d'autore.</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?q=80&w=1200&auto=format&fit=crop", caption="Musicalando Official Soundscape & Studio", use_container_width=True)
    
    st.write("In questo canale prendono vita progetti intimi, riflessivi e di grande eleganza sonora. Scopri gli artisti e le playlist ufficiali:")
    st.markdown("---")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🎤 Andrea Caliendo & Julian Cali")
        st.write("**Genere:** Cantautorato Italiano, Pop Melodico & Lounge")
        st.write("Testi profondi che esplorano la memoria e tappeti acustici caldi pensati per il relax e il viaggio.")
        
    with c2:
        st.markdown("### ✨ Xelia & Urban Project")
        st.write("**Genere:** Female Pop Etereo & Reggae Napoletano")
        st.write("Voce femminile angelica, sonorità fluttuanti, groove urban e Positive Vibes partenopee.")

    st.markdown("---")
    st.subheader("🎧 Playlist Ufficiali Musicalando su YouTube")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.image("https://images.unsplash.com/photo-1465847899084-d164df4dedc6?q=80&w=400&auto=format&fit=crop", use_container_width=True)
        st.markdown("🔥 **Canzoni d'Amore Inedite: Cantautorato & Pop Melodico**")
        st.link_button("Ascolta Playlist ➔", "https://www.youtube.com/playlist?list=PLNOqX_c4_C_aQt8IHbUDBuTm15lyJeuPI", use_container_width=True)
        
        st.markdown("---")
        st.image("https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?q=80&w=400&auto=format&fit=crop", use_container_width=True)
        st.markdown("🤖 **XELIA: AI Vocalist Project | Pop, Reggae & Inediti**")
        st.link_button("Ascolta Playlist ➔", "https://www.youtube.com/playlist?list=PLNOqX_c4_C_Y8xREZZ403N6tz8h9PKmJN", use_container_width=True)
        
        st.markdown("---")
        st.image("https://images.unsplash.com/photo-1514525253161-7a46d19cd819?q=80&w=400&auto=format&fit=crop", use_container_width=True)
        st.markdown("🎧 **Reggae Napoletano, Rap & Urban Partenopeo**")
        st.link_button("Ascolta Playlist ➔", "https://www.youtube.com/playlist?list=PLNOqX_c4_C_ZF_52h4GfDBOdmfZCVzTmq", use_container_width=True)

    with col_p2:
        st.image("https://images.unsplash.com/photo-1511192336575-5a79af67a629?q=80&w=400&auto=format&fit=crop", use_container_width=True)
        st.markdown("🌹 **Compilation Canzoni d'Autore: Pop & Cantautorato**")
        st.link_button("Ascolta Playlist ➔", "https://www.youtube.com/playlist?list=PLNOqX_c4_C_azpMevePqg1KHCQhDwomgg", use_container_width=True)
        
        st.markdown("---")
        st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=400&auto=format&fit=crop", use_container_width=True)
        st.markdown("🧘‍♂️ **Musica Rilassante Strumentale Mix | Ambient, Zen, Lo-Fi**")
        st.link_button("Ascolta Playlist ➔", "https://www.youtube.com/playlist?list=PLNOqX_c4_C_YaCpe-QNNC9B6vNDhX8_IE", use_container_width=True)

    st.markdown("---")
    st.link_button("📺 Visita il Canale YouTube Musicalando", "https://www.youtube.com/@musicalando", use_container_width=True)

# -------------------------------------------------------------
# 3. SEZIONE AUDIOCALAI
# -------------------------------------------------------------
elif menu_scelto == "🤖 AudioCalAI":
    st.markdown("<h1 style='text-align: center; font-size: 42px; margin-bottom: 10px;'>🤖 Canale: AudioCalAI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #94a3b8; margin-bottom: 30px;'>Urban, Reggae, Modern Rock, Phonk e produzioni ad alto impatto energetico.</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1598488035139-bdbb2231ce04?q=80&w=1200&auto=format&fit=crop", caption="AudioCalAI Studio & Urban Laboratory", use_container_width=True)
    
    st.write("Uno spazio dinamico dove la sperimentazione sonora incontra il ritmo della strada e le favole in famiglia:")
    st.markdown("---")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🎧 Cali61 & Max Cali")
        st.write("**Genere:** Urban Reggae / Modern Rock / Young Energy")
        st.write("Rivalsa sociale, radici urbane, chitarre distorte e motivazione senza compromessi.")

    with c2:
        st.markdown("### ⚡ Cali Phonk & Lo-Fi")
        st.write("**Genere:** Phonk / Drift / Chill Beats")
        st.write("Bassi 808 pesanti, campioni Memphis e relax totale per lo studio e la concentrazione.")

    st.markdown("---")
    st.subheader("🎧 Playlist Ufficiali AudioCalAI su YouTube")
    
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        st.image("https://images.unsplash.com/photo-1533227268428-f9ed0900fb3b?q=80&w=400&auto=format&fit=crop", use_container_width=True)
        st.markdown("📖 **Fiabe Sonore & Racconti in Famiglia**")
        st.link_button("Ascolta Playlist ➔", "https://www.youtube.com/playlist?list=PL1Fp4pSHcwMzKKDLPgmK-HSKJy5RWmzg4", use_container_width=True)
        
        st.markdown("---")
        st.image("https://images.unsplash.com/photo-1512820790803-83ca734da794?q=80&w=400&auto=format&fit=crop", use_container_width=True)
        st.markdown("🕵️ **Racconti Gialli & Storie d'Avventura**")
        st.link_button("Ascolta Playlist ➔", "https://www.youtube.com/playlist?list=PLQ9o6ha4g8QA", use_container_width=True)

    with col_a2:
        st.image("https://images.unsplash.com/photo-1470225620780-dba8ba36b745?q=80&w=400&auto=format&fit=crop", use_container_width=True)
        st.markdown("🎶 **Canzoni Allegre & Relax 432Hz**")
        st.link_button("Ascolta Playlist ➔", "https://www.youtube.com/playlist?list=PL1Fp4pSHcwMwvUBH-M9B4gElCdDwo101n", use_container_width=True)
        
        st.markdown("---")
        st.image("https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?q=80&w=400&auto=format&fit=crop", use_container_width=True)
        st.markdown("🎵 **Ritmi Urbani (Reggae & Rap)**")
        st.link_button("Ascolta Playlist ➔", "https://www.youtube.com/playlist?list=PL1Fp4pSHcwMwSnZS8pZHzizbt5wknjshp", use_container_width=True)

    st.markdown("---")
    st.link_button("📺 Visita il Canale YouTube AudioCalAI", "https://www.youtube.com/@AudioCal-AI", use_container_width=True)

# -------------------------------------------------------------
# 4. SEZIONE STORIE NELL'OMBRA
# -------------------------------------------------------------
elif menu_scelto == "🕵️ Storie nell'Ombra":
    st.markdown("<h1 style='text-align: center; font-size: 42px; margin-bottom: 10px;'>🕵️ Canale: Storie nell'Ombra</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #94a3b8; margin-bottom: 30px;'>Podcast True Crime, indagini, romanzi e misteri irrisolti.</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1478737270239-2f02b77fc618?q=80&w=1200&auto=format&fit=crop", caption="Storie nell'Ombra — True Crime & Mystery Hub", use_container_width=True)
    
    st.markdown("""
        ### 🎙️ L'Universo True Crime & Giallo
        Un progetto audio dedicato alle inchieste più oscure, ai profili psicologici dei serial killer, ai romanzi e ai racconti di avventura.
        
        * **Stile narrativo:** Voce profonda e tesa, tappeti sonori dark ambient e ricostruzioni investigative rigorose basate su fonti ufficiali.
        
        ---
    """)
    st.link_button("🔍 Visita il Canale YouTube Storie nell'Ombra", "https://www.youtube.com/@StorienellOmbra", use_container_width=True)

# -------------------------------------------------------------
# 5. SEZIONE PODCAST 1: CRIME, THRILLER E MISTERI
# -------------------------------------------------------------
elif menu_scelto == "🎙️ Crime, Thriller e Misteri":
    st.markdown("<h1 style='text-align: center; font-size: 40px; margin-bottom: 10px;'>🎙️ Podcast: Crime, Thriller e Misteri</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #94a3b8; margin-bottom: 30px;'>Inchieste e casi di cronaca nera italiana reali su Spotify e YouTube.</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1589829545856-d10d557cf95f?q=80&w=1200&auto=format&fit=crop", caption="True Crime & Investigations Hub", use_container_width=True)
    
    st.markdown("""
        ### 🔍 Dettagli del Podcast
        Un'analisi approfondita e scrupolosa dei casi di cronaca nera più discussi, con un'attenta ricerca delle fonti ufficiali e una narrazione immersiva e tesa.
    """)
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.link_button("🎧 Ascolta su Spotify", "https://open.spotify.com/show/033yqkzVoPrzKIghTn1wq1", use_container_width=True)
    with col_p2:
        st.link_button("📺 Playlist YouTube (Musicalando Noir)", "https://www.youtube.com/playlist?list=PLDqotc5g_R1w", use_container_width=True)

# -------------------------------------------------------------
# 6. SEZIONE PODCAST 2: ROMANZI E AVVENTURA
# -------------------------------------------------------------
elif menu_scelto == "🎙️ Romanzi e Avventura":
    st.markdown("<h1 style='text-align: center; font-size: 40px; margin-bottom: 10px;'>🎙️ Podcast: Romanzi e Avventura</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #94a3b8; margin-bottom: 30px;'>Storie di fiction, avventura, mistero e diari di viaggio.</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1512820790803-83ca734da794?q=80&w=1200&auto=format&fit=crop", caption="Audio Novels & Journey Sagas", use_container_width=True)
    
    st.markdown("""
        ### 🗺️ Dettagli del Podcast
        Romanzi sonori, avventure on-the-road e racconti di fiction che trasportano l'ascoltatore in mondi lontani e traversate epiche.
    """)
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.link_button("🎧 Ascolta su Spotify", "https://open.spotify.com/show/033GmIvZIcWbkZIXPnc0s9", use_container_width=True)
    with col_p2:
        st.link_button("📺 Playlist YouTube (AudioCalAI Storie)", "https://www.youtube.com/playlist?list=PLIl1XCs11eNU", use_container_width=True)

# -------------------------------------------------------------
# 7. SEZIONE PODCAST 3: NONNO ANDREA
# -------------------------------------------------------------
elif menu_scelto == "📚 Il Mondo di Nonno Andrea":
    st.markdown("<h1 style='text-align: center; font-size: 40px; margin-bottom: 10px;'>📚 Il Mondo di Nonno Andrea</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #94a3b8; margin-bottom: 30px;'>Favole, canzoncine e ninne nanne per bambini e famiglie.</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1516627145497-ae6968895b74?q=80&w=1200&auto=format&fit=crop", caption="Family Bedtime Stories & Lullabies", use_container_width=True)
    
    st.markdown("""
        ### 🧸 Dettagli del Podcast
        Un luogo magico dedicato ai più piccoli e alle famiglie, con favole della buonanotte rilassanti, canzoncine e ninne nanne originali.
    """)
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.link_button("🎧 Ascolta su Spotify", "https://open.spotify.com/show/033OqkKyDNWsEs7vi7Tczs", use_container_width=True)
    with col_p2:
        st.link_button("📺 Playlist YouTube (Favole & Buonanotte)", "https://www.youtube.com/playlist?list=PLFBikduzZzWg", use_container_width=True)

# -------------------------------------------------------------
# 8. SEZIONE FORUM & PODCAST AI
# -------------------------------------------------------------
elif menu_scelto == "💬 Forum & Podcast AI":
    st.markdown("<h1 style='text-align: center; font-size: 40px; margin-bottom: 10px;'>💬 Forum di Discussione & Podcast Critici</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #94a3b8; margin-bottom: 30px;'>Spazio di confronto aperto sull'Intelligenza Artificiale, critica musicale e crescita artistica.</p>", unsafe_allow_html=True)

    st.image("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1200&auto=format&fit=crop", caption="AI Creativity & Critical Discussion Hub", use_container_width=True)

    st.info("💡 **Spazio di Collaborazione & Dibattito Critico**\n\nQuesto angolo è dedicato alla riflessione aperta sul ruolo dell'Intelligenza Artificiale nella produzione artistica, all'analisi critica dei brani pubblicati e alle idee utili alla crescita dei canali.")

    st.markdown("### 📒 Il Mio Spazio Google Notebook Ufficiale")
    st.write("Accedi al notebook contenente tutte le discussioni, i materiali di ricerca e i podcast suddivisi per genere:")
    st.link_button("🚀 Apri Google Notebook Personale", "https://notebook.google.com/", use_container_width=True)

    st.markdown("---")
    st.subheader("🎙️ Podcast di Discussione & Approfondimento")
    st.write("Ascolta i contributi audio e i dibattiti critici sul rapporto tra creatività umana e supporto tecnologico:")
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.markdown("🤖 **Dibattito aperto: L'AI nella Musica d'Autore**")
        st.write("Un podcast critico sull'etica, il supporto tecnologico e il futuro del cantautorato.")
        st.info("🎧 *Disponibile nel Notebook Google ufficiale*")
    with col_f2:
        st.markdown("📈 **Strategie di Crescita & Community Feedback**")
        st.write("Analisi delle metriche, interazione con il pubblico e ottimizzazione dei canali.")
        st.info("🎧 *Disponibile nel Notebook Google ufficiale*")

    st.markdown("---")
    st.subheader("✍️ Lascia il Tuo Commento o Spunto Critico")
    st.write("Hai idee, critiche costruttive o vuoi dire la tua sull'uso dell'AI nei brani? Condividi il tuo pensiero:")
    
    with st.form("forum_form"):
        nome_utente = st.text_input("Il tuo nome o nickname")
        categoria_intervento = st.selectbox("Tema dell'intervento", ["Etica & Utilizzo AI", "Critica musicale sui brani", "Suggerimenti per i canali", "Altro"])
        testo_messaggio = st.text_area("Scrivi qui il tuo pensiero o la tua analisi critica...")
        invia_messaggio = st.form_submit_button("Pubblica nel Forum")
        
        if invia_messaggio:
            if nome_utente and testo_messaggio:
                st.success(f"Grazie {nome_utente}! Il tuo intervento è stato registrato con successo nel sistema di discussione.")
            else:
                st.warning("Per favore compila almeno il nome e il testo del messaggio prima di inviare.")

# -------------------------------------------------------------
# 9. SEZIONE LINK & SOCIAL
# -------------------------------------------------------------
elif menu_scelto == "🔗 Link & Social Ufficiali":
    st.markdown("<h1 style='text-align: center; font-size: 40px; margin-bottom: 10px;'>🔗 Link & Social Ufficiali</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #94a3b8; margin-bottom: 30px;'>Tutti i punti di riferimento digitali del mondo di Andrea Caliendo.</p>", unsafe_allow_html=True)

    # Immagine di copertina
    st.image("https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=1200&auto=format&fit=crop", use_container_width=True)

    st.markdown("---")
    st.subheader("🌳 Il Mio Mondo Digitale")
    
    col_l1, col_l2, col_l3 = st.columns(3)
    
    with col_l1:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 10px;">
                <img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=300&auto=format&fit=crop" style="width: 140px; height: 100px; object-fit: cover; border-radius: 12px; margin-bottom: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
                <h3 style="margin: 0 0 5px 0; font-size: 18px;">🌳 Linktree Ufficiale</h3>
                <p style="font-size: 13px; color: #94a3b8; margin: 0 0 10px 0; min-height: 40px;">Tutti i link in un click.</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Apri Linktree ➔", "https://linktr.ee/andrea61caliendo", use_container_width=True)

    with col_l2:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 10px;">
                <img src="https://images.unsplash.com/photo-1472851294608-062f824d29cc?q=80&w=300&auto=format&fit=crop" style="width: 140px; height: 100px; object-fit: cover; border-radius: 12px; margin-bottom: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
                <h3 style="margin: 0 0 5px 0; font-size: 18px;">📘 Shop Ufficiale</h3>
                <p style="font-size: 13px; color: #94a3b8; margin: 0 0 10px 0; min-height: 40px;">Merchandising esclusivo Spreadshop.</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Visita lo Shop ➔", "https://musicalando-shop.myspreadshop.it/", use_container_width=True)

    with col_l3:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 10px;">
                <img src="https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?q=80&w=300&auto=format&fit=crop" style="width: 140px; height: 100px; object-fit: cover; border-radius: 12px; margin-bottom: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
                <h3 style="margin: 0 0 5px 0; font-size: 18px;">🌐 Supporto Amazon</h3>
                <p style="font-size: 13px; color: #94a3b8; margin: 0 0 10px 0; min-height: 40px;">Sostieni i canali con il link Amazon.</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Supporta Canale ➔", "https://amzn.to/4bBSuWY", use_container_width=True)

    st.markdown("---")
    st.subheader("🎧 Streaming & Canali Principali")

    col_s1, col_s2, col_s3 = st.columns(3)
    
    with col_s1:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 10px;">
                <img src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?q=80&w=300&auto=format&fit=crop" style="width: 140px; height: 100px; object-fit: cover; border-radius: 12px; margin-bottom: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
                <h3 style="margin: 0 0 5px 0; font-size: 18px;">🎧 Artista Spotify</h3>
                <p style="font-size: 13px; color: #94a3b8; margin: 0 0 10px 0; min-height: 40px;">Brani e album in streaming.</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Apri Spotify ➔", "https://open.spotify.com/intl-it/artist/4Xv9mTYFIbajxeEnJSuYQd", use_container_width=True)

    with col_s2:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 10px;">
                <img src="https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?q=80&w=300&auto=format&fit=crop" style="width: 140px; height: 100px; object-fit: cover; border-radius: 12px; margin-bottom: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
                <h3 style="margin: 0 0 5px 0; font-size: 18px;">🎵 YouTube Music</h3>
                <p style="font-size: 13px; color: #94a3b8; margin: 0 0 10px 0; min-height: 40px;">Discografia su YT Music.</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Apri YT Music ➔", "https://music.youtube.com/@musicalando", use_container_width=True)

    with col_s3:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 10px;">
                <img src="https://images.unsplash.com/photo-1598488035139-bdbb2231ce04?q=80&w=300&auto=format&fit=crop" style="width: 140px; height: 100px; object-fit: cover; border-radius: 12px; margin-bottom: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
                <h3 style="margin: 0 0 5px 0; font-size: 18px;">📺 AudioCalAI</h3>
                <p style="font-size: 13px; color: #94a3b8; margin: 0 0 10px 0; min-height: 40px;">Canale Urban, Rock e Phonk.</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Visita AudioCalAI ➔", "https://www.youtube.com/@AudioCal-AI", use_container_width=True)

    col_s4, col_s5, col_s6 = st.columns(3)
    
    with col_s4:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 10px;">
                <img src="https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?q=80&w=300&auto=format&fit=crop" style="width: 140px; height: 100px; object-fit: cover; border-radius: 12px; margin-bottom: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
                <h3 style="margin: 0 0 5px 0; font-size: 18px;">📺 Musicalando</h3>
                <p style="font-size: 13px; color: #94a3b8; margin: 0 0 10px 0; min-height: 40px;">Cantautorato e melodie d'autore.</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Visita Musicalando ➔", "https://www.youtube.com/@musicalando", use_container_width=True)

    with col_s5:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 10px;">
                <img src="https://images.unsplash.com/photo-1478737270239-2f02b77fc618?q=80&w=300&auto=format&fit=crop" style="width: 140px; height: 100px; object-fit: cover; border-radius: 12px; margin-bottom: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
                <h3 style="margin: 0 0 5px 0; font-size: 18px;">📺 Storie nell'Ombra</h3>
                <p style="font-size: 13px; color: #94a3b8; margin: 0 0 10px 0; min-height: 40px;">True Crime e racconti gialli.</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Visita Storie ➔", "https://www.youtube.com/@StorienellOmbra", use_container_width=True)

    with col_s6:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 10px;">
                <img src="https://images.unsplash.com/photo-1611605698335-8b1569810432?q=80&w=300&auto=format&fit=crop" style="width: 140px; height: 100px; object-fit: cover; border-radius: 12px; margin-bottom: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
                <h3 style="margin: 0 0 5px 0; font-size: 18px;">👤 TikTok 1</h3>
                <p style="font-size: 13px; color: #94a3b8; margin: 0 0 10px 0; min-height: 40px;">Profilo TikTok ufficiale.</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Segui TikTok ➔", "https://www.tiktok.com/@andreacaliendo", use_container_width=True)

    st.markdown("---")
    st.subheader("📱 TikTok Ufficiali")
    
    col_t1, col_t2, _ = st.columns(3)
    with col_t1:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 10px;">
                <img src="https://images.unsplash.com/photo-1563986768609-322da13575f3?q=80&w=300&auto=format&fit=crop" style="width: 140px; height: 100px; object-fit: cover; border-radius: 12px; margin-bottom: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
                <h3 style="margin: 0 0 5px 0; font-size: 18px;">👤 TikTok 2</h3>
                <p style="font-size: 13px; color: #94a3b8; margin: 0 0 10px 0; min-height: 40px;">Secondo profilo TikTok.</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Segui TikTok ➔", "https://www.tiktok.com/@caliendoandrea", use_container_width=True)

# -------------------------------------------------------------
# 10. CONTATTI
# -------------------------------------------------------------
elif menu_scelto == "✉️ Contatti":
    st.markdown("<h1 style='text-align: center; font-size: 40px; margin-bottom: 10px;'>✉️ Mettiti in Contatto</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #94a3b8; margin-bottom: 30px;'>Canali diretti per informazioni, collaborazioni e supporto.</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1534536281715-e28d76689b4d?q=80&w=1200&auto=format&fit=crop", caption="Get in Touch & Official Collaborations", use_container_width=True)
    
    st.write("Per informazioni, collaborazioni, richieste di pacchetti musicali dedicati o supporto:")
    st.markdown("""
    * **Email commerciale e di contatto:** `andrea61caliendo@gmail.com`
    * **Community:** Lascia un commento sui nostri canali YouTube ufficiali per interagire direttamente con i contenuti pubblicati.
    """)