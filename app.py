import streamlit as st

# Judul aplikasi
st.title("Bahaya pada Bahan Kimia")

# Data bahan kimia contoh
bahan_kimia = {
  {
    "No":1,
    "Bahan":"Benzena",
    "Bahaya":"Karsinogen, mudah terbakar"
  },
  {
    "No":2,
    "Bahan":"Toluena",
    "Bahaya":"Iritasi pernapasan, neurotoksik"
  },
  {
    "No":3,
    "Bahan":"Xilena",
    "Bahaya":"Beracun, mudah terbakar"
  },
  {
    "No":4,
    "Bahan":"Fenol",
    "Bahaya":"Korosif, beracun"
  },
  {
    "No":5,
    "Bahan":"Anilin",
    "Bahaya":"Beracun, dapat diserap kulit"
  },
  {
    "No":6,
    "Bahan":"Formaldehida",
    "Bahaya":"Karsinogen, iritasi kuat"
  },
  {
    "No":7,
    "Bahan":"Aseton",
    "Bahaya":"Mudah terbakar, iritasi"
  },
  {
    "No":8,
    "Bahan":"Metanol",
    "Bahaya":"Beracun, risiko kebutaan"
  },
  {
    "No":9,
    "Bahan":"Etanol",
    "Bahaya":"Mudah terbakar, iritasi mata"
  },
  {
    "No":10,
    "Bahan":"Propanol",
    "Bahaya":"Mudah terbakar, iritasi"
  },
  {
    "No":11,
    "Bahan":"Butanol",
    "Bahaya":"Mudah terbakar, iritasi"
  },
  {
    "No":12,
    "Bahan":"Asam asetat",
    "Bahaya":"Korosif, iritasi saluran napas"
  },
  {
    "No":13,
    "Bahan":"Akrilonitril",
    "Bahaya":"Karsinogen, mudah terbakar"
  },
  {
    "No":14,
    "Bahan":"Etilena Oksida",
    "Bahaya":"Karsinogen, reaktif"
  },
  {
    "No":15,
    "Bahan":"Stirena",
    "Bahaya":"Iritasi pernapasan, neurotoksik"
  },
  {
    "No":16,
    "Bahan":"Asam benzoat",
    "Bahaya":"Iritasi kulit, mata"
  },
  {
    "No":17,
    "Bahan":"Asam sitrat",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":18,
    "Bahan":"Asam format",
    "Bahaya":"Korosif, toksik"
  },
  {
    "No":19,
    "Bahan":"Asam laktat",
    "Bahaya":"Iritasi kulit"
  },
  {
    "No":20,
    "Bahan":"Asam oksalat",
    "Bahaya":"Beracun, korosif"
  },
  {
    "No":21,
    "Bahan":"Kloroform",
    "Bahaya":"Karsinogen, toksik hati"
  },
  {
    "No":22,
    "Bahan":"Karbon tetraklorida",
    "Bahaya":"Karsinogen, hepatotoksik"
  },
  {
    "No":23,
    "Bahan":"Dietil eter",
    "Bahaya":"Mudah terbakar, anestetik"
  },
  {
    "No":24,
    "Bahan":"Metil etil keton",
    "Bahaya":"Iritasi pernapasan"
  },
  {
    "No":25,
    "Bahan":"Piridin",
    "Bahaya":"Toksik, mudah terbakar"
  },
  {
    "No":26,
    "Bahan":"Nitrobenzena",
    "Bahaya":"Karsinogen, sangat toksik"
  },
  {
    "No":27,
    "Bahan":"Asam pikrat",
    "Bahaya":"Eksplosif, toksik"
  },
  {
    "No":28,
    "Bahan":"Tetrahidrofuran",
    "Bahaya":"Mudah terbakar, iritasi"
  },
  {
    "No":29,
    "Bahan":"Dimetil sulfoksida",
    "Bahaya":"Penyerapan kulit cepat"
  },
  {
    "No":30,
    "Bahan":"Asam salisilat",
    "Bahaya":"Iritasi kulit, mata"
  },
  {
    "No":31,
    "Bahan":"Toluidina",
    "Bahaya":"Toksik, karsinogen"
  },
  {
    "No":32,
    "Bahan":"Kresol",
    "Bahaya":"Korosif, toksik"
  },
  {
    "No":33,
    "Bahan":"Nafthalen",
    "Bahaya":"Karsinogen, iritasi"
  },
  {
    "No":34,
    "Bahan":"Ftalat",
    "Bahaya":"Toksik reproduksi"
  },
  {
    "No":35,
    "Bahan":"Butil asetat",
    "Bahaya":"Mudah terbakar, iritasi"
  },
  {
    "No":36,
    "Bahan":"Heptana",
    "Bahaya":"Mudah terbakar, narkotik"
  },
  {
    "No":37,
    "Bahan":"Nonana",
    "Bahaya":"Mudah terbakar, narkotik"
  },
  {
    "No":38,
    "Bahan":"Dekana",
    "Bahaya":"Mudah terbakar"
  },
  {
    "No":39,
    "Bahan":"Isoprena",
    "Bahaya":"Mudah terbakar, karsinogen"
  },
  {
    "No":40,
    "Bahan":"Klorobenzena",
    "Bahaya":"Iritasi, toksik"
  },
  {
    "No":41,
    "Bahan":"Diklorometana",
    "Bahaya":"Toksik, karsinogen"
  },
  {
    "No":42,
    "Bahan":"Metil isobutil keton",
    "Bahaya":"Iritasi, narkotik"
  },
  {
    "No":43,
    "Bahan":"Propilena glikol",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":44,
    "Bahan":"Gliserol",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":45,
    "Bahan":"Asam oleat",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":46,
    "Bahan":"Asam palmitat",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":47,
    "Bahan":"Asam stearat",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":48,
    "Bahan":"Vinil klorida",
    "Bahaya":"Karsinogen, mudah terbakar"
  },
  {
    "No":49,
    "Bahan":"Akrilamida",
    "Bahaya":"Karsinogen, neurotoksik"
  },
  {
    "No":50,
    "Bahan":"Bisfenol A",
    "Bahaya":"Toksik reproduksi"
  },
  {
    "No":51,
    "Bahan":"Antracena",
    "Bahaya":"Karsinogen, iritasi"
  },
  {
    "No":52,
    "Bahan":"Fenantrena",
    "Bahaya":"Karsinogen, iritasi"
  },
  {
    "No":53,
    "Bahan":"Pirena",
    "Bahaya":"Karsinogen, iritasi"
  },
  {
    "No":54,
    "Bahan":"Fluorena",
    "Bahaya":"Iritasi, karsinogen"
  },
  {
    "No":55,
    "Bahan":"Indena",
    "Bahaya":"Iritasi"
  },
  {
    "No":56,
    "Bahan":"Kumarina",
    "Bahaya":"Iritasi, hepatotoksik"
  },
  {
    "No":57,
    "Bahan":"Resorsinol",
    "Bahaya":"Korosif, iritasi"
  },
  {
    "No":58,
    "Bahan":"Hidrokuinon",
    "Bahaya":"Korosif, iritasi"
  },
  {
    "No":59,
    "Bahan":"Tereftalat",
    "Bahaya":"Toksik reproduksi"
  },
  {
    "No":60,
    "Bahan":"Asam adipat",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":61,
    "Bahan":"Asam maleat",
    "Bahaya":"Korosif, iritasi"
  },
  {
    "No":62,
    "Bahan":"Asam fumarat",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":63,
    "Bahan":"Asam itakonat",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":64,
    "Bahan":"Asam tartarat",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":65,
    "Bahan":"Maltol",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":66,
    "Bahan":"Sorbitol",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":67,
    "Bahan":"Mannitol",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":68,
    "Bahan":"Trehalosa",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":69,
    "Bahan":"Sukrosa",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":70,
    "Bahan":"Ribosa",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":71,
    "Bahan":"Galaktosa",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":72,
    "Bahan":"Fruktosa",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":73,
    "Bahan":"Glukosa",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":74,
    "Bahan":"Laktosa",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":75,
    "Bahan":"Selulosa",
    "Bahaya":"Iritasi debu"
  },
  {
    "No":76,
    "Bahan":"Lignin",
    "Bahaya":"Iritasi debu"
  },
  {
    "No":77,
    "Bahan":"Pektin",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":78,
    "Bahan":"Agar-agar",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":79,
    "Bahan":"Kitosan",
    "Bahaya":"Iritasi debu"
  },
  {
    "No":80,
    "Bahan":"Asam hialuronat",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":81,
    "Bahan":"Keratin",
    "Bahaya":"Iritasi debu"
  },
  {
    "No":82,
    "Bahan":"Kasein",
    "Bahaya":"Iritasi debu"
  },
  {
    "No":83,
    "Bahan":"Albumin",
    "Bahaya":"Iritasi debu"
  },
  {
    "No":84,
    "Bahan":"Gelatin",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":85,
    "Bahan":"Peptida",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":86,
    "Bahan":"Polipeptida",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":87,
    "Bahan":"Polisakarida",
    "Bahaya":"Iritasi debu"
  },
  {
    "No":88,
    "Bahan":"Dekstrin",
    "Bahaya":"Iritasi debu"
  },
  {
    "No":89,
    "Bahan":"Glikogen",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":90,
    "Bahan":"Histamin",
    "Bahaya":"Alergi, iritasi"
  },
  {
    "No":91,
    "Bahan":"Adrenalin",
    "Bahaya":"Toksik dosis tinggi"
  },
  {
    "No":92,
    "Bahan":"Tirosin",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":93,
    "Bahan":"Triptofan",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":94,
    "Bahan":"Glutamat",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":95,
    "Bahan":"Asam aspartat",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":96,
    "Bahan":"Arginin",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":97,
    "Bahan":"Lisina",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":98,
    "Bahan":"Leusina",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":99,
    "Bahan":"Valina",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":100,
    "Bahan":"Alanina",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":101,
    "Bahan":"Serina",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":102,
    "Bahan":"Sisteina",
    "Bahaya":"Bau menyengat, iritasi"
  },
  {
    "No":103,
    "Bahan":"Metionina",
    "Bahaya":"Bau menyengat, iritasi"
  },
  {
    "No":104,
    "Bahan":"Fenilalanina",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":105,
    "Bahan":"Glutamin",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":106,
    "Bahan":"Prolina",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":107,
    "Bahan":"Asam propionat",
    "Bahaya":"Korosif, iritasi"
  },
  {
    "No":108,
    "Bahan":"Asam kaproat",
    "Bahaya":"Iritasi, bau busuk"
  },
  {
    "No":109,
    "Bahan":"Asam kaprilat",
    "Bahaya":"Iritasi, bau busuk"
  },
  {
    "No":110,
    "Bahan":"Asam laurat",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":111,
    "Bahan":"Asam miristat",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":112,
    "Bahan":"Asam arakidat",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":113,
    "Bahan":"Asam linoleat",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":114,
    "Bahan":"Asam linolenat",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":115,
    "Bahan":"Asam eikosapentaenoat",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":116,
    "Bahan":"Asam dokosaheksaenoat",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":117,
    "Bahan":"Karbamazepin",
    "Bahaya":"Toksik, neurotoksik"
  },
  {
    "No":118,
    "Bahan":"Kafeina",
    "Bahaya":"Stimulasi berlebih"
  },
  {
    "No":119,
    "Bahan":"Teobromina",
    "Bahaya":"Stimulasi, toksik hewan"
  },
  {
    "No":120,
    "Bahan":"Nikotina",
    "Bahaya":"Sangat toksik, adiktif"
  },
  {
    "No":121,
    "Bahan":"Morfina",
    "Bahaya":"Adiktif, depresan"
  },
  {
    "No":122,
    "Bahan":"Kodeina",
    "Bahaya":"Adiktif, depresan"
  },
  {
    "No":123,
    "Bahan":"Heroin",
    "Bahaya":"Sangat adiktif, ilegal"
  },
  {
    "No":124,
    "Bahan":"LSD (asam lisergat)",
    "Bahaya":"Halusinogen, ilegal"
  },
  {
    "No":125,
    "Bahan":"THC (tetrahidrokanabinol)",
    "Bahaya":"Psikoaktif"
  },
  {
    "No":126,
    "Bahan":"Psilosibin",
    "Bahaya":"Halusinogen"
  },
  {
    "No":127,
    "Bahan":"Mescalina",
    "Bahaya":"Halusinogen"
  },
  {
    "No":128,
    "Bahan":"Efedrina",
    "Bahaya":"Stimulasi, toksik dosis tinggi"
  },
  {
    "No":129,
    "Bahan":"Amfetamina",
    "Bahaya":"Adiktif, stimulan kuat"
  },
  {
    "No":130,
    "Bahan":"Metamfetamina",
    "Bahaya":"Adiktif, stimulan ilegal"
  },
  {
    "No":131,
    "Bahan":"MDMA (ekstasi)",
    "Bahaya":"Psikoaktif, neurotoksik"
  },
  {
    "No":132,
    "Bahan":"Dimetiltriptamina",
    "Bahaya":"Halusinogen"
  },
  {
    "No":133,
    "Bahan":"Beta-karoten",
    "Bahaya":"Iritasi debu"
  },
  {
    "No":134,
    "Bahan":"Retinol",
    "Bahaya":"Toksik dosis tinggi"
  },
  {
    "No":135,
    "Bahan":"Ergosterol",
    "Bahaya":"Iritasi"
  },
  {
    "No":136,
    "Bahan":"Kolesterol",
    "Bahaya":"Iritasi debu"
  },
  {
    "No":137,
    "Bahan":"Lanosterol",
    "Bahaya":"Iritasi debu"
  },
  {
    "No":138,
    "Bahan":"Sitosterol",
    "Bahaya":"Iritasi ringan"
  },
  {
    "No":139,
    "Bahan":"Kapsaisin",
    "Bahaya":"Iritasi kulit, mata"
  },
  {
    "No":140,
    "Bahan":"Piperina",
    "Bahaya":"Iritasi hidung, mata"
  },
  {
    "No":141,
    "Bahan":"Eugenol",
    "Bahaya":"Iritasi kulit"
  },
  {
    "No":142,
    "Bahan":"Limonena",
    "Bahaya":"Iritasi, mudah terbakar"
  },
  {
    "No":143,
    "Bahan":"Linalool",
    "Bahaya":"Iritasi kulit"
  },
  {
    "No":144,
    "Bahan":"Geraniol",
    "Bahaya":"Iritasi kulit"
  },
  {
    "No":145,
    "Bahan":"Citronellol",
    "Bahaya":"Iritasi kulit"
  },
  {
    "No":146,
    "Bahan":"Mentol",
    "Bahaya":"Iritasi, pendingin"
  },
  {
    "No":147,
    "Bahan":"Kamfer",
    "Bahaya":"Iritasi, neurotoksik dosis tinggi"
  },
  {
    "No":148,
    "Bahan":"Thujon",
    "Bahaya":"Neurotoksik"
  },
  {
    "No":149,
    "Bahan":"Safrol",
    "Bahaya":"Karsinogen"
  },
  {
    "No":150,
    "Bahan":"Kumena",
    "Bahaya":"Iritasi, mudah terbakar"
  }
]

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
