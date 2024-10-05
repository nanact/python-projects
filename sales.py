cost = float(input("What is the cost"));

sale = float(input("how much is it sale"));

if cost < sale:
    print("You made profit");
    amount = sale - cost;
    print("profit = {0}".format(amount));
    
else:
    print("You lost profit");