from random import randint
import time
import pgzrun
WIDTH = 1400
HEIGHT = 750
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
error = 0
price = 0
health = 0
cash = 0
gems = 10
purgems = 0
upgrade1price = 500
upgrade2price = 500
opupgrade1price = 10
opupgrade2price = 100
opupgrade3price = 500
opupgrade4price = 1000
opupgrade5price = 100000
evolevedupgradeprice1 = 10
evolevedupgradeprice2 = 100
with open('cash.dat', 'r') as f:
    cash = int(f.read())
with open('gems.dat', 'r') as f:
    gems = int(f.read())
with open('purgems.dat', 'r') as f:
    purgems = int(f.read())
ores = ["emerald", "rainbow", "diamond", "black_diamond", "ruby", "stone", "gold", "purple_diamond", "shiny", "periore", "red_diamond", "rainbow_2", "jadeite", "fire", "glichore", "virus", "tanzanite", "taaffeite", "rainbow_3", "alexandrite"]
ore = ores[randint(0, 19)]
block = Actor(ore)
block.pos = CENTER_X, 600
upgrade1button = Actor("money")
upgrade1button.pos = 175, 500

upgrade2button = Actor("picaxe")
upgrade2button.pos = 175, 625

opupgrade1button = Actor("moreore")
opupgrade1button.pos = 1125, 500

opupgrade2button = Actor("ultra_ores")
opupgrade2button.pos = 1305, 500

opupgrade3button = Actor("ore_cleaner")
opupgrade3button.pos = 1125, 620

opupgrade4button = Actor("ore_digger")
opupgrade4button.pos = 1305, 620

opupgrade5button = Actor("glichore4")
opupgrade5button.pos = 1220, 720

evolevedupgradebutton1 = Actor("omegaores")
evolevedupgradebutton1.pos = 520, 500
evolevedupgradebutton2 = Actor("gemfinder")
evolevedupgradebutton2.pos = 720, 500

shopbutton = Actor("shopbutton")
shopbutton.pos = 1300, 100



changeore = Actor("1")

moreores = False
ultraores = False
glichore = False
omegaores = False
adminpannel = False

upgrade1 = 1
upgrade2 = 1
num = 1
orecleaner = 1
oredigger = 1
shop = False


def draw():
    global error
    if shop == True:
        screen.clear()
        screen.blit("shop", (0, 0))
        screen.draw.text("Cash: " + str(cash), color="white", pos=(200, 250))
        screen.draw.text("VER: 0.8.1(BETA) ", color="white", pos=(0, 0))
        screen.draw.text("price: " + str(upgrade1price), color="white", pos=(155, 550))
        screen.draw.text("price: " + str(upgrade2price), color="white", pos=(155, 700))
        screen.draw.text("price: " + str(opupgrade1price), color="white", pos=(1100, 420))
        screen.draw.text("price: " + str(opupgrade2price), color="white", pos=(1275, 420))
        screen.draw.text("price: " + str(opupgrade3price), color="white", pos=(1100, 550))
        screen.draw.text("price: " + str(opupgrade4price), color="white", pos=(1275, 550))
        screen.draw.text("price: " + str(opupgrade5price), color="white", pos=(1140, 670))
        screen.draw.text("price: " + str(evolevedupgradeprice1), color="white", pos=(500, 420))
        screen.draw.text("price: " + str(evolevedupgradeprice2), color="white", pos=(700, 420))
        screen.draw.text("Gems: " + str(gems), color="white", pos=(1200, 250))
        screen.draw.text("PurGems: " + str(purgems), color="white", pos=(CENTER_X, 250))
        upgrade1button.draw()
        upgrade2button.draw()
        opupgrade1button.draw()
        opupgrade2button.draw()
        opupgrade3button.draw()
        opupgrade4button.draw()
        opupgrade5button.draw()
        evolevedupgradebutton1.draw()
        evolevedupgradebutton2.draw()
        shopbutton.draw()
    else:
        screen.clear()
        screen.blit("bg", (0, 0))
        block.draw()
        changeore.draw()
        shopbutton.draw()
        screen.draw.text("Health: " + str(health), color="white", pos=(CENTER_X - 50, 705))
        screen.draw.text("Cash: " + str(cash), color="white", pos=(CENTER_X, 305))
        screen.draw.text("Gems: " + str(gems), color="white", pos=(CENTER_X, 325))
        screen.draw.text("VER: 0.8(BETA) ", color="white", pos=(0, 0))



def orechange():
    global ore, ores, block
    with open('cash.dat', 'w') as f:
        f.write(str(cash))
    with open('gems.dat', 'w') as f:
        f.write(str(gems))
    with open('purgems.dat', 'w') as f:
        f.write(str(purgems))
    ore = ores[randint(0,19)]
    block.image = ore
    block.pos = CENTER_X, 600
    healthprice()

