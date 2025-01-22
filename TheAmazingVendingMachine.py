class AmazingVendingMachine:
    def __init__(self): # Snack and Drink categories
        self.snacks = {
            'Chips': { # Subcategories for organized user experience
                '#A11': {"name": "Cheetos", "price": 2.50},
                '#A12': {"name": "Doritos", "price": 2.50},
                '#A13': {"name": "Lays", "price": 2.50},
                '#A14': {"name": "Takis", "price": 4.00}
            },
            'Chocolate': {
                '#B21': {"name": "Mars", "price": 3.45},
                '#B22': {"name": "Snickers", "price": 3.45},
                '#B23': {"name": "Twix", "price": 3.50},
                '#B24': {"name": "Toblerone", "price": 4.45}
            },
            'Cookies': {
                '#L41': {"name": "Oreo", "price": 4.20},
                '#L42': {"name": "Lotus Biscoff", "price": 6.80},
                '#L43': {"name": "Fita", "price": 2.50},
                '#L44': {"name": "Chips Ahoy", "price": 7.90}
            }
        }

        self.drinks = {
            'Cold Drinks': {
                '#S11': {"name": "Coke", "price": 2.50},
                '#S12': {"name": "Pepsi", "price": 2.50},
                '#S13': {"name": "Mountain Dew", "price": 2.50},
                '#S14': {"name": "Sprite", "price": 2.50},
                '#S15': {"name": "Lipton Iced Tea", "price": 3.10},
                '#S16': {"name": "Capri-Sun Apple", "price": 2.15}
            },
            'Hot Drinks': {
                '#F11': {"name": "Americano", "price": 2.95},
                '#F12': {"name": "Caramel Macchiato", "price": 4.50},
                '#F13': {"name": "Spanish Latte", "price": 5.00},
                '#F14': {"name": "Chamomile", "price": 3.50},
                '#F15': {"name": "Green Tea", "price": 2.50},
                '#F16': {"name": "Lemon Tea", "price": 2.00}
            }
        }

        self.cart = [] # Tracks item chosen
        self.total_amount = 0 # To get the total at the end of purchase

    # Class groups are used to make the code more readable and less redundant.
    def display_items(self, category):
        # Displays items in the selected category
        for code, info in category.items():
            print(f"{info['name']} (Code: {code}) - ${info['price']:.2f}")

    def add_to_cart(self, item):
        # Updates cart and total cost whenever an item is chosen by user
        self.cart.append(item['name'])
        self.total_amount += item['price']
        print(f"{item['name']} has been added to your cart.")

    def handle_payment(self):
        # Purchase payment for the total amount
        print("\nHow amazing! Thank you for your purchase!")
        print("[SS] -> Cash")
        print("[CC] -> Card")
        purchase = self.get_valid_selection(['SS', 'CC'], "Choose a payment method: ")
        
        if purchase == 'SS': 
            # This handles cash payment 
            # Also allows user to insert cash multiple times if needed
            total_remaining = self.total_amount
            while total_remaining > 0:
                try:
                    cash = float(input(f"Your total amount is ${total_remaining:.2f}. Please insert cash: "))
                    
                    if cash < total_remaining:
                        total_remaining -= cash
                        total_remaining = round(total_remaining, 2)
                        print(f"Oh no! Your cash is insufficient to complete your order. ${total_remaining:.2f} is still needed.")
                        
                        additional_cash = input("Would it be cool if you add more? (yes/no): ").strip().lower()
                        if additional_cash != 'yes':
                            print("Sorry. Since you didn't insert additional cash, your transaction will be cancelled :(")
                            return 
                    else:
                        change = round(cash - total_remaining, 2)
                        print(f"AMAZING! Your payment is successful. Your change is ${change:.2f}. Thank you for choosing The Amazing Vending Machine. Have an Amazing day! :)")
                        break
                    
                except ValueError:
                    print("Oh no! Your input is invalid. Please enter a valid amount.")

        elif purchase == 'CC':
            # Deals with card payment if chosen. Less complicated transaction
            print("AMAZING! Your payment is successful! Payment successful. Thank you for using your card.")
            return
        else:
            print("Invalid payment method. Transaction cancelled.")

    def get_valid_selection(self, valid_choices, prompt):
        # Validating whether the user was able to select the correct choice shown in the given
        while True:
            choice = input(prompt).strip().upper()
            if choice in valid_choices:
                return choice
            print(f"Oh no! Your input is invalid. Please choose from {', '.join(valid_choices)}.")

    def run(self):
        # The main function of how the vending machine program will progress
        while True:
            print("\n--- Welcome to the Amazing Vending Machine! ---") # User will first choose between food or drink purchase. Otheriwse, transaction will be finished as it is
            print("[F] -> Food")
            print("[D] -> Drinks")
            print("[X] -> Exit")

            choice = self.get_valid_selection(['F', 'D', 'X'], "What would you like to purchase today?: ")

            if choice == 'X':
                # Will end the program right away if chosen
                print("\nThank you for using the Amazing Vending Machine!")
                if self.cart:
                    print("\n--- Proof of Purchase ---")
                    for item in self.cart:
                        print(item)
                    print(f"Total: ${self.total_amount:.2f}")
                    self.handle_payment()
                break

            elif choice == 'F':
                # Will display the available food subcategories to the user
                # Opted to do this for smoother and organized order flow
                print("\nAmazing choice! Below are some of our Snack options:")
                print("[A] -> Chips")
                print("[B] -> Chocolate")
                print("[L] -> Cookies")
                snack_choice = self.get_valid_selection(['A', 'B', 'L'], "Select a category (A/B/L): ")

                if snack_choice == 'A':
                    # Displays full menu for the chosen food subcategory including item's code and price 
                    # Same goes with the rest of the following
                    self.display_items(self.snacks['Chips'])
                    code = self.get_valid_selection(self.snacks['Chips'].keys(), "Please enter the code of your chosen chips: ")
                    self.add_to_cart(self.snacks['Chips'][code])

                elif snack_choice == 'B':
                    self.display_items(self.snacks['Chocolate'])
                    code = self.get_valid_selection(self.snacks['Chocolate'].keys(), "Please enter the code of your chosen chocolate: ")
                    self.add_to_cart(self.snacks['Chocolate'][code])

                elif snack_choice == 'L':
                    self.display_items(self.snacks['Cookies'])
                    code = self.get_valid_selection(self.snacks['Cookies'].keys(), "Please enter the code of your chosen cookie: ")
                    self.add_to_cart(self.snacks['Cookies'][code])

            elif choice == 'D':
                # Will display the available drink subcategories to the user
                print("\nDrink Categories:")
                print("[C] -> Cold Drinks")
                print("[H] -> Hot Drinks")
                drink_choice = self.get_valid_selection(['C', 'H'], "Do you want to purchase cold drinks or hot drinks? (C/H): ")

                if drink_choice == 'C':
                    self.display_items(self.drinks['Cold Drinks'])
                    code = self.get_valid_selection(self.drinks['Cold Drinks'].keys(), "Please enter the code of your chosen cold drink: ")
                    self.add_to_cart(self.drinks['Cold Drinks'][code])

                elif drink_choice == 'H':
                    self.display_items(self.drinks['Hot Drinks'])
                    code = self.get_valid_selection(self.drinks['Hot Drinks'].keys(), "Please enter the code of your chosen hot drink: ")
                    self.add_to_cart(self.drinks['Hot Drinks'][code])

            # Option is given to the user if interested in purchasing another item
            # If yes, the program will start over
            repeat_choice = input("UH-Mazing! Choose another item? (yes/no): ").strip().lower()
            if repeat_choice != 'yes':
                print("\nThank you for using the Amazing Vending Machine!")
                if self.cart:
                    print("\n--- Proof of Purchase ---")
                    for item in self.cart:
                        print(item)
                    print(f"Total: ${self.total_amount:.2f}")
                    self.handle_payment()
                break

# To run the vending machine program
machine = AmazingVendingMachine()
machine.run()