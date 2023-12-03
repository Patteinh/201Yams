import math

def prob_to_str(s, prob):
    return f"Chances to get a {s}: {prob:.2f}%"

def combination(k, n):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def binomial(k, n):
    comb = combination(k, n)
    p = (1/6) ** k
    pc = (5/6) ** (n - k)
    return comb * p * pc

def count_good_values(data, nbr):
    return sum(1 for d in data if d == nbr)

def count_straight_values(data, start, end):
    return sum(1 for d in data if start <= d < end)

def start_basic(data):
    count = count_good_values(data['d'], data['nbr'][0])
    if count >= data['v']:
        print(prob_to_str(data['s'], 100))
    else:
        prob = sum(binomial(i, 5 - count) for i in range(data['v'] - count, 5 - count + 1))
        print(prob_to_str(f"{data['nbr'][0]} {data['s']}", prob * 100))

def start_full(data):
    count1 = count_good_values(data['d'], data['nbr'][0])
    count2 = count_good_values(data['d'], data['nbr'][1])
    if count1 == 3 and count2 == 2:
        print(prob_to_str(data['v'], data['s'], 100))
    else:
        count1, count2 = min(count1, 3), min(count2, 2)
        three = combination(3 - count1, 5 - count1 - count2)
        pair = combination(2 - count2, 2 - count2)
        prob = three * pair / 6**(5 - count1 - count2)
        print(prob_to_str(f"{data['nbr'][0]} full of {data['nbr'][1]}", prob * 100))

def start_straight(data):
    count = count_straight_values(data['d'], data['nbr'][0], data['nbr'][0] + 5)
    if count == 5:
        print(prob_to_str(data['s'], 100))
    else:
        prob = math.factorial(5 - count) / 6**(5 - count)
        print(prob_to_str(f"{data['nbr'][0]} {data['s']}", prob * 100))

def start_yams(data):
    if data['combination'] in {'pair', 'three', 'four', 'yams'}:
        start_basic(data)
    elif data['combination'] == 'full':
        start_full(data)
    elif data['combination'] == 'straight':
        start_straight(data)
