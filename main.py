import math
import random
from artifact import Artifact
from character import Character
from enemy import Enemy

def main():

    # ### Character
    # childe = Character()
    # childe.LvlChar = 90
    # childe.AtkChar = 301
    # childe.AtkWeapon = 674
    # childe.AtkBonus = .48 + .20 + .25 + .466       # ttds + noblesse + pyro 48 + 20 + 25
    # childe.FlatAtk = 311 #+ 1000          # bennett buff
    # childe.DefChar = 815
    # childe.DefBonus = 0
    # childe.FlatDmg = 0
    # childe.DmgBonus = .754
    # childe.CR = 0.7
    # childe.CD = 1.4
    # childe.EM = 200
    # childe.ReactionBonus = 0
    # childe.talent = 6.0544 # Lvl 8 ranged burst
    # childe.resistReduction = .4
    #
    # raiden = Character()
    # raiden.LvlChar = 90
    # raiden.AtkChar = 337
    # raiden.AtkWeapon = 674
    # raiden.AtkBonus = .2
    # raiden.FlatAtk = 311 + 1600
    # raiden.DefChar = 0
    # raiden.DefBonus = 0
    # raiden.FlatDmg = 0
    # raiden.DmgBonus = .32 + .2272*.25 + .466 + .3   # kazuha + emblem + goblet + raiden E
    # raiden.CR = .765
    # raiden.CD = 2.289
    # raiden.talent = 7.2144+(60*7*.01)
    # raiden.defReduction = .4
    # raiden.resistReduction = .4
    # raiden.EM = 0
    # raiden.ReactionBonus = 0
    # raiden.otherBonus = 0

    # Artifacts
    # flower = Artifact(["HP", 4780], ["ATK", 53], ["CR%", .086], ["CD%", .132], ["ER%", .065])
    # feather = Artifact(["ATK", 311], ["ATK%", .053], ["CR%", .148], ["CD%", .132], ["ER%", .104])
    # sands = Artifact(["ER%", .518], ["ATK%", .087], ["CR%", .066], ["CD%", .155], ["HP%", .105])
    # goblet = Artifact(["Electro%", .466], ["DEF", 42], ["CR%", .089], ["CD%", .148], ["ER%", .058])
    # circlet = Artifact(["CD%", .622], ["ATK%", .175], ["CR%", .105], ["ER%", .052], ["DEF", 23])

    # flower = Artifact(["HP", 4780], ["ATK", 18], ["ATK%", .093], ["CD%", .218], ["EM", 54])
    # feather = Artifact(["ATK", 311], ["DEF", 16], ["CR%", .105], ["CD%", .148], ["HP", 837])
    # sands = Artifact(["ATK%", .466], ["DEF", 39], ["CR%", .101], ["CD%", .210], ["DEF%", .058])
    # goblet = Artifact(["Cryo%", .466], ["HP", 269], ["CR%", .074], ["CD%", .117], ["ER%", .155])
    # circlet = Artifact(["CD%", .622], ["ATK%", .140], ["CR%", .035], ["ER%", .058], ["HP%", .181])

    flower = Artifact(["HP", 4780], ["CR%", .101], ["ATK%", .058], ["CD%", .187], ["EM", 21])
    feather = Artifact(["ATK", 311], ["DEF%", .066], ["EM", 37], ["CD%", .303], ["ATK%", .093])
    sands = Artifact(["EM", 187], ["DEF", 23], ["ER%", .104], ["CD%", .311], ["DEF%", .073])
    goblet = Artifact(["Pyro%", .466], ["HP%", .047], ["CR%", .07], ["CD%", .28], ["ER%", .058])
    circlet = Artifact(["CR%", .622], ["ATK%", .093], ["CD%", .202], ["HP%", .111], ["EM", 19])

    artifactList = [flower, feather, sands, goblet, circlet]

    test = Character(artifactList)
    test.AtkChar = 335
    test.FlatAtk += 925 # bennett and sara
    test.DmgBonus += .31 + .15    # serpent spine, kazuha, crimson
    test.resistReduction = 0
    test.defReduction = 0
    test.LvlChar = 90
    test.CD += .882   # Sara c6 Buff
    test.CR += 0
    test.AtkWeapon = 542        # jade spear
    test.AtkBonus += .45 + .18        # pyro res, noblesse, shimenawa
    test.talent = 2.0608        # TL8 E
    test.DefBonus += .28
    test.DefChar = 784
    #test.FlatDmg = 2673.44

    e = Enemy()
    #talent = 7.2144+(60*7*.01)


    # Combo mode forces average DMG
    comboMode = True
    if comboMode:

        # N1 E N2 E N3 E N4
        combo = [153.32, 151.04, 149.79, 156.16, 168.9, 206.08, 229.03]
        for i in range(len(combo)): combo[i] = combo[i] / 100.0

        total = 0
        for talentMultiplier in combo:
            test.talent = talentMultiplier
            total += (calc(test, e, 0) + calc(test, e, 1))/2.0

        print(f"Total average damage over combo: {total}")

    else:
        print("Non crit: ", calc(test, e, 0))
        print("On crit: ", calc(test, e, 1))
        print("Average: ", (calc(test, e, 0) + calc(test, e, 1))/2.0)



def calc(c: Character, e: Enemy, forceCrit: int):

    # general

    # ampReaction (2: forward, 1.5: reverse)
    ampReaction = 1.5 * (1 + (2.78 * c.EM) / (1400 + c.EM) + c.ReactionBonus)
    #ampReaction = 1

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

    if forceCrit == 0:
        crit = 1
    else:
        crit = 1 + c.CD

    # Defense formula
    defense = c.DefChar * (1 + c.DefBonus) + c.FlatDef

    # attack
    attack = (c.AtkChar + c.AtkWeapon) * (1 + c.AtkBonus) + c.FlatAtk

    # temporary
    c.FlatDmg = defense * .4

    # baseDamage
    baseDamage = c.talent * attack + c.FlatDmg      # attack scaling
    #baseDamage = c.talent * defense + c.FlatDmg     # defense scaling

    damage = baseDamage * (
                1 + c.DmgBonus) * crit * enemyDefMult * enemyResMult * ampReaction * c.otherBonus  # no transformative

    #print()

    return damage


if __name__ == "__main__":
    main()
