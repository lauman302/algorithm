def buy_bicycles(money, price, left, right):
    if right <= left and left != 0:
        return -1
    mid = (left + right) // 2
    if (money[mid] >= price and (money[mid - 1] < price or mid == 0))
        return mid + 1
    elif price <= money[mid]:
        return buy_bicycles(money, price, left, mid)
    else:
        return buy_bicycles(money, price, mid + 1, right)


if __name__ == '__main__':
    days = int(input())
    money = [int(num) for num in input().split(' ')]
    price = int(input())
    print(buy_bicycles(money, price, 0, days), end=' ')
    print(buy_bicycles(money, price * 2, 0, days))

def gen_binary(n, prefix):
    if n == 0:
        print(prefix) 
    else:
        gen_binary(n - 1, prefix + '0')
        gen_binary(n - 1, prefix + '1')

gen_binary(5, 'ol')


# 6
# 1 2 4 4 4 4
# 0 1 2 3 4 5
# 1
# mid[3] = 4
# left = 0, right = 3
# mid[1] = 2
