from classes.game import Person, bcolors


magic = [{'name': 'Fire', 'cost': 10, 'dmg': 60},
         {'name': 'Thunder', 'cost': 10, 'dmg': 124},
         {'name': 'Blizzard', 'cost': 10, 'dmg': 100}]

player = Person(80, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 1

#print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    print("===============================================================")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for " + str(dmg) + " DMG points")
        print("Your enemy has " + str(enemy.get_hp()) + " HP left")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose your magic spell: ")) - 1
        spell = player.get_spell_name(magic_choice)
        magic_dmg = player.generate_spell_damage(magic_choice)
        print(spell)
        cost = player.get_spell_mp_cost(magic_choice)
        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + "\nYou have been running out of mana !\n")
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell + " deals ", str(magic_dmg), " points of damage" + bcolors.ENDC)


        enemy.take_damage(magic_dmg)
        print("You attacked for " + str(magic_dmg) + " DMG points")

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print ("--------------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC + "\n")
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")


    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You have been defeated by the enemy" + bcolors.ENDC)
        running = False
