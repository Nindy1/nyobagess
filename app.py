import streamlit as st

# Judul aplikasi
st.title("Bahan Kimia Organik")

# Data bahan kimia contoh
bahan_kimia = {
 "Benzena":{
    "Rumus": "C6H6",
    "Bahaya": "Karsinogen, mudah terbakar, iritasi kulit dan saluran pernapasan.",
    "Tindakan Pencegahan": "Gunakan APD, hindari inhalasi dan kontak langsung.",
    "Penyimpanan": "Simpan di tempat sejuk dan jauh dari api."
  },
 "Toluena":{
    "Rumus": "C7H8",
    "Bahaya": "Mudah terbakar, dapat menyebabkan pusing dan iritasi pernapasan.",
    "Tindakan Pencegahan": "Gunakan masker dan ventilasi baik.",
    "Penyimpanan": "Simpan jauh dari sumber api."
  },
   
 "Xilena":{
    "Rumus": "C8H10",
    "Bahaya": "Iritasi kulit, mata, dan saluran pernapasan, beracun jika tertelan.",
    "Tindakan Pencegahan": "Gunakan sarung tangan dan ventilasi baik.",
    "Penyimpanan": "Simpan di tempat sejuk dan tertutup rapat."
  },
  
 "Metanol":{
    "Rumus": "CH3OH",
    "Bahaya": "Beracun jika tertelan, dapat menyebabkan kebutaan dan kematian.",
    "Tindakan Pencegahan": "Hindari konsumsi dan kontak kulit, gunakan ventilasi baik.",
    "Penyimpanan": "Simpan di tempat tertutup dan jauh dari api."
  },
 
 "Etil asetat":{
    "Rumus": "C4H8O2",
    "Bahaya": "Mudah menguap dan mudah terbakar, dapat menyebabkan iritasi mata dan pernapasan.",
    "Tindakan Pencegahan": "Gunakan di area berventilasi, hindari kontak langsung.",
    "Penyimpanan": "Simpan di tempat tertutup dan sejuk."
  },
 "Formaldehida":{
    "Rumus": "CH2O",
    "Bahaya": "Karsinogen, iritasi kulit dan saluran pernapasan.",
    "Tindakan Pencegahan": "Gunakan APD lengkap, hindari inhalasi.",
    "Penyimpanan": "Simpan di tempat gelap dan dingin."
  },
 "Asam_asetat":{
    "Rumus": "CH3COOH",
    "Bahaya": "Iritasi kulit dan mata, korosif pada konsentrasi tinggi.",
    "Tindakan Pencegahan": "Gunakan sarung tangan dan pelindung mata.",
    "Penyimpanan": "Simpan dalam wadah tertutup rapat."
  },
 "Aseton":{
    "Rumus": "C3H6O",
    "Bahaya": "Mudah terbakar, iritasi mata dan pernapasan.",
    "Tindakan Pencegahan": "Gunakan di area berventilasi, hindari kontak langsung.",
    "Penyimpanan": "Simpan jauh dari sumber api."
  },
 "Fenol":{
    "Rumus": "C6H5OH",
    "Bahaya": "Beracun, korosif, dapat menyebabkan luka bakar kulit.",
    "Tindakan Pencegahan": "Gunakan APD lengkap, hindari kontak langsung.",
    "Penyimpanan": "Simpan di tempat sejuk dan tertutup rapat."
  },
 "Kloroform":{
    "Rumus": "CHCl3",
    "Bahaya": "Beracun, karsinogen, dapat menyebabkan kerusakan hati.",
    "Tindakan Pencegahan": "Gunakan APD dan ventilasi baik.",
    "Penyimpanan": "Simpan di tempat gelap dan sejuk."
  },
 "Etilena glikol":{
    "Rumus": "C2H6O2",
    "Bahaya": "Beracun jika tertelan, menyebabkan gagal ginjal.",
    "Tindakan Pencegahan": "Gunakan sarung tangan, hindari konsumsi.",
    "Penyimpanan": "Simpan di tempat sejuk dan berventilasi."
  },
 "Asam format":{
    "Rumus": "HCOOH",
    "Bahaya": "Korosif, dapat menyebabkan iritasi dan luka bakar.",
    "Tindakan Pencegahan": "Gunakan pelindung mata dan sarung tangan.",
    "Penyimpanan": "Simpan dalam wadah tertutup."
  },
 "Stirena":{
    "Rumus": "C8H8",
    "Bahaya": "Mudah terbakar, iritasi kulit dan pernapasan.",
    "Tindakan Pencegahan": "Gunakan ventilasi baik dan hindari kontak kulit.",
    "Penyimpanan": "Simpan jauh dari api dan panas."
  },
 "Keton metil etil":{
    "Rumus": "C4H8O",
    "Bahaya": "Mudah terbakar, mengiritasi mata dan pernapasan.",
    "Tindakan Pencegahan": "Gunakan alat pelindung dan ventilasi baik.",
    "Penyimpanan": "Simpan tertutup dan jauh dari api."
  },
 "Nitrobenzena":{
    "Rumus": "C6H5NO2",
    "Bahaya": "Beracun, dapat menyebabkan keracunan darah.",
    "Tindakan Pencegahan": "Gunakan APD lengkap dan hindari inhalasi.",
    "Penyimpanan": "Simpan di tempat sejuk dan tertutup."
  },
 "Asam benzoat":{
    "Rumus": "C7H6O2",
    "Bahaya": "Dapat menyebabkan iritasi kulit dan mata.",
    "Tindakan Pencegahan": "Gunakan sarung tangan dan kacamata pelindung.",
    "Penyimpanan": "Simpan di tempat kering dan tertutup."
  },
 "Asam salisilat":{
    "Rumus": "C7H6O3",
    "Bahaya": "Dapat menyebabkan iritasi kulit dan reaksi alergi.",
    "Tindakan Pencegahan": "Gunakan sarung tangan, hindari kontak langsung.",
    "Penyimpanan": "Simpan di tempat sejuk dan kering."
  },
 "Etil alkohol (etanol)":{
    "Rumus": "C2H5OH",
    "Bahaya": "Mudah terbakar, mengiritasi mata dan kulit.",
    "Tindakan Pencegahan": "Hindari sumber api, gunakan ventilasi baik.",
    "Penyimpanan": "Simpan di tempat sejuk dan tertutup."
  },
 "Asam propionat":{
    "Rumus": "C3H6O2",
    "Bahaya": "Iritasi kulit dan mata.",
    "Tindakan Pencegahan": "Gunakan pelindung mata dan sarung tangan.",
    "Penyimpanan": "Simpan di tempat sejuk dan tertutup."
  },
 "Asam format metil":{
    "Rumus": "HCOOCH3",
    "Bahaya": "Iritasi pada kulit dan mata, mudah terbakar.",
    "Tindakan Pencegahan": "Gunakan APD dan ventilasi baik.",
    "Penyimpanan": "Simpan jauh dari sumber api."
  },
 "Isopropanol":{
    "Rumus": "C3H8O",
    "Bahaya": "Mudah terbakar, mengiritasi mata dan saluran pernapasan.",
    "Tindakan Pencegahan": "Gunakan di area berventilasi, hindari kontak langsung.",
    "Penyimpanan": "Simpan tertutup dan jauh dari api."
  },
 "Asam klorida asetat":{
    "Rumus": "CH2ClCOOH",
    "Bahaya": "Korosif, menyebabkan iritasi dan luka bakar.",
    "Tindakan Pencegahan": "Gunakan pelindung mata dan sarung tangan.",
    "Penyimpanan": "Simpan di tempat tertutup dan sejuk."
  },
 
  "Akrilonitril":{
    "Rumus": "C3H3N",
    "Bahaya": "Beracun, mudah terbakar, iritasi saluran pernapasan.",
    "Tindakan Pencegahan": "Gunakan APD, hindari inhalasi.",
    "Penyimpanan": "Simpan jauh dari api dan panas."
  },
  
  "Asam kaproat":{
    "Rumus": "C6H12O2",
    "Bahaya": "Iritasi kulit dan mata.",
    "Tindakan Pencegahan": "Gunakan sarung tangan dan pelindung mata.",
    "Penyimpanan": "Simpan di tempat kering dan tertutup."
  },
  
  "Butil alkohol":{
    "Rumus": "C4H10O",
    "Bahaya": "Mudah terbakar, iritasi kulit dan pernapasan.",
    "Tindakan Pencegahan": "Gunakan ventilasi baik dan hindari kontak kulit.",
    "Penyimpanan": "Simpan jauh dari api."
  },
 
  "Asam oksalat":{
    "Rumus": "C2H2O4",
    "Bahaya": "Korosif, dapat menyebabkan iritasi kulit dan saluran pernapasan.",
    "Tindakan Pencegahan": "Gunakan APD lengkap dan hindari inhalasi.",
    "Penyimpanan": "Simpan dalam wadah tertutup."
  },
  
  "Metil metakrilat":{
    "Rumus": "C5H8O2",
    "Bahaya": "Mudah terbakar, iritasi mata dan kulit.",
    "Tindakan Pencegahan": "Gunakan pelindung mata dan sarung tangan.",
    "Penyimpanan": "Simpan di tempat tertutup dan sejuk."
  },
  
  "Asam laktat":{
    "Rumus": "C3H6O3",
    "Bahaya": "Iritasi ringan pada kulit dan mata.",
    "Tindakan Pencegahan": "Gunakan sarung tangan jika kontak langsung.",
    "Penyimpanan": "Simpan di tempat kering."
  },
 
  "Benzaldehida":{
    "Rumus": "C7H6O",
    "Bahaya": "Iritasi kulit dan saluran pernapasan.",
    "Tindakan Pencegahan": "Gunakan masker dan sarung tangan.",
    "Penyimpanan": "Simpan di tempat tertutup dan sejuk."
  },
  
  "Asam maleat":{
    "Rumus": "C4H4O4",
    "Bahaya": "Iritasi kulit, mata, dan saluran pernapasan.",
    "Tindakan Pencegahan": "Gunakan APD lengkap."
  },
 
  "Asam oleat":{
    "Rumus": "C18H34O2",
    "Bahaya": "Iritasi ringan pada kulit dan mata.",
    "Tindakan Pencegahan": "Gunakan sarung tangan.",
    "Penyimpanan": "Simpan di tempat kering."
  },
  
  "Anilin":{
    "Rumus": "C6H5NH2",
    "Bahaya": "Beracun, dapat diserap melalui kulit.",
    "Tindakan Pencegahan": "Gunakan APD lengkap.",
    "Penyimpanan": "Simpan tertutup rapat dan di tempat sejuk."
  },
  
  "Piridina":{
    "Rumus": "C5H5N",
    "Bahaya": "Beracun dan mudah terbakar.",
    "Tindakan Pencegahan": "Gunakan di area berventilasi.",
    "Penyimpanan": "Simpan jauh dari sumber panas."
 },
  
 "Asam sitrat":{
    "Rumus": "C6H8O7",
    "Bahaya": "Iritasi ringan pada kulit dan mata.",
    "Tindakan Pencegahan": "Gunakan sarung tangan dan kacamata pelindung.",
    "Penyimpanan": "Simpan di tempat kering dan tertutup."
  },
  
  "Asam stearat":{
    "Rumus": "C18H36O2",
    "Bahaya": "Iritasi ringan kulit dan mata.",
    "Tindakan Pencegahan": "Gunakan pelindung kulit dan mata.",
    "Penyimpanan": "Simpan di tempat sejuk."
  },
  
  "Asam oleat":{
    "Rumus": "C18H34O2",
    "Bahaya": "Iritasi ringan pada kulit dan mata.",
    "Tindakan Pencegahan": "Gunakan sarung tangan.",
    "Penyimpanan": "Simpan di tempat kering."
  },
  
  "Asam linoleat":{
    "Rumus": "C18H32O2",
    "Bahaya": "Dapat menyebabkan iritasi ringan pada kulit.",
    "Tindakan Pencegahan": "Gunakan sarung tangan pelindung.",
    "Penyimpanan": "Simpan dalam wadah tertutup dan kering."
  },
  
  "Asam arakidonat":{
    "Rumus": "C20H32O2",
    "Bahaya": "Iritasi jika terhirup atau kontak dengan kulit.",
    "Tindakan Pencegahan": "Gunakan masker dan APD.",
    "Penyimpanan": "Simpan dalam suhu rendah dan wadah tertutup."
  },
  
    "Kaprolaktam":{
    "Rumus": "C6H11NO",
    "Bahaya": "Iritasi kulit dan saluran pernapasan.",
    "Tindakan Pencegahan": "Gunakan APD dan ventilasi yang baik.",
    "Penyimpanan": "Simpan di tempat sejuk dan kering."
  },
 
  "Asam glutamat":{
    "Rumus": "C5H9NO4",
    "Bahaya": "Iritasi ringan mata dan kulit.",
    "Tindakan Pencegahan": "Hindari kontak langsung.",
    "Penyimpanan": "Simpan dalam wadah tertutup."
  },
  
  "Asam linolenat":{
    "Rumus": "C18H30O2",
    "Bahaya": "Dapat menyebabkan iritasi pada kulit sensitif.",
    "Tindakan Pencegahan": "Gunakan pelindung tangan.",
    "Penyimpanan": "Simpan di tempat gelap dan sejuk."
  },
  
  "Asam fumarat":{
    "Rumus": "C4H4O4",
    "Bahaya": "Dapat menyebabkan iritasi saluran pernapasan.",
    "Tindakan Pencegahan": "Gunakan masker dan sarung tangan.",
    "Penyimpanan": "Simpan dalam wadah tertutup dan kering."
  },
  
  "Gliserol":{
    "Rumus": "C3H8O3",
    "Bahaya": "Iritasi ringan jika tertelan dalam jumlah besar.",
    "Tindakan Pencegahan": "Hindari konsumsi berlebihan.",
    "Penyimpanan": "Simpan di tempat sejuk dan kering."
  },
  
  "Trigliserida":{
    "Rumus": "C55H98O6",
    "Bahaya": "Non-toksik namun mudah terdegradasi secara oksidatif.",
    "Tindakan Pencegahan": "Hindari pemanasan berlebih.",
    "Penyimpanan": "Simpan di tempat gelap dan tertutup."
  },

  "Alanin":{
    "Rumus": "C3H7NO2",
    "Bahaya": "Risiko rendah, tetapi tetap gunakan APD.",
    "Tindakan Pencegahan": "Gunakan sarung tangan saat kontak langsung.",
    "Penyimpanan": "Simpan dalam wadah kering dan bersih."
  },
  
  "Lisin":{
    "Rumus": "C6H14N2O2",
    "Bahaya": "Iritasi ringan pada kontak langsung.",
    "Tindakan Pencegahan": "Gunakan pelindung kulit.",
    "Penyimpanan": "Simpan di tempat kering dan sejuk."
  },

  "Alanin":{
    "Rumus": "C3H7NO2",
    "Bahaya": "Risiko rendah, tetapi tetap gunakan APD.",
    "Tindakan Pencegahan": "Gunakan sarung tangan saat kontak langsung.",
    "Penyimpanan": "Simpan dalam wadah kering dan bersih."
  },
  
  "Lisin":{
    "Rumus": "C6H14N2O2",
    "Bahaya": "Iritasi ringan pada kontak langsung.",
    "Tindakan Pencegahan": "Gunakan pelindung kulit.",
    "Penyimpanan": "Simpan di tempat kering dan sejuk."
  },
 
  "Asam askorbat":{
    "Rumus": "C6H8O6",
    "Bahaya": "Dapat mengiritasi jika terhirup dalam bentuk serbuk.",
    "Tindakan Pencegahan": "Gunakan masker dan sarung tangan.",
    "Penyimpanan": "Simpan dalam wadah gelap dan kedap udara."
  },
  
  "Tiamin (Vitamin B1)":{
    "Rumus": "C12H17N4OS",
    "Bahaya": "Dosis tinggi dapat menyebabkan iritasi.",
    "Tindakan Pencegahan": "Gunakan sesuai dosis.",
    "Penyimpanan": "Simpan dalam tempat gelap dan tertutup."
  },
  
  "Urea":{
    "Rumus": "CH4N2O",
    "Bahaya": "Iritasi mata dan kulit.",
    "Tindakan Pencegahan": "Gunakan sarung tangan dan hindari kontak langsung.",
    "Penyimpanan": "Simpan di tempat kering dan tertutup."
  },
 
  "Kreatin":{
    "Rumus": "C4H9N3O2",
    "Bahaya": "Aman dalam jumlah kecil, iritasi jika terhirup serbuk.",
    "Tindakan Pencegahan": "Gunakan masker jika berbentuk bubuk.",
    "Penyimpanan": "Simpan di tempat kering."
  },
  
  "Kolesterol":{
    "Rumus": "C27H46O",
    "Bahaya": "Tidak berbahaya secara langsung, namun mudah teroksidasi.",
    "Tindakan Pencegahan": "Hindari paparan cahaya.",
    "Penyimpanan": "Simpan dalam wadah gelap dan tertutup."
  },
  "Asam piruvat":{
    "Rumus": "C3H4O3",
    "Bahaya": "Iritasi kulit dan mata.",
    "Tindakan Pencegahan": "Gunakan sarung tangan dan pelindung mata.",
    "Penyimpanan": "Simpan di tempat kering dan tertutup."
  },
  
  "Asam malat":{
    "Rumus": "C4H6O5",
    "Bahaya": "Iritasi ringan bila terhirup atau kontak dengan kulit.",
    "Tindakan Pencegahan": "Gunakan APD.",
    "Penyimpanan": "Simpan dalam wadah tertutup rapat."
  },
  
  "Asam tartarat":{
    "Rumus": "C4H6O6",
    "Bahaya": "Iritasi ringan pada kulit dan mata.",
    "Tindakan Pencegahan": "Gunakan sarung tangan.",
    "Penyimpanan": "Simpan di tempat sejuk dan kering."
  },
  
  "Asam mandelat":{
    "Rumus": "C8H8O3",
    "Bahaya": "Dapat menyebabkan iritasi kulit.",
    "Tindakan Pencegahan": "Gunakan APD saat penanganan.",
    "Penyimpanan": "Simpan di tempat kering dan tertutup."
  },
  
  "Beta-karoten":{
    "Rumus": "C40H56",
    "Bahaya": "Tidak beracun, namun sensitif terhadap cahaya.",
    "Tindakan Pencegahan": "Hindari cahaya langsung.",
    "Penyimpanan": "Simpan dalam wadah gelap."
  },
  
  "Retinol":{
    "Rumus": "C20H30O",
    "Bahaya": "Sensitif terhadap cahaya dan oksigen.",
    "Tindakan Pencegahan": "Gunakan pelindung cahaya.",
    "Penyimpanan": "Simpan dalam wadah tertutup rapat dan gelap."
  },
  
  "Asam butenat":{
    "Rumus": "C4H6O2",
    "Bahaya": "Mudah terbakar dan iritasi kulit.",
    "Tindakan Pencegahan": "Gunakan sarung tangan dan hindari api.",
    "Penyimpanan": "Simpan di tempat sejuk dan jauh dari sumber api."
  },
 
  "Asam kaproat etil":{
    "Rumus": "C8H16O2",
    "Bahaya": "Mengiritasi kulit dan mata.",
    "Tindakan Pencegahan": "Gunakan pelindung kulit dan mata.",
    "Penyimpanan": "Simpan di tempat sejuk dan kering."
  },
 
  "Asam benzensulfonat":{
    "Rumus": "C6H6O3S",
    "Bahaya": "Korosif dan iritasi saluran pernapasan.",
    "Tindakan Pencegahan": "Gunakan masker dan pelindung kulit.",
    "Penyimpanan": "Simpan dalam wadah tahan korosi."
  },
  
  "Vanilin":{
    "Rumus": "C8H8O3",
    "Bahaya": "Iritasi ringan pada kulit dan mata.",
    "Tindakan Pencegahan": "Gunakan sarung tangan saat kontak langsung.",
    "Penyimpanan": "Simpan di tempat kering dan gelap."
  },
  
  "Asam asetosalisilat (Aspirin)":{
    "Rumus": "C9H8O4",
    "Bahaya": "Dapat menyebabkan iritasi saluran cerna jika tertelan berlebihan.",
    "Tindakan Pencegahan": "Gunakan sesuai dosis.",
    "Penyimpanan": "Simpan di tempat kering dan sejuk."
  },
  
  "Asam glutarat":{
    "Rumus": "C5H8O4",
    "Bahaya": "Iritasi kulit dan saluran pernapasan.",
    "Tindakan Pencegahan": "Gunakan pelindung pernapasan.",
    "Penyimpanan": "Simpan dalam wadah tertutup dan berventilasi baik."
  },
  
  "Asam adipat":{
    "Rumus": "C6H10O4",
    "Bahaya": "Dapat mengiritasi kulit dan mata.",
    "Tindakan Pencegahan": "Gunakan APD lengkap.",
    "Penyimpanan": "Simpan di tempat kering dan tertutup."
  },
  
  "Asam itakonat":{
    "Rumus": "C5H6O4",
    "Bahaya": "Iritasi ringan kulit dan pernapasan.",
    "Tindakan Pencegahan": "Gunakan sarung tangan dan ventilasi baik.",
    "Penyimpanan": "Simpan dalam wadah kedap udara."
  },
  
  "Betaine":{
    "Rumus": "C5H11NO2",
    "Bahaya": "Relatif aman, iritasi ringan bila terhirup.",
    "Tindakan Pencegahan": "Gunakan masker jika dalam bentuk bubuk.",
    "Penyimpanan": "Simpan dalam wadah kering."
  },
  
  "Asam deoksiribonukleat (DNA)":{
    "Rumus": "C15H31N3O13P2 (unit)",
    "Bahaya": "Tidak berbahaya, bahan biologis.",
    "Tindakan Pencegahan": "Gunakan sesuai protokol laboratorium biologi.",
    "Penyimpanan": "Simpan di suhu -20°C atau sesuai instruksi."
  },
  
  "Asam ribonukleat (RNA)":{
    "Rumus": "C10H13N5O8P (unit)",
    "Bahaya": "Tidak berbahaya, bahan biologis.",
    "Tindakan Pencegahan": "Gunakan sarung tangan dan teknik aseptik.",
    "Penyimpanan": "Simpan beku dalam kondisi RNase-free."
  },
  
  "Asam fitat":{
    "Rumus": "C6H18O24P6",
    "Bahaya": "Dapat mengganggu penyerapan mineral jika tertelan berlebih.",
    "Tindakan Pencegahan": "Gunakan dosis sesuai instruksi.",
    "Penyimpanan": "Simpan dalam wadah gelap dan tertutup."
  },
  
  "Asam urat":{
    "Rumus": "C5H4N4O3",
    "Bahaya": "Dapat membentuk kristal dalam tubuh (gout).",
    "Tindakan Pencegahan": "Gunakan sesuai prosedur medis.",
    "Penyimpanan": "Simpan di tempat kering dan aman."
  },
  
  "Melatonin":{
    "Rumus": "C13H16N2O2",
    "Bahaya": "Dosis tinggi dapat menyebabkan kantuk berlebihan.",
    "Tindakan Pencegahan": "Gunakan sesuai petunjuk.",
    "Penyimpanan": "Simpan di tempat gelap dan dingin."
  },
  
  "Asam galat":{
    "Rumus": "C7H6O5",
    "Bahaya": "Iritasi pada kulit dan mata.",
    "Tindakan Pencegahan": "Gunakan pelindung mata dan sarung tangan.",
    "Penyimpanan": "Simpan di tempat kering dan terlindung dari cahaya."
  },
  
  "Asam kafeat":{
    "Rumus": "C9H8O4",
    "Bahaya": "Iritasi ringan pada kulit.",
    "Tindakan Pencegahan": "Gunakan sarung tangan saat penanganan.",
    "Penyimpanan": "Simpan di tempat sejuk dan gelap."
  },
  
  "Asam sinamat":{
    "Rumus": "C9H8O2",
    "Bahaya": "Dapat menyebabkan iritasi kulit dan saluran pernapasan.",
    "Tindakan Pencegahan": "Gunakan APD dan ventilasi baik.",
    "Penyimpanan": "Simpan dalam wadah tertutup dan kering."
  },
  
  "Genistein":{
    "Rumus": "C15H10O5",
    "Bahaya": "Kemungkinan mengganggu hormon bila digunakan berlebihan.",
    "Tindakan Pencegahan": "Gunakan sesuai petunjuk ilmiah.",
    "Penyimpanan": "Simpan di tempat gelap dan kering."
  },
  
  "Kuarsetin":{
    "Rumus": "C15H10O7",
    "Bahaya": "Iritasi ringan jika terhirup dalam bentuk serbuk.",
    "Tindakan Pencegahan": "Gunakan masker dan sarung tangan.",
    "Penyimpanan": "Simpan dalam wadah kedap udara."
  },
  
  "Limonen":{
    "Rumus": "C10H16",
    "Bahaya": "Iritasi kulit dan mata, mudah terbakar.",
    "Tindakan Pencegahan": "Gunakan APD, jauhkan dari sumber api.",
    "Penyimpanan": "Simpan di tempat sejuk dan berventilasi baik."
  },
  
  "Mentol":{
    "Rumus": "C10H20O",
    "Bahaya": "Dapat menyebabkan iritasi kulit atau reaksi alergi.",
    "Tindakan Pencegahan": "Gunakan sarung tangan.",
    "Penyimpanan": "Simpan di tempat tertutup dan sejuk."
  },
  
  "Eugenol":{
    "Rumus": "C10H12O2",
    "Bahaya": "Iritasi kulit dan saluran pernapasan.",
    "Tindakan Pencegahan": "Gunakan pelindung kulit dan ventilasi baik.",
    "Penyimpanan": "Simpan dalam wadah tertutup rapat."
  },
  
  "Tiamin pirofosfat":{
    "Rumus": "C12H19ClN4O7PS",
    "Bahaya": "Iritasi jika terhirup atau kontak dengan kulit.",
    "Tindakan Pencegahan": "Gunakan masker dan APD.",
    "Penyimpanan": "Simpan di suhu rendah dan terlindung cahaya."
  },
  
  "Asam nikotinat (Niacin)":{
    "Rumus": "C6H5NO2",
    "Bahaya": "Iritasi kulit ringan dan reaksi 'flushing'.",
    "Tindakan Pencegahan": "Gunakan sesuai dosis.",
    "Penyimpanan": "Simpan di tempat sejuk dan kering."
  },
  
  "Asam pantotenat":{
    "Rumus": "C9H17NO5",
    "Bahaya": "Dosis tinggi dapat menyebabkan diare.",
    "Tindakan Pencegahan": "Ikuti panduan penggunaan.",
    "Penyimpanan": "Simpan dalam wadah tertutup dan kering."
  },
  
  "Asam folat":{
    "Rumus": "C19H19N7O6",
    "Bahaya": "Relatif aman, overdosis dapat menyebabkan gangguan pencernaan.",
    "Tindakan Pencegahan": "Gunakan sesuai anjuran medis.",
    "Penyimpanan": "Simpan di tempat gelap dan sejuk."
  },
  
  "Riboflavin":{
    "Rumus": "C17H20N4O6",
    "Bahaya": "Tidak berbahaya, namun sensitif terhadap cahaya.",
    "Tindakan Pencegahan": "Hindari paparan sinar langsung.",
    "Penyimpanan": "Simpan dalam wadah gelap dan kering."
  },
  
  "Flavon":{
    "Rumus": "C15H10O2",
    "Bahaya": "Iritasi ringan bila terhirup dalam bentuk serbuk.",
    "Tindakan Pencegahan": "Gunakan masker.",
    "Penyimpanan": "Simpan dalam wadah tertutup."
  },
  
  "Catechin":{
    "Rumus": "C15H14O6",
    "Bahaya": "Iritasi ringan pada kulit dan mata.",
    "Tindakan Pencegahan": "Gunakan sarung tangan saat penanganan.",
    "Penyimpanan": "Simpan di tempat sejuk dan kering."
  },
  
  "Kurkumin":{
    "Rumus": "C21H20O6",
    "Bahaya": "Iritasi ringan pada saluran cerna jika tertelan dalam jumlah besar.",
    "Tindakan Pencegahan": "Gunakan sesuai takaran.",
    "Penyimpanan": "Simpan di tempat gelap dan tertutup."
  },
  
  "Apigenin":{
    "Rumus": "C15H10O5",
    "Bahaya": "Iritasi ringan jika terhirup.",
    "Tindakan Pencegahan": "Gunakan masker.",
    "Penyimpanan": "Simpan di tempat kering dan tertutup."
  },
  
  "Galangin":{
    "Rumus": "C15H10O5",
    "Bahaya": "Iritasi ringan pada kulit.",
    "Tindakan Pencegahan": "Gunakan pelindung kulit.",
    "Penyimpanan": "Simpan dalam wadah kedap udara."
  },
  
  "Kavain":{
    "Rumus": "C14H14O3",
    "Bahaya": "Sedatif, bisa memengaruhi sistem saraf.",
    "Tindakan Pencegahan": "Gunakan sesuai petunjuk medis.",
    "Penyimpanan": "Simpan di tempat sejuk dan kering."
  },
  
  "Serotonin":{
    "Rumus": "C10H12N2O",
    "Bahaya": "Dapat memengaruhi sistem saraf pusat.",
    "Tindakan Pencegahan": "Gunakan dalam konteks medis/laboratorium.",
    "Penyimpanan": "Simpan dalam kondisi dingin dan stabil."
  }
  
  "Histamin":{
    "Rumus": "C5H9N3",
    "Bahaya": "Dapat menyebabkan reaksi alergi dan inflamasi.",
    "Tindakan Pencegahan": "Gunakan sarung tangan dan hindari inhalasi.",
    "Penyimpanan": "Simpan dalam suhu dingin dan terlindung cahaya."
  },
  
  "Adrenalin":{
    "Rumus": "C9H13NO3",
    "Bahaya": "Dapat memengaruhi tekanan darah dan jantung.",
    "Tindakan Pencegahan": "Tangani dengan hati-hati sesuai protokol medis.",
    "Penyimpanan": "Simpan di tempat sejuk dan gelap."
  },
  
  "Dopamin":{
    "Rumus": "C8H11NO2",
    "Bahaya": "Dapat memengaruhi sistem saraf.",
    "Tindakan Pencegahan": "Gunakan APD saat penanganan.",
    "Penyimpanan": "Simpan dalam kondisi stabil dan tertutup."
  },
  
  "Asam hialuronat":{
    "Rumus": "(C14H21NO11)n",
    "Bahaya": "Tidak berbahaya secara umum.",
    "Tindakan Pencegahan": "Gunakan sarung tangan untuk penanganan steril.",
    "Penyimpanan": "Simpan pada suhu rendah dan bebas kontaminasi."
  },
  
  "Prostaglandin E2":{
    "Rumus": "C20H32O5",
    "Bahaya": "Berpotensi memengaruhi sistem reproduksi.",
    "Tindakan Pencegahan": "Tangani di bawah lemari asam dengan APD lengkap.",
    "Penyimpanan": "Simpan pada suhu rendah."
  },
  
  "Leukotrien B4":{
    "Rumus": "C20H32O4",
    "Bahaya": "Memicu peradangan dan reaksi imun.",
    "Tindakan Pencegahan": "Gunakan sarung tangan dan pelindung wajah.",
    "Penyimpanan": "Simpan dalam kondisi beku."
  },
  
  "Triptofan":{
    "Rumus": "C11H12N2O2",
    "Bahaya": "Aman dalam dosis normal, dapat menyebabkan kantuk.",
    "Tindakan Pencegahan": "Hindari konsumsi berlebih.",
    "Penyimpanan": "Simpan di tempat sejuk dan kering."
  },
  
  "Fenilalanin":{
    "Rumus": "C9H11NO2",
    "Bahaya": "Berbahaya bagi penderita fenilketonuria (PKU).",
    "Tindakan Pencegahan": "Gunakan label peringatan bila dijual.",
    "Penyimpanan": "Simpan dalam wadah tertutup."
  },
  
  "Tirosin":{
    "Rumus": "C9H11NO3",
    "Bahaya": "Risiko rendah, gunakan sesuai kebutuhan.",
    "Tindakan Pencegahan": "Gunakan APD bila dalam bentuk serbuk.",
    "Penyimpanan": "Simpan di tempat kering."
  },
  
  "Asam uridilat (UMP)":{
    "Rumus": "C9H13N2O9P",
    "Bahaya": "Tidak toksik, digunakan dalam biokimia.",
    "Tindakan Pencegahan": "Tangani sesuai prosedur lab molekuler.",
    "Penyimpanan": "Simpan dalam freezer -20°C."
  },
  
  "Karnosin":{
    "Rumus": "C9H14N4O3",
    "Bahaya": "Aman, tetapi hindari konsumsi berlebihan.",
    "Tindakan Pencegahan": "Gunakan sesuai pedoman laboratorium.",
    "Penyimpanan": "Simpan dalam wadah tertutup dan kering."
  },
  
  "Glutathion":{
    "Rumus": "C10H17N3O6S",
    "Bahaya": "Aman secara umum, oksidatif bila terekspos udara.",
    "Tindakan Pencegahan": "Gunakan segera setelah dibuka.",
    "Penyimpanan": "Simpan di suhu rendah dan bebas cahaya."
  },
  
  "Koenzim Q10":{
    "Rumus": "C59H90O4",
    "Bahaya": "Iritasi ringan bila kontak langsung.",
    "Tindakan Pencegahan": "Gunakan sarung tangan.",
    "Penyimpanan": "Simpan dalam wadah gelap dan sejuk."
  },
  
  "Squalene":{
    "Rumus": "C30H50",
    "Bahaya": "Mudah teroksidasi, iritasi ringan.",
    "Tindakan Pencegahan": "Hindari panas dan udara terbuka.",
    "Penyimpanan": "Simpan dalam wadah kedap udara."
  },
  
  "Retinal":{
    "Rumus": "C20H28O",
    "Bahaya": "Sensitif terhadap cahaya dan udara.",
    "Tindakan Pencegahan": "Tangani di bawah cahaya redup.",
    "Penyimpanan": "Simpan di tempat gelap dan dingin."
  },
  
  "Palmitat etil":{
    "Rumus": "C18H36O2",
    "Bahaya": "Iritasi ringan pada kulit.",
    "Tindakan Pencegahan": "Gunakan pelindung kulit.",
    "Penyimpanan": "Simpan di tempat kering dan sejuk."
  },
  
  "Stearat gliseril":{
    "Rumus": "C21H42O4",
    "Bahaya": "Umumnya tidak beracun.",
    "Tindakan Pencegahan": "Tangani di lingkungan bersih.",
    "Penyimpanan": "Simpan di wadah tertutup."
  },
  
  "Laurat natrium":{
    "Rumus": "C12H23NaO2",
    "Bahaya": "Iritasi kulit dan mata.",
    "Tindakan Pencegahan": "Gunakan sarung tangan dan pelindung mata.",
    "Penyimpanan": "Simpan dalam tempat kering."
  },
  
  "Oleil alkohol":{
    "Rumus": "C18H36O",
    "Bahaya": "Iritasi ringan pada kulit.",
    "Tindakan Pencegahan": "Gunakan APD saat penanganan.",
    "Penyimpanan": "Simpan dalam wadah tertutup dan gelap."
  },
  
  "Miranol":{
    "Rumus": "C18H38N2O3S",
    "Bahaya": "Iritasi kulit dan mata.",
    "Tindakan Pencegahan": "Gunakan APD dan hindari kontak langsung.",
    "Penyimpanan": "Simpan di tempat kering dan berventilasi."
  }


# Input pencarian bahan kimia
nama_bahan = st.text_input("Masukkan nama bahan kimia:")

if nama_bahan:
    found = False
    for key, data in bahan_kimia.items():
        # Normalisasi: ganti underscore jadi spasi, lowercase semua
        key_normalized = key.replace('_', ' ').lower()
        input_normalized = nama_bahan.lower()

        # Cek apakah input ada di nama bahan
        if input_normalized in key_normalized:
            st.subheader(f"Informasi tentang {key.replace('_', ' ').title()}:")
            st.write(f"*Rumus Kimia:* {data['Rumus']}")
            st.write(f"*Bahaya:* {data['Bahaya']}")
            st.write(f"*Tindakan Pencegahan:* {data['Tindakan Pencegahan']}")
            st.write(f"*Penyimpanan:* {data['Penyimpanan']}")
            found = True

    if not found:
        st.error("Data bahan kimia tidak ditemukan. Silakan coba nama lain.")
else:
    st.info("Masukkan nama bahan kimia untuk melihat informasinya.")
