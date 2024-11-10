
def total_calcu(realamount,tip_pentange):
    total = realamount*(1 + 0.01 * tip_pentange)
    total = round(total,2)
    print(f"Please pay ${total}")


total_calcu(15,10)