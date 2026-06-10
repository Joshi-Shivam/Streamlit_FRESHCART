cart={}
prize=[]
flag=0
from fpdf import FPDF
pdf=FPDF()
import time
print("Welcome to the grocery store!")
def fruit(cart,prize):
    item={
        "Apple": 20,
        "Banana": 10,
        "Orange": 15,
        "Mango": 50,
        "Peach": 40
    }
    print("Following is the menu of available fruits:")
    time.sleep(1.1)
    for i,j in item.items():
        print(f"{i} : {j} Rs/1 unit")
        #time.sleep(0.4)
    for i,j in enumerate(item.keys(),start=1):
        print(f"Press {i} to add {j} in the cart")
        #time.sleep(0.4)
    choice=int(input("Enter the choice" ))-1
    good=[]
    for i in item.keys():
        good.append(i)
    while True:
        quant=int(input(f"How many {good[choice]}'s you like to purchase per unit quantity\n(Maximum units at once are 15) "))
        if quant<=15 and quant>0:
            print(f"You added {quant} {good[choice]}'s in the cart")
            prize.append(item[good[choice]]*quant)
            if good[choice] in cart:
              cart[good[choice]]+=quant
            else:
              cart[good[choice]]=quant
            break
        else:
            print("Invalid quantity, please try again")

    return cart,prize
def vegies(cart,prize):
  item={
      "Tomato":10,
      "Onion":12,
      "Cabbage":10,
      "Potato":15,
      "Garlic":5,
      "Spinach":20
  }
  print("Following is the menu of available vegies:")
  for i,j in item.items():
    print(f"{i} for RS.{j}/1 unit")
  for i,j in enumerate(item.keys(),start=1):
    print(f"Press {i} to add {j} in the cart")
  choice=int(input("Enter your choice"))-1
  good=[]
  for i in item.keys():
    good.append(i)
  while True:
    quant=int(input(f"How many {good[choice]}'s you like to purchase per unit quantity\n(Maximum units at once are 15) "))
    if quant>0 and quant<=15:
      print(f"You added {quant} {good[choice]}'s in the cart")
      prize.append(item[good[choice]]*quant)
      if good[choice] not in cart:
        cart[good[choice]]=quant
      elif good[choice] in cart:
        cart[good[choice]]+=quant
      break
    else:
      print("Invalid quantity, please try again")
  return cart,prize

def Dairy(cart,prize):
  dairy={
      "Milk":20,
      "Egg":5,
      "Cheese":10,
      "Yougurt":25,
      "Butter":30,
      "Icecream":15
  }
  print("Following is the menu of available vegies:")
  for i,j in dairy.items():
    print(f"{i} for RS.{j}/1 unit")
  for i,j in enumerate(dairy.keys(),start=1):
    print(f"Press {i} to add {j} in the cart")
  choice=int(input("Enter your choice"))-1
  good=[]
  for i in dairy.keys():
    good.append(i)
  while True:
    quant=int(input(f"How many {good[choice]}'s you like to purchase per unit quantity\n(Maximum units at once are 15) "))
    if quant>0 and quant<=15:
      print(f"You added {quant} {good[choice]}'s in the cart")
      prize.append(dairy[good[choice]]*quant)
      if good[choice] not in cart:
        cart[good[choice]]=quant
      elif good[choice] in cart:
        cart[good[choice]]+=quant
      break
    else:
      print("Invalid quantity, please try again")
  return cart,prize
def General(cart,prize):
  stuff={
     "Broom":50,
     "Water bottel":10,
     "Waffers/Snacks":20,
     "Cold Drink":25,
     "Stationary":30,
     "Toothpaste":15,
     "Brush":10
  }
  print("Following is the menu of available vegies:")
  for i,j in stuff.items():
    print(f"{i} for RS.{j}/1 unit")
  for i,j in enumerate(stuff.keys(),start=1):
    print(f"Press {i} to add {j} in the cart")
  choice=int(input("Enter your choice"))-1
  good=[]
  for i in stuff.keys():
    good.append(i)
  while True:
    quant=int(input(f"How many {good[choice]}'s you like to purchase per unit quantity\n(Maximum units at once are 15) "))
    if quant>0 and quant<=15:
      print(f"You added {quant} {good[choice]}'s in the cart")
      prize.append(stuff[good[choice]]*quant)
      if good[choice] not in cart:
        cart[good[choice]]=quant
      elif good[choice] in cart:
        cart[good[choice]]+=quant
      break
    else:
      print("Invalid quantity, please try again")
  return cart,prize
def checkout(cart,prize,flag):
    while True:
        chance=input("Would you like to checkout and create bill or Shop more goods ? (Y for bill)\n(N to browse)").lower()
        if chance in ["y","n"]:
            if chance=="y":
                print("Thank you for shopping with us!")
                for i,j in cart.items():
                  print(f"Items :\n {i} Quantity : {j}")
                print(f"Total bill {sum(prize)}")
                flag=1
                pdf.add_page()
                pdf.set_font("Arial","B",size=20)
                pdf.cell(200,10,txt="Thank you for shopping with us!",ln=1,align="C")
                pdf.ln(10)
                pdf.set_font("Arial","B",12)
                pdf.cell(100,10,txt="Items",ln=0,align="L")
                pdf.cell(40,10,txt="Quantity",ln=1,align="R")
                for i,j in cart.items():
                    pdf.cell(100,10,txt=f"{i} ",ln=0,align="L")
                    pdf.cell(40,10,txt=f"{j}",ln=1,align="R")
                pdf.ln(8)
                pdf.cell(100,10,txt="________________________________________________________________",ln=1,align="R")
                pdf.cell(40,10,txt=fr"Total bill : {sum(prize)}",ln=2,align="R")
                pdf.output("Your Bill2.pdf")
                break
            else:
                break

        else:
            print("Invalid input try again")
    return flag
def main(cart,prize,flag):
  while True:
    if flag==1:
      break
    else:
      category=["Fruits","Vegetables","Dairy","General Stuff"]
      for i,y in enumerate(category,start=1):
          print(f"Press {i} to browse items in {y}")
      while True:
          choice=int(input("Enter your choice :"))
          if choice not in [1,2,3,4]:
              print("invald choice, please try again")
          else:
              if choice==1:
                  cart,prize=fruit(cart,prize)
                  flag=checkout(cart,prize,flag)
                  break
              elif choice==2:
                  cart,prize=vegies(cart,prize)
                  flag=checkout(cart,prize,flag)
                  break
              elif choice==3:
                  cart,prize=Dairy(cart,prize)
                  flag=checkout(cart,prize,flag)
                  break
              elif choice==4:
                General(cart,prize)
                flag=checkout(cart,prize,flag)
                break
              else:
                  print("Invalid choice, please try again")
if __name__=="__main__":
    main(cart,prize,flag)