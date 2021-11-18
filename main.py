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



def main():

    ### Character
    childe = Character

    childe.LvlChar = 90
    childe.AtkChar = 301
    childe.AtkWeapon = 674
    childe.AtkBonus = .48 + .20 + .25 + .466       # ttds + noblesse + pyro 48 + 20 + 25
    childe.FlatAtk = 311 #+ 1000          # bennett buff

    childe.DefChar = 815
    childe.DefBonus = 0
    childe.FlatDmg = 0
    childe.DmgBonus = .754

    childe.CR = 1
    childe.CD = 1.4

    EM = 200
    childe.ReactionBonus = 0

    childe.talent = 6.0544 # Lvl 8 ranged burst

    ### Enemy
    lvlEnemy = 100
    defReduction = 0

    baseResist = .1
    resistReduction = .4

    # Formula calcs

    # general
    otherBonus = 1      # evilsoother

    # ampReaction
    ampReaction = 2 * (1 + (2.78 * EM)/(1400 +EM) + childe.ReactionBonus)

    # enemyResMult
    resistance = baseResist - resistReduction

    enemyResMult = 0
    if resistance < 0:
        enemyResMult = 1 - (resistance/2)
    elif resistance < 0.75:
        enemyResMult = 1 - resistance
    else:
        enemyResMult = 1 / (4 * resistance + 1)

    # enemyDefMult
    enemyDefMult = (childe.LvlChar + 100)/((childe.LvlChar + 100) + (lvlEnemy + 100) * (1 - defReduction))

    # Crit Formula
    r = random.uniform(0, 1)
    crit = 1
    if (r < childe.CR):
        crit = 1 + childe.CD

    # attack
    attack = (childe.AtkChar + childe.AtkWeapon) * (1 + childe.AtkBonus) + childe.FlatAtk

    # baseDamage
    baseDamage = childe.talent * attack + childe.FlatDmg

    damage = baseDamage * (1 + childe.DmgBonus) * crit * enemyDefMult * enemyResMult * ampReaction * otherBonus # no transformative

    print(f"{baseDamage=}\n{enemyDefMult=}\n{enemyResMult=}\n{ampReaction=}")

    print(f"\n{attack=}")

    print("Damage Done (within 1%):", damage)





if __name__ == "__main__":
    main()
