def hide_credit_card_number():
    card_number = input("Enter your 16 digit credit card number: ")
    while len(card_number) != 16:
        print("Try again! ")
        card_number = input("Enter your 16 digit credit card number: ")
    hide_card_number = card_number[12:16]
    hide_card_number_two = "-" * 12
    print(hide_card_number_two + hide_card_number)

hide_credit_card_number()
