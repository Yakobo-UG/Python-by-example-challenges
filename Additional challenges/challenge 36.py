#You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory. Return the total profit made, rounded to the nearest dollar. Assume all of the inventory has been sold.
sellUnits = 30
costUnits = 20
def totalProfit(inventory, cost, sell):
    Total = ((sell*sellUnits) - (cost*costUnits)) + inventory
    return "the profit is", Total
print(totalProfit(10, 3000, 4000))

