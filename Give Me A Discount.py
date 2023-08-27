def give_me_a_discount(full_price, discount):
    discounted = full_price * ((1-discount/100))
    print("The cost with a discount will be : " + str(discounted))


give_me_a_discount(100, 60)
