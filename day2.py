#DAY -> 2
# Q1-> simple market system using OOPs concept
def menu():
    av_it={
        "milk":20,
        "bread":30,
        "eggs":10,
        "fruits":50,
        "vegetables":40,
        "newspaper":15,
        "magazine":25,
        "book":100,
    }
    return av_it
    
    
class shop:
    def __init__(self,name):
        self.name=name
        self.items={}
    def display_menu(self):
        print(f"Welcome to {self.name} shopping cart !!")
        av_it=menu()
        for item,price in av_it.items():
            print(f"{item}: {price} rs per pack!!")
    

    def item_selection(self):

        while True:
            print()
            item=input("enter the item to add to cart or 'done' to finish: ")
            if item.lower()=="done":
                break
            n=int(input("enter the quantity: "))
            self.items[item] = n

        return self.items
    def items_selected(self):
        for item,quantity in self.items.items():
            print(f"{item}: {quantity} packs")

    def billing(self):
        total_price=0
        av_it=menu()
        for item,quan in self.items.items():
            cost_of_this_item=av_it[item]*quan
            total_price+=cost_of_this_item
            print(f"{item}:{quan}X{av_it[item]} = {cost_of_this_item} rs")
        print(f"total price: {total_price} rs!!")
        print("Thank you for shopping with us!!")

def day1():
    shop1=shop("sin30 supermarket")
    c=input("would u like to see the menu? (y/n): ")
    if c=="y":
        shop1.display_menu()
        c=input("would u like to add items to cart? (y/n): ")
        if c=="y":
            shop1.item_selection()
            c=input("would u like to see the items selected? (y/n): ")
            if c=="y":
                shop1.items_selected()
                shop1.billing()
            else:
                shop1.billing()
                

        else:
            print("Thank you for visiting!!")
    else:
        print("Thank you for visiting!!")
#q2-> Calculating the BMI of a fitneser
class BMI:
    def __init__(self,h,w):
        self.h=h
        self.w=w
        self.BMI=0
    def calculate_BMI(self):
        self.BMI= self.w/(self.h*self.h)

    def __str__(self):
        self.calculate_BMI()
        return str(self.BMI)

def d22():
    akshay=BMI(1.75,50)
    print(akshay)

    

    

