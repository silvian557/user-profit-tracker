print("=== GESTIUNE UTILIZATOR ===")

COMISION_FIX = 5.0

nume_utilizator = input("Introdu numele utilizatorului: ")
bani_depusi = float(input("Introdu suma depusă de utilizator (RON): "))

profit_net = bani_depusi - COMISION_FIX

print("\n--- RAPORT FINAL ---")
print(f"Utilizator: {nume_utilizator}")
print(f"Sumă depusă: {bani_depusi} RON")
print(f"Comision platformă (predefinit): {COMISION_FIX} RON")
print(f"Profit net rămas: {profit_net} RON")
