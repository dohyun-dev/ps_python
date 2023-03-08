CASH = int(input())
chart = list(map(int, input().split()))
J_arr, S_arr = [CASH, 0], [CASH, 0]

for i, price in enumerate(chart):
    if price <= J_arr[0]:
        J_arr[1] += J_arr[0] // price
        J_arr[0] -= J_arr[0] // price * price

up_cnt, down_cnt = 0, 0
for i, price in enumerate(chart):
    if i != 0 and chart[i-1] < price:
        up_cnt += 1
        down_cnt = 0
    elif i != 0 and chart[i-1] > price:
        up_cnt = 0
        down_cnt += 1
    elif i != 0 and chart[i-1] == price:
        up_cnt = 0
        down_cnt = 0

    if up_cnt == 3:
        S_arr[0] += price * S_arr[1]
        S_arr[1] = 0
        up_cnt = 0
    elif down_cnt == 3:
        S_arr[1] += S_arr[0] // price
        S_arr[0] -= S_arr[0] // price * price

if J_arr[0] + (J_arr[1] * chart[-1]) > S_arr[0] + (S_arr[1] * S_arr[-1]):
    print("BNP")
elif J_arr[0] + (J_arr[1] * chart[-1]) == S_arr[0] + (S_arr[1] * S_arr[-1]):
    print("SAMESAME")
else:
    print("TIMING")