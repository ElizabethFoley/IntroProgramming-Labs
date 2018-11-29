# CMPT120 Intro to Programming
# Lab 9
# 11-29=18

productNames = [ "Ultrasonic range finder",
                 "Servo motor",
                 "Microcontroller Board",
                 "Laser range finder",
                 "Lithium polymer battery"
                ]

productPrices = [ 2.50, 14.99, 44.95, 34.95, 149.99, 8.99 ]
productQuantities = [ 4, 10, 5, 7, 2, 8 ]

def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(productNames)):
        if productQuantities[i] > 0:
            print(str(i)+")",productNames[i], "$" , productPrices[i])
    print()

def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()

        vals = input("Enter product ID and quantity you wish to buy: ")split(" ")
        if vals[0] == "quit":
            break
        proId = int(vals[0])
        count = int(vals[1])

        if productQuantities[proId] >= count:
            if cash >= productPrices[proId] * count:
                productQuantities[proId] -= count
                cash -= productPrices[proId] * count
                print("You purchased" , count, productNames[proId] + ".")
                print("You have $" , "{0: 2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of" , productNames[proId])

main()
            
                 
