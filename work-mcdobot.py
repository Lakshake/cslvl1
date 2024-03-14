print("Good morrow th're! what can i receiveth f'r thee?")

burger = input("What burger would you like?")

if burger.lowercase() in ['Burger King', 'Humans', 'A&W']:
    print("no what's wrong with you. please leave the store.")

else:
    fries = input(f"Okay, {burger}, and fries? (YES/NO)")

if fries.lower() in ['y', 'yes', 'yeah']:
    print(f"Okay here is your order with {burger} and fries.")



