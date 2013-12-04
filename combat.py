#!/usr/bin/python
import sys
import dice
import equip
playerdex = equip.dex("jon.ini")
enemydex = equip.dex("goblin.ini")
if (playerdex >= enemydex):
	t1 = "jon.ini"
	t2 = "goblin.ini"
else:
	t1 = "goblin.ini"
	t2 = "jon.ini"

# Names of our heros
t1name = equip.name(t1)
t2name = equip.name(t2)
#What is each combatants health
t1health = int(equip.health(t1))
t2health = int(equip.health(t2))
#What weapons are they holding
t1weapon = equip.weapon(t1)
t2weapon = equip.weapon(t2)
#Which combatant goes first

while (t1health > 0 ) and (t2health > 0 ):
	#####Turn 1#####
        attack = dice.attackroll()
        print "%s attacks %s with %s" % (t1name, t2name, t1weapon)
        print "%s rolls a %s" % (t1name,attack)
        if (attack == 1):
                print "%s swings wildly and cuts off his left hand" % (t1name)
                damage = 0
        elif (attack == 20):
		damage = 6
		print "%s lands a devastating blow" % (t1name)
	elif ( attack >= 10):
                damage = dice.damageroll()
                print "%s cuts %s for %s" % (t1name,t2name,damage)
	else:
		print "%s dodges the attack" % (t2name)
		damage = 0
        int(damage)
        t2health = t2health - damage
        if (attack == 0):
                print "%s laughs at %s's misfortune" % (t2name, t1name)
        elif (damage >= 1) and (t2health > 0):
                print "%s was hurt" % (t2name)
	elif (t2health <= 0):
		print "%s is dead" % (t2name)
		sys.exit()
	#####Turn 2#####
        attack = dice.attackroll()
        print "%s attacks %s with %s" % (t2name, t1name, t2weapon)
        print "%s rolls a %s" % (t2name,attack)
        if (attack == 1):
                print "%s swings wildly and cuts off his left hand" % (t2name)
                damage = 0
        elif (attack == 20):
                damage = 6
                print "%s lands a devastating blow" % (t2name)
        elif ( attack >= 10):
                damage = dice.damageroll()
                print "%s cuts %s for %s" % (t2name,t1name,damage)
        else:
                print "%s dodges the attack" % (t1name)
                damage = 0
        int(damage)
        t1health = t1health - damage
        if (attack == 1):
                print "%s laughs at %s's misfortune" % (t1name, t2name)
        elif (damage >= 1) and (t1health > 0):
                print "%s was hurt" % (t1name)
        elif (t1health <= 0):
                print "%s is dead" % (t1name)
