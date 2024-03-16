def min_insertions_to_make_continuous(arr):
    arr_set = set(arr)
    max_num = max(arr)
    min_num = min(arr)

    count = 0
    for num in range(min_num, max_num):
        if num not in arr_set:
            count += 1

    return count

def main():
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    result = min_insertions_to_make_continuous(arr)
    print(result)

if __name__ == "__main__":
    main()