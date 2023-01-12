for n in range(1,11):
    match n % 2:
        case 0:
            print(f"{n} is even.")
        case 1:
            print(f"{n} is odd.")
            

for m in range(1, 101):
    match (m % 3, m % 5):
        case (0, 0):
            print(f"{m} is fizzbuzz.")
        case (_, 0):
            print(f"{m} is buzz.")
        case (0, _):
            print(f"{m} is fizz.")
        case (_, _):
            print(f"{m}")
