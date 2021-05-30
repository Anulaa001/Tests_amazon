
def is_triplet(arr):
    n = len(arr)

    for i in range(n):
        arr[i] = arr[i] * arr[i]

    arr.sort()
    for i in range(n - 1, 1, -1):
        j = 0
        k = i - 1
        while j < k:
            if arr[j] + arr[k] == arr[i]:
                return True
            else:
                if arr[j] + arr[k] < arr[i]:
                    j += 1
                else:
                    k -= 1
    return False


def find_position_of_multiplication_in_fibonacci(k, n):
    f1 = 0
    f2 = 1
    i = 2
    while i != 0:
        f3 = f1 + f2
        f1 = f2
        f2 = f3

        if f2 % k == 0:
            return n * i

        i += 1

    return


def find_remainder_of_division(arr, n):
    mul = 1

    for i in arr:
        mul = mul * (i % n)

    return mul % n


def first_not_repeated_value(str1):
    output = []
    mind = {}

    for e in str1:
        if e not in mind:
            mind[e] = 0
        mind[e] += 1
    if len(mind) == 0:
        return output
    for e, count in mind.items():
        if count == 1:
            output.append(e)

    if len(output) > 0:
        return output[0]
    else:
        return []


def search_list_by_substring(arr, subs):
    lowered_arr = sorted(a.lower() for a in arr)
    matched_word = []
    if len(subs) < 2:
        print("Substring length should be at  least 2 characters!")

    for i in range(1, len(subs)):
        sub = subs[0:i + 1]

        for a in lowered_arr:
            if a.startswith(sub):
                matched_word.append(a)

    return matched_word


def pwd_validation(pwd):
    while True:
        if len(pwd) < 8:
            return False

        if not any(char.isdigit() for char in pwd):
            return False

        if not any(char.isupper() for char in pwd):
            return False

        else:
            return True
