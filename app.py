import streamlit as st

# Judul aplikasi
st.title("Bahaya pada Bahan Kimia")

# Data bahan kimia contoh
bahan_kimia = {
    "Nama": "Benzena"{
    "Rumus": "C6H6",
    "Bahaya": "Karsinogen, mudah terbakar, iritasi kulit dan saluran pernapasan.",
    "Tindakan Pencegahan": "Gunakan APD, hindari inhalasi dan kontak langsung.",
    "Penyimpanan": "Simpan di tempat sejuk dan jauh dari api."
  },
  
    "Nama": "Toluena"{,
    "Rumus": "C7H8",
    "Bahaya": "Mudah terbakar, dapat menyebabkan pusing dan iritasi pernapasan.",
    "Tindakan Pencegahan": "Gunakan masker dan ventilasi baik.",
    "Penyimpanan": "Simpan jauh dari sumber api."
  },
   
    "Nama": "Xilena"{,
    "Rumus": "C8H10",
    "Bahaya": "Iritasi kulit, mata, dan saluran pernapasan, beracun jika tertelan.",
    "Tindakan Pencegahan": "Gunakan sarung tangan dan ventilasi baik.",
    "Penyimpanan": "Simpan di tempat sejuk dan tertutup rapat."
  },
  
    "Nama": "Metanol"{,
    "Rumus": "CH3OH",
    "Bahaya": "Beracun jika tertelan, dapat menyebabkan kebutaan dan kematian.",
    "Tindakan Pencegahan": "Hindari konsumsi dan kontak kulit, gunakan ventilasi baik.",
    "Penyimpanan": "Simpan di tempat tertutup dan jauh dari api."
  },
 
    "Nama": "Etil asetat"{,
    "Rumus": "C4H8O2",
    "Bahaya": "Mudah menguap dan mudah terbakar, dapat menyebabkan iritasi mata dan pernapasan.",
    "Tindakan Pencegahan": "Gunakan di area berventilasi, hindari kontak langsung.",
    "Penyimpanan": "Simpan di tempat tertutup dan sejuk."
  },
  
    "Nama": "Formaldehida"{,
    "Rumus": "CH2O",
    "Bahaya": "Karsinogen, iritasi kulit dan saluran pernapasan.",
    "Tindakan Pencegahan": "Gunakan APD lengkap, hindari inhalasi.",
    "Penyimpanan": "Simpan di tempat gelap dan dingin."
  },
  
    "Nama": "Asam asetat"{,
    "Rumus": "CH3COOH",
    "Bahaya": "Iritasi kulit dan mata, korosif pada konsentrasi tinggi.",
    "Tindakan Pencegahan": "Gunakan sarung tangan dan pelindung mata.",
    "Penyimpanan": "Simpan dalam wadah tertutup rapat."
  },
  
    "Nama": "Aseton"{,
    "Rumus": "C3H6O",
    "Bahaya": "Mudah terbakar, iritasi mata dan pernapasan.",
    "Tindakan Pencegahan": "Gunakan di area berventilasi, hindari kontak langsung.",
    "Penyimpanan": "Simpan jauh dari sumber api."
  },
  
    "Nama": "Fenol"{,
    "Rumus": "C6H5OH",
    "Bahaya": "Beracun, korosif, dapat menyebabkan luka bakar kulit.",
    "Tindakan Pencegahan": "Gunakan APD lengkap, hindari kontak langsung.",
    "Penyimpanan": "Simpan di tempat sejuk dan tertutup rapat."
  },
  
    "Nama": "Kloroform"{,
    "Rumus": "CHCl3",
    "Bahaya": "Beracun, karsinogen, dapat menyebabkan kerusakan hati.",
    "Tindakan Pencegahan": "Gunakan APD dan ventilasi baik.",
    "Penyimpanan": "Simpan di tempat gelap dan sejuk."
  },
  
    "Nama": "Etilena glikol"{,
    "Rumus": "C2H6O2",
    "Bahaya": "Beracun jika tertelan, menyebabkan gagal ginjal.",
    "Tindakan Pencegahan": "Gunakan sarung tangan, hindari konsumsi.",
    "Penyimpanan": "Simpan di tempat sejuk dan berventilasi."
  },
  
    "Nama": "Asam format"{,
    "Rumus": "HCOOH",
    "Bahaya": "Korosif, dapat menyebabkan iritasi dan luka bakar.",
    "Tindakan Pencegahan": "Gunakan pelindung mata dan sarung tangan.",
    "Penyimpanan": "Simpan dalam wadah tertutup."
  },
  
    "Nama": "Stirena"{,
    "Rumus": "C8H8",
    "Bahaya": "Mudah terbakar, iritasi kulit dan pernapasan.",
    "Tindakan Pencegahan": "Gunakan ventilasi baik dan hindari kontak kulit.",
    "Penyimpanan": "Simpan jauh dari api dan panas."
  },
  
    "Nama": "Keton metil etil"{,
    "Rumus": "C4H8O",
    "Bahaya": "Mudah terbakar, mengiritasi mata dan pernapasan.",
    "Tindakan Pencegahan": "Gunakan alat pelindung dan ventilasi baik.",
    "Penyimpanan": "Simpan tertutup dan jauh dari api."
  },
  
    "Nama": "Nitrobenzena"{,
    "Rumus": "C6H5NO2",
    "Bahaya": "Beracun, dapat menyebabkan keracunan darah.",
    "Tindakan Pencegahan": "Gunakan APD lengkap dan hindari inhalasi.",
    "Penyimpanan": "Simpan di tempat sejuk dan tertutup."
  },
  
    "Nama": "Asam benzoat"{,
    "Rumus": "C7H6O2",
    "Bahaya": "Dapat menyebabkan iritasi kulit dan mata.",
    "Tindakan Pencegahan": "Gunakan sarung tangan dan kacamata pelindung.",
    "Penyimpanan": "Simpan di tempat kering dan tertutup."
  },
  
    "Nama": "Asam salisilat"{,
    "Rumus": "C7H6O3",
    "Bahaya": "Dapat menyebabkan iritasi kulit dan reaksi alergi.",
    "Tindakan Pencegahan": "Gunakan sarung tangan, hindari kontak langsung.",
    "Penyimpanan": "Simpan di tempat sejuk dan kering."
  },
  
    "Nama": "Etil alkohol (etanol)"{,
    "Rumus": "C2H5OH",
    "Bahaya": "Mudah terbakar, mengiritasi mata dan kulit.",
    "Tindakan Pencegahan": "Hindari sumber api, gunakan ventilasi baik.",
    "Penyimpanan": "Simpan di tempat sejuk dan tertutup."
  },
  
    "Nama": "Asam propionat"{,
    "Rumus": "C3H6O2",
    "Bahaya": "Iritasi kulit dan mata.",
    "Tindakan Pencegahan": "Gunakan pelindung mata dan sarung tangan.",
    "Penyimpanan": "Simpan di tempat sejuk dan tertutup."
  },
  
    "Nama": "Asam format metil"{,
    "Rumus": "HCOOCH3",
    "Bahaya": "Iritasi pada kulit dan mata, mudah terbakar.",
    "Tindakan Pencegahan": "Gunakan APD dan ventilasi baik.",
    "Penyimpanan": "Simpan jauh dari sumber api."
  },
  
    "Nama": "Isopropanol"{,
    "Rumus": "C3H8O",
    "Bahaya": "Mudah terbakar, mengiritasi mata dan saluran pernapasan.",
    "Tindakan Pencegahan": "Gunakan di area berventilasi, hindari kontak langsung.",
    "Penyimpanan": "Simpan tertutup dan jauh dari api."
  },
  
    "Nama": "Asam klorida asetat"{,
    "Rumus": "CH2ClCOOH",
    "Bahaya": "Korosif, menyebabkan iritasi dan luka bakar.",
    "Tindakan Pencegahan": "Gunakan pelindung mata dan sarung tangan.",
    "Penyimpanan": "Simpan di tempat tertutup dan sejuk."
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
