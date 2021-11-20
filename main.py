import math
import random

class Artifact:

    #mainStat = list()
    #subStat = list()

    def __init__(self, a, b, c, d, e):
        self.mainStat = []
        self.subStat = []

        self.mainStat = a
        self.subStat.append(b)
        self.subStat.append(c)
        self.subStat.append(d)
        self.subStat.append(e)

class Character:

    AtkChar = 0         # ATK stats
    AtkWeapon = 0
    AtkBonus = 0
    FlatAtk = 0
    DefChar = 0         # DEF stats
    DefBonus = 0
    FlatDmg = 0         # DMG stats
    DmgBonus = 0
    CR = .05            # Crit stats
    CD = .50
    LvlChar = 0         # LEVEL
    EM = 0              # EM
    ReactionBonus = 0   # Reaction bonuses (like CW)
    defReduction = 0        # Def reduction (Klee C2)
    resistReduction = .0    # Resist reduction (VV)
    otherBonus = 1          # 1.5 if Evilsoother is active
    ER = 0                  # ER

    def __init__(self, artifacts: list[Artifact], weaponAtk: int):

        self.AtkWeapon = weaponAtk
        elementalGoblets = ["Electro%", "Pyro%", "Physical%", "Hydro%", "Cryo%", "Geo%"]

        for item in artifacts:          # only damage stats currently
            if item.mainStat[0] == "ATK":
                self.FlatAtk += item.mainStat[1]
            if item.mainStat[0] == "ATK%":
                self.AtkBonus += item.mainStat[1]
            if elementalGoblets.count(item.mainStat[0]) > 0:
                self.DmgBonus += item.mainStat[1]
            if item.mainStat[0] == "CR%":
                self.CR += item.mainStat[1]
            if item.mainStat[0] == "CD%":
                self.CD += item.mainStat[1]
            if item.mainStat[0] == "ER%":
                self.ER += item.mainStat[1]
            for subs in item.subStat:
                if subs[0] == "ATK":
                    self.FlatAtk += subs[1]
                if subs[0] == "ATK%":
                    self.AtkBonus += subs[1]
                if subs[0] == "CR%":
                    self.CR += subs[1]
                if subs[0] == "CD%":
                    self.CD += subs[1]
                if subs[0] == "EM":
                    self.EM += subs[1]
                if subs[0] == "ER%":
                    self.ER += subs[1]



class Enemy:

    lvl = 100
    baseResist = .1

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
    flower = Artifact(["HP", 4780], ["ATK", 53], ["CR%", .086], ["CD%", .132], ["ER%", .065])
    feather = Artifact(["ATK", 311], ["ATK%", .053], ["CR%", .148], ["CD%", .132], ["ER%", .104])
    sands = Artifact(["ER%", .518], ["ATK%", .087], ["CR%", .066], ["CD%", .155], ["HP%", .105])
    goblet = Artifact(["Electro%", .466], ["DEF", 42], ["CR%", .089], ["CD%", .148], ["ER%", .058])
    circlet = Artifact(["CD%", .622], ["ATK%", .175], ["CR%", .105], ["ER%", .052], ["DEF", 23])

    artifactList = [flower, feather, sands, goblet, circlet]

    test = Character(artifactList, 674)
    test.FlatAtk = 337
    test.FlatAtk += 1600 # bennett and sara
    test.DmgBonus += .32 + .3 + .2272*.25 # kazuha + raiden E + emblem
    test.resistReduction = .4
    test.defReduction = .4
    test.LvlChar = 90
    test.CD += .6   # Sara c6 Buff
    test.CR += .221
    test.AtkWeapon = 674        # jade spear
    test.AtkBonus += .2

    e = Enemy()
    talent = 7.2144+(60*7*.01)

    runCount = 100
    dmgArr = []
    for i in range(runCount):
        d = calc(test,e,talent)
        dmgArr.append(d)
        print(d)

    print(f"\nAverage DMG over {runCount} runs: {sum(dmgArr)/runCount}")


def calc(c: Character, e: Enemy, talent: float):

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
    baseDamage = talent * attack + c.FlatDmg

    damage = baseDamage * (
                1 + c.DmgBonus) * crit * enemyDefMult * enemyResMult * ampReaction * c.otherBonus  # no transformative

    return damage




if __name__ == "__main__":
    main()
