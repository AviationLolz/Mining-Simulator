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
try:
    with open('DATA/cash.dat', 'r') as f:
        cash = int(f.read())
    with open('DATA/gems.dat', 'r') as f:
        gems = int(f.read())
    with open('DATA/purgems.dat', 'r') as f:
        purgems = int(f.read())
except:
    input("NOTICE!: data may be corrupt or interfeired with.do you want to reset (Y/N)")
ores = ["emerald", "rainbow", "diamond", "black_diamond", "ruby", "stone", "gold", "purple_diamond", "shiny", "periore", "red_diamond", "rainbow_2", "jadeite", "fire", "glichore", "virus", "tanzanite", "taaffeite", "rainbow_3", "alexandrite"]
ore = ores[randint(0, 19)]
block = Actor(ore)
block.pos = CENTER_X, 600
upgrade1button = Actor("money")
upgrade1button.pos = 175, 500

upgrade2button = Actor("picaxe")
upgrade2button.pos = 375, 500

opupgrade1button = Actor("moreore")
opupgrade1button.pos = 175, 500

opupgrade2button = Actor("ultra_ores")
opupgrade2button.pos = 375, 500

opupgrade3button = Actor("ore_cleaner")
opupgrade3button.pos = 575, 500

opupgrade4button = Actor("ore_digger")
opupgrade4button.pos = 775, 500

opupgrade5button = Actor("glichore4")
opupgrade5button.pos = CENTER_X, 670

evolevedupgradebutton1 = Actor("omegaores")
evolevedupgradebutton1.pos = 175, 500
evolevedupgradebutton2 = Actor("gemfinder")
evolevedupgradebutton2.pos = 375, 500

shopbutton = Actor("shopbutton")
shopbutton.pos = 1300, 100

upgradeA = Actor("shop0")
upgradeA.pos = 400, 350

upgradeB = Actor("shop1")
upgradeB.pos = 700, 350

upgradeC = Actor("shop2")
upgradeC.pos = 1000, 350

changeore = Actor("1")

backbutton = Actor("back")
backbutton.pos = 1125, 100


adminpannel = False
home = True
with open('DATA/opupgrade1.dat', 'r') as f:
    moreores = f.read()
with open('DATA/opupgrade2.dat', 'r') as f:
    ultraores = f.read()
with open('DATA/opupgrade5.dat', 'r') as f:
    glichore = f.read()
with open('DATA/eupgrade1.dat', 'r') as f:
    omegaores = f.read()

with open('DATA/upgrade1.dat', 'r') as f:
    upgrade1 = int(f.read())
with open('DATA/upgrade2.dat', 'r') as f:
    upgrade2 = int(f.read())
with open('DATA/opupgrade3.dat', 'r') as f:
    orecleaner = int(f.read())
with open('DATA/opupgrade4.dat', 'r') as f:
    oredigger = int(f.read())
shop = False
pshop = False
gshop = False
ushop = False
print(omegaores)
def draw():
    global error
    if shop == True:
        screen.clear()
        screen.blit("shop", (0, 0))
        upgradeA.draw()
        upgradeB.draw()
        upgradeC.draw()
        backbutton.draw()
    elif ushop == True:
        screen.clear()
        screen.blit("ushop", (0, 0))
        upgrade2button.pos = 375, 500
        upgrade1button.pos = 175, 500
        screen.draw.text("Cash: " + str(cash), color="white", pos=(CENTER_X - 35, 350))
        screen.draw.text("price: " + str(upgrade1price), color="white", pos=(175, 550))
        screen.draw.text("price: " + str(upgrade2price), color="white", pos=(375, 550))
        screen.draw.text("VER: 0.8.2(BETA) ", color="white", pos=(0, 0))
        upgrade1button.draw()
        upgrade2button.draw()
        shopbutton.draw()
    elif gshop == True:
        screen.clear()
        screen.blit("gshop", (0, 0))
        upgrade2button.pos = 375, 1500
        upgrade1button.pos = 375, 1500
        screen.draw.text("Gems: " + str(gems), color="white", pos=(CENTER_X - 35, 350))
        screen.draw.text("price: " + str(opupgrade1price), color="white", pos=(175, 550))
        screen.draw.text("price: " + str(opupgrade2price), color="white", pos=(375, 550))
        screen.draw.text("price: " + str(opupgrade3price), color="white", pos=(575, 550))
        screen.draw.text("price: " + str(opupgrade4price), color="white", pos=(775, 550))
        screen.draw.text("price: " + str(opupgrade5price), color="white", pos=(CENTER_X - 35, 720))
        opupgrade1button.draw()
        opupgrade2button.draw()
        opupgrade3button.draw()
        opupgrade4button.draw()
        opupgrade5button.draw()
        shopbutton.draw()
        block.pos = CENTER_X, 2000
    elif pshop == True:
        screen.clear()
        screen.blit("pshop", (0, 0))
        screen.draw.text("price: " + str(evolevedupgradeprice1), color="white", pos=(175, 550))
        screen.draw.text("price: " + str(evolevedupgradeprice2), color="white", pos=(375, 550))
        screen.draw.text("PurGems: " + str(purgems), color="white", pos=(CENTER_X - 35, 350))
        evolevedupgradebutton1.draw()
        evolevedupgradebutton2.draw()
        shopbutton.draw()


    elif home == True:
        screen.clear()
        screen.blit("bg", (0, 0))
        block.draw()
        changeore.draw()
        shopbutton.draw()
        screen.draw.text("Health: " + str(health), color="white", pos=(CENTER_X - 50, 705))
        screen.draw.text("Cash: " + str(cash), color="white", pos=(CENTER_X - 50, 315))
        screen.draw.text("Gems: " + str(gems), color="white", pos=(CENTER_X - 50, 335))
        screen.draw.text("VER: 0.8.2(BETA) ", color="white", pos=(0, 0))
        block.pos = CENTER_X, 600



