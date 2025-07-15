import streamlit as st

# Judul aplikasi
st.title("Bahaya pada Bahan Kimia")

# Data bahan kimia contoh
bahan_kimia = {
    "Benzena": {
        "Rumus": "C6H6",
        "Bahaya": "Karsinogen, mudah terbakar, dapat menyebabkan kanker dan iritasi kulit.",
        "Tindakan Pencegahan": "Gunakan alat pelindung diri, hindari inhalasi dan kontak langsung.",
        "Penyimpanan": "Simpan di tempat sejuk, jauh dari sumber api."
    },
    "Aseton": {
        "Rumus": "C3H6O",
        "Bahaya": "Mudah terbakar, mengiritasi mata dan saluran pernapasan.",
        "Tindakan Pencegahan": "Gunakan di area berventilasi, hindari kontak langsung dengan kulit.",
        "Penyimpanan": "Simpan di tempat sejuk dan tertutup rapat."
    },
    "Formaldehida": {
        "Rumus": "CH2O",
        "Bahaya": "Beracun dan karsinogen, dapat menyebabkan iritasi dan kanker.",
        "Tindakan Pencegahan": "Gunakan alat pelindung lengkap, hindari inhalasi.",
        "Penyimpanan": "Simpan di tempat tertutup dan dingin."
    }
}

# Input pencarian bahan kimia
nama_bahan = st.text_input("Masukkan nama bahan kimia:")

if nama_bahan:
    data = bahan_kimia.get(nama_bahan.title())
    if data:
        st.subheader(f"Informasi tentang {nama_bahan.title()}:")
        st.write(f"*Rumus Kimia:* {data['Rumus']}")
        st.write(f"*Bahaya:* {data['Bahaya']}")
        st.write(f"*Tindakan Pencegahan:* {data['Tindakan Pencegahan']}")
        st.write(f"*Penyimpanan:* {data['Penyimpanan']}")
    else:
        st.error("Data bahan kimia tidak ditemukan. Silakan coba nama lain.")
else:
    st.info("Masukkan nama bahan kimia untuk melihat informasinya.")