def healthprice():
    global ore, health, price, moreores
    if ore == "emerald":
        health = 75
        price = health * 3
    elif ore == "rainbow":
        health = 250
        price = health * 3
    elif ore == "stone":
        health = 10
        price = health * 3
    elif ore == "black_diamond":
        health = 125
        price = health * 3
    elif ore == "ruby":
        health = 50
        price = health * 3
    elif ore == "diamond":
        health = 120
        price = health * 3
    elif ore == "gold":
        if not moreores:
            orechange()
        else:
            health = 1000
            price = health * 3
    elif ore == "purple_diamond":
        if not moreores:
            orechange()
        else:
            health = 5000
            price = health * 3

    elif ore == "shiny":
        if not moreores:
            orechange()
        else:
            health = 2500
            price = health * 3
    elif ore == "rainbow_2":
        if not ultraores:
            orechange()
        else:
            health = 10000
            price = health * 3
    elif ore == "red_diamond":
        if not ultraores:
            orechange()
        else:
            health = 15000
            price = health * 3
    elif ore == "fire":
        if not ultraores:
            orechange()
        else:
            health = 20000
            price = health * 3
    elif ore == "jadeite":
        if not ultraores:
            orechange()
        else:
            health = 50000
            price = health * 3
    elif ore == "periore":
        if not ultraores:
            orechange()
        else:
            health = 100000
            price = health * 3
    elif ore == "glichore":
        if not glichore:
            orechange()
        else:
            health = 99
            price = health * 3
    elif ore == "virus":
        if not omegaores:
            orechange()
        else:
            health = 150000
            price = health * 3
    elif ore == "tanzanite":
        if not omegaores:
            orechange()
        else:
            health = 250000
            price = health * 3
    elif ore == "taaffeite":
        if not omegaores:
            orechange()
        else:
            health = 500000
            price = health * 3
    elif ore == "rainbow_3":
        if not omegaores:
            orechange()
        else:
            health = 1000000
            price = health * 3
    elif ore == "alexandrite":
        if not omegaores:
            orechange()
        else:
            health = 750000
            price = health * 3

healthprice()
def RainbowChecker():
    global health, price, cash, upgrade1, upgrade2, upgrade1price, upgrade2price, gems, moreores, num
    for i in range(num):
        if health < 1:
            if ore == "rainbow":
                gems += 1
                cash = cash + price * upgrade1
                print(cash)
                orechange()
                check()
            else:
                cash = cash + price * upgrade1
                print(cash)
                orechange()



def on_mouse_down(pos):
    global health, price, cash, upgrade1, upgrade2, upgrade1price, upgrade2price, gems, moreores, ultraores, orecleaner, oredigger, shop, opupgrade4price, opupgrade5button, glichore, purgems, omegaores
    if block.collidepoint(pos):
        if health < 1:
            if ore == "rainbow":
                gems += 1
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            elif ore == "gold":
                gems += 3
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            elif ore == "shiny":
                gems += 5
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            elif ore == "purple_gem":
                gems += 10
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            if ore == "rainbow_2":
                gems += 25
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            elif ore == "red_diamond":
                gems += 50
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            elif ore == "fire":
                gems += 100
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            elif ore == "jadeite":
                gems += 250
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            elif ore == "periore":
                gems += 500
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            elif ore == "glich":
                purgems += 1
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            elif ore == "virus":
                purgems += 1.5
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            elif ore == "tanzanite":
                purgems += 2.5
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            elif ore == "taaffeite":
                purgems += 5
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            elif ore == "rainbow_3":
                purgems += 10
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            elif ore == "alexandrite":
                purgems += 7.5
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()

            else:
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
        else:
            health -= 1 * upgrade2
            print(price)
    elif upgrade1button.collidepoint(pos):
        if shop == True:
            if cash > upgrade1price:
                cash -= upgrade1price
                upgrade1price *= 3
                upgrade1 += 1
            else:
                print("no")
    elif upgrade2button.collidepoint(pos):
        if shop == True:
            if cash > upgrade2price:
                cash -= upgrade2price
                upgrade2price *= 3
                upgrade2 += 1
            else:
                print("no")
    elif changeore.collidepoint(pos):
        if health == 322:
            adminpannel = True
        else:
            orechange()
    elif opupgrade1button.collidepoint(pos):
        if shop == True:
            if gems < 10:
                print("no")
            elif moreores == True:
                print("no")
            else:
                moreores = True
                gems -= 10
    elif opupgrade2button.collidepoint(pos):
        if shop == True:
            if gems < 100:
                print("no")
            elif ultraores == True:
                print("no")
            else:
                ultraores = True
                gems -= 100
    elif opupgrade3button.collidepoint(pos):
        if shop == True:
            if gems < 500:
                print("no")
            elif orecleaner == 4:
                print("no")
            else:
                orecleaner = 4
                gems -= 500
    elif opupgrade4button.collidepoint(pos):
        if shop == True:
            if gems >= opupgrade4price:
                oredigger += 10
                gems -= opupgrade4price
                upgrade2 += 10
                opupgrade4price += 1000
            else:
                print("no")
    elif opupgrade5button.collidepoint(pos):
        if shop == True:
            if gems < opupgrade5price:
                print("no")
            elif glichore == True:
                print("no")
            else:
                glichore = True
                gems -= 100000
    elif evolevedupgradebutton1.collidepoint(pos):
        if shop == True:
            if purgems < evolevedupgradeprice1:
                print("no")
            elif omegaores == True:
                print("no")
            else:
                omegaores = True
                purgems -= 10
    elif shopbutton.collidepoint(pos):
        if shop == True:
            shop = False
            shopbutton.image = "shopbutton"
            draw()
        else:
            shop = True
            shopbutton.image = "shopclosebutton"
            draw()
pgzrun.go()