def orechange():
    global ore, ores, block
    with open('DATA/cash.dat', 'w') as f:
        f.write(str(cash))
    with open('DATA/gems.dat', 'w') as f:
        f.write(str(gems))
    with open('DATA/purgems.dat', 'w') as f:
        f.write(str(purgems))
    ore = ores[randint(0,19)]
    block.pos = CENTER_X, 600
    healthprice()

def healthprice():
    global ore, health, price, moreores
    if ore == "emerald":
        block.image = ore
        health = 75
        price = 75 * 1
    elif ore == "rainbow":
        block.image = ore
        health = 250
        price = 250 * 1
    elif ore == "stone":
        block.image = ore
        health = 10
        price = 10 * 1

    elif ore == "black_diamond":
        block.image = ore
        health = 125
        price = 125 * 1

    elif ore == "ruby":
        block.image = ore
        health = 50
        price = 50 * 1

    elif ore == "diamond":
        block.image = ore
        health = 120
        price = 120 * 1

    elif ore == "gold":
        if moreores == True:
            block.image = ore
            health = 1000
            price = health * 1
        else:
            orechange()

    elif ore == "purple_diamond":
        if moreores == True:
            block.image = ore
            health = 5000
            price = health * 1
        else:
            orechange()

    elif ore == "shiny":
        if moreores == True:
            block.image = ore
            health = 2500
            price = health * 1
        else:
            orechange()

    elif ore == "rainbow_2":
        if ultraores == True:
            block.image = ore
            health = 10000
            price = health * 1
        else:
            orechange()

    elif ore == "red_diamond":
        if ultraores == True:
            block.image = ore
            health = 15000
            price = health * 1
        else:
            orechange()

    elif ore == "fire":
        if ultraores == True:
            block.image = ore
            health = 20000
            price = health * 1
        else:
            orechange()

    elif ore == "jadeite":
        if ultraores == True:
            block.image = ore
            health = 50000
            price = health * 1
        else:
            orechange()
    elif ore == "periore":
        if ultraores == True:
            block.image = ore
            health = 100000
            price = health * 1
        else:
            orechange()

    elif ore == "glichore":
        if glichore == True:
            block.image = ore
            health = 99
            price = health * 1
        else:
            orechange()

    elif ore == "virus":
        if omegaores == True:
            block.image = ore
            health = 150000
            price = health * 1
        else:
            orechange()

    elif ore == "tanzanite":
        if omegaores == True:
            block.image = ore
            health = 250000
            price = health * 1
        else:
            orechange()
            
    elif ore == "taaffeite":
        if omegaores == True:
            block.image = ore
            health = 500000
            price = health * 1
        else:
            orechange()

    elif ore == "rainbow_3":
        if omegaores == True:
            block.image = ore
            health = 1000000
            price = health * 1
        else:
            orechange()

    elif ore == "alexandrite":
        if omegaores == True:
            block.image = ore
            health = 750000
            price = health * 1
        else:
            orechange()
"""["emerald", "rainbow", "diamond", "black_diamond", "ruby", "stone", "gold", "purple_diamond", "shiny", "periore", "red_diamond", "rainbow_2", "jadeite", "fire", "glichore", "virus", "tanzanite", "taaffeite", "rainbow_3", "alexandrite"]
"""
healthprice()
def RainbowChecker():
    global health, price, cash, upgrade1, upgrade2, upgrade1price, upgrade2price, gems, moreores, num
    if health < 2:
        if ore == ores[5]:
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()
        if ore == ores[1]:
            gems += 1
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()
        if ore == ores[0]:
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()
        if ore == ores[4]:
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()
        if ore == ores[2]:
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()
        if ore == ores[3]:
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()
        if ore ==ores[6]:
            gems += 3
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()
        if ore == ores[8]:
            gems += 5
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()
        if ore == ores[7]:
            gems += 10
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()
        if ore == ores[11]:
            gems += 25
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()
        if ore == ores[10]:
            gems += 50
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()
        if ore == ores[13]:
            gems += 100
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()
        if ore == ores[12]:
            gems += 250
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()
        if ore == ores[9]:
            gems += 500
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()
        if ore == ores[14]:
            purgems += 1
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()
        if ore == ores[15]:
            purgems += 2
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()
        if ore == ores[16]:
            purgems += 3
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()
        if ore == ores[17]:
            purgems += 5
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()
        if ore == ores[18]:
            purgems += 10
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()
        if ore == ores[19]:
            purgems += 7
            cash = cash + price * upgrade1 * oredigger * orecleaner
            print(cash)
            orechange()

