def feast(beast, dish):
    first_leater_from_beast = beast[0]
    last_leater_from_beast = beast[-1]

    first_leater_from_dish = dish[0]
    last_leater_from_dish = dish[-1]

    if first_leater_from_beast == first_leater_from_dish and last_leater_from_beast == last_leater_from_dish:
        return True
    else:
        return False

print(feast("brown bear", "bear claw"))
