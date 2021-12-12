from artifact import Artifact

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
    FlatDef = 0

    talent = 0              # talent value

    def __init__(self, artifacts: list[Artifact]):

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
            if item.mainStat[0] == "EM":
                self.EM += item.mainStat[1]
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
                if subs[0] == "DEF%":
                    self.DefBonus += subs[1]
                if subs[0] == "DEF":
                    self.FlatDef += subs[1]