# Promoção de gratuidade na entrada para pessoas em crise de meia idade 45 a 55 anos.
# Uso das cond

print("Welcome to the rollercoaster!")
height = int(input("Whats is your height in cm? \n"))
ticketValue = 0
if height >= 120:
    age = int(input("how old are you? \n "))
    if age <= 12:
        ticketValue = 5
        print("Child tickets are $5,00")
    elif age <=18:
        ticketValue = 7
        print("youth tickets are $7,00")
    elif   45 <=  age <=55: # simplificação de compração
        ticketValue = 0
    else:
        ticketValue = 12
        print("Adult tickets are $12,00")
    
    wantsPhoto = input("Do you want a to have a photo take? Type Y or N \n").upper()
    if wantsPhoto == "Y":
        ticketValue  += 3
        
    
    
    print(f"Please pay ${ticketValue:.2f} for ticket.")    


else:
    print("you can't ride the rollercoaster!")    