def on_mouse_down(pos):
    global pshop, ushop, gshop, health, price, cash, upgrade1, upgrade2, upgrade1price, upgrade2price, gems, moreores, ultraores, orecleaner, oredigger, shop, opupgrade4price, opupgrade5button, glichore, purgems, omegaores
    if block.collidepoint(pos):
        print(price)
        if health < 1:
            RainbowChecker()
            """
            if ore == "emerald":
                cash -= price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            elif ore == "stone":
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            elif ore == "black_diamond":
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            elif ore == "ruby":
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            elif ore == "diamond":
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            elif ore == "rainbow":
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
                purgems += 2
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()
            elif ore == "tanzanite":
                purgems += 3
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
                purgems += 7
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()

            else:
                cash = cash + price * upgrade1 * oredigger * orecleaner
                print(cash)
                orechange()

"""
        else:
            health -= (1 * upgrade2)
    elif upgrade1button.collidepoint(pos):
        if ushop == True:
            if cash > upgrade1price:
                cash -= upgrade1price
                upgrade1price *= 3
                upgrade1 += 0.1
                with open('DATA/upgrade1.dat', 'w') as f:
                    f.write(str(upgrade1))
            else:
                print("no")
    elif upgrade2button.collidepoint(pos):
        if ushop == True:
            if cash > upgrade2price:
                cash -= upgrade2price
                upgrade2price *= 3
                upgrade2 += 1
                with open('DATA/upgrade2.dat', 'w') as f:
                    f.write(str(upgrade2))
            else:
                print("no")
    elif changeore.collidepoint(pos):
        if health == 322:
            adminpannel = True
        else:
            orechange()
    elif opupgrade1button.collidepoint(pos):
        if gshop == True:
            if gems < 10:
                print("no")
            elif moreores == True:
                print("no")
            else:
                moreores = True
                gems -= 10
                with open('DATA/opupgrade1.dat', 'w') as f:
                    f.write(str(moreores))
    elif opupgrade2button.collidepoint(pos):
        if gshop == True:
            if gems < 100:
                print("no")
            elif ultraores == True:
                print("no")
            else:
                with open('DATA/opupgrade2.dat', 'w') as f:
                    f.write(str(ultraores))
                ultraores = True
                gems -= 100
    elif opupgrade3button.collidepoint(pos):
        if gshop == True:
            if gems < 500:
                print("no")
            elif orecleaner == 4:
                print("no")
            else:
                orecleaner = 4
                gems -= 500
                with open('DATA/opupgrade3.dat', 'w') as f:
                    f.write(str(orecleaner))
    elif opupgrade4button.collidepoint(pos):
        if gshop == True:
            if gems >= opupgrade4price:
                oredigger += 10
                gems -= opupgrade4price
                upgrade2 += 10
                with open('DATA/upgrade2.dat', 'w') as f:
                    f.write(str(upgrade2))
                with open('DATA/opupgrade4.dat', 'w') as f:
                    f.write(str(oredigger))
            else:
                print("no")
    elif opupgrade5button.collidepoint(pos):
        if gshop == True:
            if gems < opupgrade5price:
                print("no")
            elif glichore == True:
                print("no")
            else:
                glichore = True
                gems -= 100000
                with open('DATA/opupgrade2.dat', 'w') as f:
                    f.write(str(glichore))
    elif evolevedupgradebutton1.collidepoint(pos):
        if pshop == True:
            if purgems < evolevedupgradeprice1:
                print("no")
            elif omegaores == True:
                print("no")
            else:
                omegaores = True
                purgems -= 10
                with open('DATA/eupgrade1.dat', 'w') as f:
                    f.write(str(omegaores))

    elif evolevedupgradebutton2.collidepoint(pos):
        if pshop == True:
            if purgems < evolevedupgradeprice2:
                print("no")
            elif omegaores == True:
                print("no")
            else:
                omegaores = True
                purgems -= 100

    elif upgradeA.collidepoint(pos):
        if shop == True:
            ushop = True
            shop = False
    elif upgradeB.collidepoint(pos):
        if shop == True:
            gshop = True
            shop = False
    elif upgradeC.collidepoint(pos):
        if shop == True:
            pshop = True
            shop = False
    elif backbutton.collidepoint(pos):
        print("1")
        shop = False
        shopbutton.image = "shopbutton"
        pshop = False
        gshop = False
        ushop = False
        home = True
    elif shopbutton.collidepoint(pos):
        if shop == True:
            shop = False
            shopbutton.image = "shopbutton"
            pshop = False
            gshop = False
            ushop = False
            home = True
        elif shop == False:
            print("1")
            shop = True
            shopbutton.image = "shopclosebutton"
            pshop = False
            gshop = False
            ushop = False
    
        else:
            print("1")
pgzrun.go()
