# --- Proiect: Calculator Simplu de Profit per Utilizator ---

print("=== GESTIUNE UTILIZATOR ===")

# Setăm comisionul platformei direct în cod (valoare fixă)
COMISION_FIX = 5.0  # de exemplu, 5 RON comision per tranzacție

# Preluăm doar datele esențiale de la cel care testează
nume_utilizator = input("Introdu numele utilizatorului: ")
bani_depusi = float(input("Introdu suma depusă de utilizator (RON): "))

# Calculăm automat profitul net
profit_net = bani_depusi - COMISION_FIX

# Afișăm raportul final clar și ordonat
print("\n--- RAPORT FINAL ---")
print(f"Utilizator: {nume_utilizator}")
print(f"Sumă depusă: {bani_depusi} RON")
print(f"Comision platformă (predefinit): {COMISION_FIX} RON")
print(f"Profit net rămas: {profit_net} RON")
