def to_egy_pound (amount, currency):
    currency = currency.upper()
    if amount == 0:
        return 0
    else:
        if currency == 'USD':
            output = amount * 21.23
        elif currency == 'EUR':
            output = amount * 15.76
        elif currency == 'GBP':
            output = amount * 24.30
        elif currency == 'KWD':
            output = amount * 64.41
        return output
        
print(to_egy_pound(0, 'USD'), "L.E")
print(to_egy_pound(500, 'USD'), "L.E")
print(to_egy_pound(500, 'EUR'), "L.E")
print(to_egy_pound(500, 'GBP'), "L.E")
print(to_egy_pound(500, 'KWD'), "L.E")

        
    