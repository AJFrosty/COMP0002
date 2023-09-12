from Stock import Stock

inventory = Stock("FRO", "Frosty", 20.5,35.99)

print(
    f"Symbol is {inventory.getSymbol()}. Item is {inventory.getName()}. Previous price was {inventory.previousClosingPrice()}. Current Price is {inventory.getCurrentPrice()}. Change Percentage is {inventory.getChangePercentage()}"
    )