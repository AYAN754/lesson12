def total_calc(bill,tip):
    total=bill*(1+0.01*tip)
    total=round(total,2)
    print("please pay",total)
total_calc(150,20)