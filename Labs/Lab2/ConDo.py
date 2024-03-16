def ferry_crossings(l, m, cars):
    left_bank, right_bank = [], []

    for car in cars:
        length, bank = car[0], car[1]
        if bank == "left":
            left_bank.append(length)
        else:
            right_bank.append(length)

    crossings = 0
    current_bank = left_bank
    other_bank = right_bank

    while left_bank or right_bank:
        if not current_bank:
            current_bank, other_bank = other_bank, current_bank
            crossings += 1
        else:
            total_length = 0
            while current_bank and total_length + current_bank[0] <= l * 100:
                total_length += current_bank.pop(0)
            current_bank, other_bank = other_bank, current_bank
            crossings += 1

    return crossings

def main():
    l, m = map(int, input().split())
    cars = [input().split() for _ in range(m)]

    for i in range(m):
        cars[i][0] = int(cars[i][0])

    result = ferry_crossings(l, m, cars)
    print(result)

if __name__ == "__main__":
    main()