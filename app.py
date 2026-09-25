import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Benzina Pistoia Smart", page_icon="⛽", layout="centered")

st.title("⛽ Previsione Benzina - Pistoia")
st.caption("Monitoraggio personale dei benzinai della tua zona")

# 1. Analisi Petrolio Brent
st.subheader("📊 Mercato Petrolio (Brent)")
try:
    brent = yf.Ticker("BZ=F")
    hist = brent.history(period="5d")
    if len(hist) >= 2:
        ultimo = hist['Close'].iloc[-1]
        precedente = hist['Close'].iloc[-2]
        var_percent = ((ultimo - precedente) / precedente) * 100

        col1, col2 = st.columns(2)
        col1.metric("Prezzo Brent", f"${ultimo:.2f}")
        col2.metric("Variazione 24h", f"{var_percent:+.2f}%")

        st.subheader("💡 Consigliere Smart")
        if var_percent < -1.5:
            st.success("🟢 **CONSIGLIO: ASPETTA!**\nIl petrolio è in calo netto. Nei prossimi 1-2 giorni le pompe di Pistoia dovrebbero abbassare i prezzi.")
        elif var_percent > 1.5:
            st.warning("🔴 **CONSIGLIO: FAI BENZINA OGGI!**\nIl petrolio è in forte rialzo. Probabile aumento del prezzo entro 24-48 ore.")
        else:
            st.info("🟡 **CONSIGLIO: SITUAZIONE STABILE**\nI mercati sono stabili. Fai rifornimento se ne hai bisogno.")
    else:
        st.write("Dati finanziari temporaneamente non disponibili.")
except Exception as e:
    st.error(f"Errore durante il recupero dei dati di mercato: {e}")

st.divider()

# 2. I tuoi 8 Benzinai a Pistoia
st.subheader("📍 I tuoi Benzinai a Pistoia")

distributori = [
    {"Nome": "IP", "Indirizzo": "Viale Antonelli 506", "Zona": "Pistoia Est"},
    {"Nome": "Eni", "Indirizzo": "Via G. Chirici 291", "Zona": "Pistoia Nord-Est"},
    {"Nome": "Esso", "Indirizzo": "Via Bartolomeo Sestini", "Zona": "Pistoia Est"},
    {"Nome": "Tamoil", "Indirizzo": "Via Maria Tasselli 187/233", "Zona": "Pistoia Est"},
    {"Nome": "Q8", "Indirizzo": "Via E. Fermi 2B", "Zona": "Zona Industriale Sant'Agostino"},
    {"Nome": "Eni", "Indirizzo": "Via E. Fermi 91", "Zona": "Zona Industriale Sant'Agostino"},
    {"Nome": "Eni", "Indirizzo": "Via Dalmazia 242", "Zona": "Pistoia Nord"},
    {"Nome": "Tamoil", "Indirizzo": "Via E. Fermi 91", "Zona": "Zona Industriale Sant'Agostino"}
]

df_benzinai = pd.DataFrame(distributori)
st.dataframe(df_benzinai, use_container_width=True, hide_index=True)

st.caption("Prototipo ad uso privato familiare - Pistoia")