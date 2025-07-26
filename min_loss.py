prices = [20,15,7,13]
if len(prices)!=len(set(prices)):
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] == prices[j]:
                print(f"If buy is in year {i+1}, sell in year {j+1}, then No loss")
                break
else:
    min_loss = float('inf')
    buy_year = -1
    sell_year = -1
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] < prices[i]:
                loss = prices[i] - prices[j]
                if loss < min_loss:
                    min_loss = loss
                    buy_year = i + 1
                    sell_year = j + 1

    if buy_year == -1:
        print("No valid loss possible") 
    else:
        print(f"If buy is {buy_year}, sell is {sell_year}, then loss is {min_loss}")    