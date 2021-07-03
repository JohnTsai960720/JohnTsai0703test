from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

from random import choice
cards_symbol = ["黑桃","梅花","愛心","方塊"]
cards_number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
Player1_card=[]
Player2_card=[]

def Player1(status):
    if status == "ok":
        print("ok")
    elif status == "not ok":
        print("get ready")
    else:
        print("錯誤，再試試")
Player1(input("Please enter your status(ok or not ok):"))

for i in range (1,5):
    card_combine = [choice(cards_symbol)+choice(cards_number)]
    Player1_card.append(card_combine)
print(Player1_card)

mc.setSign(x,y,z,63,0,"Player1_card",Player1_card[0],Player1_card[1],Player1_card[2],Player1_card[3])

def Player2(status):
    if status == "ok":
        print("ok")
    elif status == "not ok":
        print("get ready")
    else:
        print("錯誤，再試試")
Player2(input("Please enter your status(ok or not ok):"))

for i in range (1,5):
    card_combine = [choice(cards_symbol)+choice(cards_number)]
    Player2_card.append(card_combine)
print(Player2_card)

mc.setSign(x,y,z,63,0,"Player2_card",Player2_card[0],Player2_card[1],Player2_card[2],Player2_card[3])   
    

                

