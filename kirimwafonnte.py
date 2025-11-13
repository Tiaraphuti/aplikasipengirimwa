import streamlit as st
import pandas as pd
import requests

st.title("📱 Kirim Pesan WhatsApp via API")

token = st.text_input("Masukkan API Key:")
file = st.file_uploader("Upload file Excel", type=["xlsx"])

if file and token:
    data = pd.read_excel(file)
    st.dataframe(data)

    if st.button("Kirim Pesan"):
        for _, row in data.iterrows():
            nomor = row['nomor']
            pesan = row['pesan']
            # Contoh ke Fonnte API
            response = requests.post(
                "https://api.fonnte.com/send",
                headers={"Authorization": token},
                data={"target": nomor, "message": pesan}
            )
            st.write(f"Mengirim ke {nomor} → {response.status_code}")
        st.success("✅ Semua pesan dikirim!")
