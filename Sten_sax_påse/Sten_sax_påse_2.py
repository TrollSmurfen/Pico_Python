import random

def get_dator_val():# Funktion för att få datorns val 
    val = ["sten", "sax", "påse"]
    return random.choice(val)

def get_spelare_val():# Funktion för att få spelarens val 
    spelare_val = input("Välj sten, sax eller påse: ").lower()
    while spelare_val not in ["sten", "sax", "påse"]: # Kontrollera att spelarens val är giltigt
        spelare_val = input("Ogiltigt val. Välj sten, sax eller påse: ").lower()
    return spelare_val

def avgör_vinnare(spelare_val, dator_val): #Funktion för att avgöra vinnaren
    if spelare_val == dator_val:
        return "Oavgjort!"
    elif (spelare_val == "sten" and dator_val == "sax") or \
         (spelare_val == "sax" and dator_val == "påse") or \
         (spelare_val == "påse" and dator_val == "sten"):
        return "Du vinner!"
    else:
        return "Datorn vinner!"

def spela(): # Huvudfuntion för att spela spelet
    while True:
        # Få spelarens och datorns val
        spelare_val = get_spelare_val()
        dator_val = get_dator_val()
        # Visa resultet
        print(f"Du valde: {spelare_val}")
        print(f"Datorn valde: {dator_val}")
        print(avgör_vinnare(spelare_val, dator_val))
        #Fråga om spelaren vill spela igen
        spela_igen = input("Vill du spela igen? (ja/nej): ").lower()
        if spela_igen != "ja":
            print("Spelet är över!")
            break # Exit the loop after one game

if __name__ == "__main__": #Starta spelet
    spela()