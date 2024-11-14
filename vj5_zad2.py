def provjera_broja (broj): 
    if 10 <= broj <= 100:
        return f"Broj {broj} je unutar raspona."
    else:
    
        return f"Broj {broj} je izvan raspona."
if __name__ == "__main__":
    try:
    print (provjera broja (prvi broj))
    drugi_broj = int(input("Unesite drugi broj: "))
    print (provjera_broja (drugi_broj))
    except ValueError:
    print("Unesena vrijednost nije broj.")