import math
import random

class Character:

    AtkChar = 0
    AtkWeapon = 0
    AtkBonus = 0
    FlatAtk = 0

    DefChar = 0
    DefBonus = 0
    FlatDmg = 0
    DmgBonus = 0

    CR = 0
    CD = 0

    LvlChar = 0

    EM = 0
    ReactionBonus = 0

    talent = 0

    defReduction = 0
    resistReduction = .0

    otherBonus = 1  # evilsoother

class Enemy:

    lvl = 100
    baseResist = .1

def main():
    
    # Character Template #
    template = Character()
    template.AtkChar = 0
    template.AtkWeapon = 0
    template.AtkBonus = 0
    template.FlatAtk = 0
    template.DefChar = 0
    template.DefBonus = 0
    template.FlatDmg = 0
    template.DmgBonus = 0
    template.CR = 0
    template.CD = 0
    template.LvlChar = 0
    template.EM = 0
    template.ReactionBonus = 0
    template.talent = 0
    template.defReduction = 0
    template.resistReduction = .0
    template.otherBonus = 1

    ### Character
    childe = Character()
    childe.LvlChar = 90
    childe.AtkChar = 301
    childe.AtkWeapon = 674
    childe.AtkBonus = .48 + .20 + .25 + .466       # ttds + noblesse + pyro 48 + 20 + 25
    childe.FlatAtk = 311 #+ 1000          # bennett buff
    childe.DefChar = 815
    childe.DefBonus = 0
    childe.FlatDmg = 0
    childe.DmgBonus = .754
    childe.CR = 0.7
    childe.CD = 1.4
    childe.EM = 200
    childe.ReactionBonus = 0
    childe.talent = 6.0544 # Lvl 8 ranged burst
    childe.resistReduction = .4

    raiden = Character()
    raiden.LvlChar = 90
    raiden.AtkChar = 337
    raiden.AtkWeapon = 674
    raiden.AtkBonus = .2
    raiden.FlatAtk = 311 + 1600
    raiden.DefChar = 0
    raiden.DefBonus = 0
    raiden.FlatDmg = 0
    raiden.DmgBonus = .32 + .2272*.25 + .466 + .3   # kazuha + emblem + goblet + raiden E
    raiden.CR = .765
    raiden.CD = 2.289
    raiden.talent = 7.2144+(60*7*.01)
    raiden.defReduction = .4
    raiden.resistReduction = .4

    ### Enemy

    # Formula calcs

    e = Enemy()

    #calc(childe, e)

    runCount = 100
    dmgArr = []
    for i in range(runCount):
        d = calc(raiden,e)
        dmgArr.append(d)
        print(d)

    print(f"\nAverage DMG over {runCount} runs: {sum(dmgArr)/runCount}")


def calc(c=Character(), e=Enemy()):

    # general


    # ampReaction
    ampReaction = 2 * (1 + (2.78 * c.EM) / (1400 + c.EM) + c.ReactionBonus)

    # enemyResMult
    resistance = e.baseResist - c.resistReduction

    enemyResMult = 0
    if resistance < 0:
        enemyResMult = 1 - (resistance / 2)
    elif resistance < 0.75:
        enemyResMult = 1 - resistance
    else:
        enemyResMult = 1 / (4 * resistance + 1)

    # enemyDefMult
    enemyDefMult = (c.LvlChar + 100) / ((c.LvlChar + 100) + (e.lvl + 100) * (1 - c.defReduction))

    # Crit Formula
    r = random.uniform(0, 1)
    crit = 1
    if (r < c.CR):
        crit = 1 + c.CD

    # attack
    attack = (c.AtkChar + c.AtkWeapon) * (1 + c.AtkBonus) + c.FlatAtk

    # baseDamage
    baseDamage = c.talent * attack + c.FlatDmg

    damage = baseDamage * (
                1 + c.DmgBonus) * crit * enemyDefMult * enemyResMult * ampReaction * c.otherBonus  # no transformative

    #print(f"{baseDamage=}\n{enemyDefMult=}\n{enemyResMult=}\n{ampReaction=}")

    #print(f"\n{attack=}")

    return damage




if __name__ == "__main__":
    main()
