# CMPT120 Intro to Programming
# Lab 9
# 11-29=18


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def testStock(self, stock):
        if self.quantity >= stock:
            return True
        else:
            return False
    def totalCost(self, amount):
        totalCost = self.price * amount
        return totalCost
    def takeItem(self, amount):
        self.quantity -= amount

product = [ Product("Ultrasonic range finder" , 2.50 , 4),
            Product("Servo motor" , 14.99 , 10),
            Product("Servo controller" , 44.95 , 5),  
            Product("Microcontroller Board" , 34.95 , 7),
            Product("Laser range finder" , 149.99 , 2),
            Product("Lithium polymer battery" , 8.99 , 8)
            ]

def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(product)):
        if product[i].testStock(1):
            print(str(i)+")",product[i].name, "$" , product[i].price)
    print()

def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()

        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit":
            break
        proId = int(vals[0])
        count = int(vals[1])

        if product[proId].testStock(count):
            if cash >= product[proId].totalCost(count):
                product[proId].takeItem(count)
                cash -= product[proId].totalCost(count)
                print("You purchased" , count, product[proId].name + ".")
                print("You have $" , "{0: 2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of" , product[proId].name)

main()
            
                 
