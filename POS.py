# POS funksie om produkte en pryse te stoor
def store_products():
    products = []
    while True:
        print("\nKies 'n produk om by te voeg:")
        print("1. Kaas")
        print("2. Melk")
        print("3. Brood")
        print("4. Klaar met inkopies")

        choice = input("Gee jou keuse (1/2/3/4): ")

        if choice == '4':
            break  # Verlaat die lus as die gebruiker klaar is met inkopies

        if choice == '1':
            product_name = "Kaas"
        elif choice == '2':
            product_name = "Melk"
        elif choice == '3':
            product_name = "Brood"
        else:
            print("Ongeldige keuse. Probeer weer.")
            continue

        while True:
            try:
                product_price = float(input(f"Gee die prys vir {product_name}: R"))
                break  # Verlaat die lus as die konversie suksesvol is
            except ValueError:
                print("Ongeldige prys. Voer 'n geldige prys in.")

        products.append((product_name, product_price))

    return products

# POS funksie om die totale koste te bereken en te druk
def calculate_and_print_total(products):
    total = 0.0
    print("\nProdukte gekoop:")
    print("----------------")
    for product, price in products:
        print(f"{product.ljust(10)} R{price:.2f}")
        total += price
    print("----------------")
    print(f"Totaal      R{total:.2f}")

# Funksie om die hoofmenu te druk en 'n keuse van die gebruiker te kry
def print_menu():
    print("\nKies 'n opsie:")
    print("1. Voer produkte in")
    print("2. Wys produkte en totaal")
    print("3. Verlaat")

# Hoofprogram van die POS
def main():
    print("Welkom by die POS stelsel.")
    products = []

    while True:
        print_menu()
        choice = input("Gee jou keuse (1/2/3): ")

        if choice == '1':
            print("\nVoer produkte in:")
            products += store_products()
        elif choice == '2':
            if products:
                calculate_and_print_total(products)
            else:
                print("Geen produkte ingevoer nie.")
        elif choice == '3':
            print("Uitvoer die POS stelsel.")
            break
        else:
            print("Ongeldige keuse. Probeer weer.")

if __name__ == "__main__":
    main()
