import random
card_dictionary = {
    "EXIT": "",
    "CLEAR": "",
    
    "S2" : {
        "value": 2,
        "drawing": [" _____ ", "|2    |", "|  ♠  |", "|     |", "|  ♠  |", "|____Z|"]
        },
    "S3" : {
        "value": 3,
        "drawing": [" _____ ", "|3    |", "| ♠ ♠ |", "|     |", "|  ♠  |", "|____E|"]
        },
    "S4" : {
        "value": 4,
        "drawing": [" _____ ", "|4    |", "| ♠ ♠ |", "|     |", "| ♠ ♠ |", "|____h|"]
        },
    "S5" : {
        "value": 5,
        "drawing": [" _____ ", "|5    |", "| ♠ ♠ |", "|  ♠  |", "| ♠ ♠ |", "|____S|"]
        },
    "S6" : {
        "value": 6,
        "drawing": [" _____ ", "|6    |", "| ♠ ♠ |", "| ♠ ♠ |", "| ♠ ♠ |", "|____9|"]
        },
    "S7" : {
        "value": 7,
        "drawing": [" _____ ", "|7    |", "| ♠ ♠ |", "|♠ ♠ ♠|", "| ♠ ♠ |", "|____L|"]
        },
    "S8" : {
        "value": 8,
        "drawing": [" _____ ", "|8    |", "|♠ ♠ ♠|", "| ♠ ♠ |", "|♠ ♠ ♠|", "|____8|"]
        },
    "S9" : {
        "value": 9,
        "drawing": [" _____ ", "|9    |", "|♠ ♠ ♠|", "|♠ ♠ ♠|", "|♠ ♠ ♠|", "|____6|"]
        },
    "S10" : {
        "value": 10,
        "drawing": [" _____ ", "|10 ♠ |", "|♠ ♠ ♠|", "|♠ ♠ ♠|", "|♠ ♠ ♠|", "|___0I|"]
        },
    "SJ" : {
        "value": 11,
        "drawing": [" _____ ", "|J  WW|", "|   {)|", "|(♠)% |", "| | % |", "|__/%[|"]
        },
    "SQ" : {
        "value": 12,
        "drawing": [" _____ ", "|Q  WW|", "|   {(|", "|(♠)/%|", "| |/%%|", "|_/%%O|"]
        },
    "SK" : {
        "value": 13,
        "drawing": [" _____ ", "|K  WW|", "|   {)|", "|(♠)/%|", "| |/%%|", "|_/%%>|"]
        },
    "SA" : {
        "value": 14,
        "drawing": [" _____ ", "|A .  |", r"| /.\ |", "|(_._)|", "|  |  |", "|____V|"]
        },
        
    "H2" : {
        "value": 2,
        "drawing": [" _____ ", "|2    |", "|  ♥  |", "|     |", "|  ♥  |", "|____Z|"]
        },
    "H3" : {
        "value": 3,
        "drawing": [" _____ ", "|3    |", "| ♥ ♥ |", "|     |", "|  ♥  |", "|____E|"]
        },
    "H4" : {
        "value": 4,
        "drawing": [" _____ ", "|4    |", "| ♥ ♥ |", "|     |", "| ♥ ♥ |", "|____h|"]
        },
    "H5" : {
        "value": 5,
        "drawing": [" _____ ", "|5    |", "| ♥ ♥ |", "|  ♥  |", "| ♥ ♥ |", "|____S|"]
        },
    "H6" : {
        "value": 6,
        "drawing": [" _____ ", "|6    |", "| ♥ ♥ |", "| ♥ ♥ |", "| ♥ ♥ |", "|____9|"]
        },
    "H7" : {
        "value": 7,
        "drawing": [" _____ ", "|7    |", "| ♥ ♥ |", "|♥ ♥ ♥|", "| ♥ ♥ |", "|____L|"]
        },
    "H8" : {
        "value": 8,
        "drawing": [" _____ ", "|8    |", "|♥ ♥ ♥|", "| ♥ ♥ |", "|♥ ♥ ♥|", "|____8|"]
        },
    "H9" : {
        "value": 9,
        "drawing": [" _____ ", "|9    |", "|♥ ♥ ♥|", "|♥ ♥ ♥|", "|♥ ♥ ♥|", "|____6|"]
        },
    "H10" : {
        "value": 10,
        "drawing": [" _____ ", "|10 ♥ |", "|♥ ♥ ♥|", "|♥ ♥ ♥|", "|♥ ♥ ♥|", "|___0I|"]
        },
        
    "C2" : {
        "value": 2,
        "drawing": [" _____ ", "|2    |", "|  ♣  |", "|     |", "|  ♣  |", "|____Z|"]
        },
    "C3" : {
        "value": 3,
        "drawing": [" _____ ", "|3    |", "| ♣ ♣ |", "|     |", "|  ♣  |", "|____E|"]
        },
    "C4" : {
        "value": 4,
        "drawing": [" _____ ", "|4    |", "| ♣ ♣ |", "|     |", "| ♣ ♣ |", "|____h|"]
        },
    "C5" : {
        "value": 5,
        "drawing": [" _____ ", "|5    |", "| ♣ ♣ |", "|  ♣  |", "| ♣ ♣ |", "|____S|"]
        },
    "C6" : {
        "value": 6,
        "drawing": [" _____ ", "|6    |", "| ♣ ♣ |", "| ♣ ♣ |", "| ♣ ♣ |", "|____9|"]
        },
    "C7" : {
        "value": 7,
        "drawing": [" _____ ", "|7    |", "| ♣ ♣ |", "|♣ ♣ ♣|", "| ♣ ♣ |", "|____L|"]
        },
    "C8" : {
        "value": 8,
        "drawing": [" _____ ", "|8    |", "|♣ ♣ ♣|", "| ♣ ♣ |", "|♣ ♣ ♣|", "|____8|"]
        },
    "C9" : {
        "value": 9,
        "drawing": [" _____ ", "|9    |", "|♣ ♣ ♣|", "|♣ ♣ ♣|", "|♣ ♣ ♣|", "|____6|"]
        },
    "C10" : {
        "value": 10,
        "drawing": [" _____ ", "|10 ♣ |", "|♣ ♣ ♣|", "|♣ ♣ ♣|", "|♣ ♣ ♣|", "|___0I|"]
        },
    "CJ" : {
        "value": 11,
        "drawing": [" _____ ", "|J  WW|", "|   {)|", "|(♣)% |", "| | % |", "|__/%[|"]
        },
    "CQ" : {
        "value": 12,
        "drawing": [" _____ ", "|Q  WW|", "|   {(|", "|(♣)/%|", "| |/%%|", "|_/%%O|"]
        },
    "CK" : {
        "value": 13,
        "drawing": [" _____ ", "|K  WW|", "|   {)|", "|(♣)/%|", "| |/%%|", "|_/%%>|"]
        },
    "CA" : {
        "value": 14,
        "drawing": [" _____ ", "|A _  |", "| ( ) |", "|(_'_)|", "|  |  |", "|____V|"]
        },
        
    "D2" : {
        "value": 2,
        "drawing": [" _____ ", "|2    |", "|  ♦  |", "|     |", "|  ♦  |", "|____Z|"]
        },
    "D3" : {
        "value": 3,
        "drawing": [" _____ ", "|3    |", "| ♦ ♦ |", "|     |", "|  ♦  |", "|____E|"]
        },
    "D4" : {
        "value": 4,
        "drawing": [" _____ ", "|4    |", "| ♦ ♦ |", "|     |", "| ♦ ♦ |", "|____h|"]
        },
    "D5" : {
        "value": 5,
        "drawing": [" _____ ", "|5    |", "| ♦ ♦ |", "|  ♦  |", "| ♦ ♦ |", "|____S|"]
        },
    "D6" : {
        "value": 6,
        "drawing": [" _____ ", "|6    |", "| ♦ ♦ |", "| ♦ ♦ |", "| ♦ ♦ |", "|____9|"]
        },
    "D7" : {
        "value": 7,
        "drawing": [" _____ ", "|7    |", "| ♦ ♦ |", "|♦ ♦ ♦|", "| ♦ ♦ |", "|____L|"]
        },
    "D8" : {
        "value": 8,
        "drawing": [" _____ ", "|8    |", "|♦ ♦ ♦|", "| ♦ ♦ |", "|♦ ♦ ♦|", "|____8|"]
        },
    "D9" : {
        "value": 9,
        "drawing": [" _____ ", "|9    |", "|♦ ♦ ♦|", "|♦ ♦ ♦|", "|♦ ♦ ♦|", "|____6|"]
        },
    "D10" : {
        "value": 10,
        "drawing": [" _____ ", "|10 ♦ |", "|♦ ♦ ♦|", "|♦ ♦ ♦|", "|♦ ♦ ♦|", "|___0I|"]
        }
}
deck = []
monsters = []
potions = []
weapons = []

for key in card_dictionary:
    if key != "EXIT" and key != "CLEAR":
        deck.append(key)

for item in deck:
    if "S" in item or "C" in item:
        monsters.append(item)
    if "H" in item:
        potions.append(item)
    if "D" in item:
        weapons.append(item)        

def card_drawing(scene):
    drawn_scene = []
    for i in scene:
        if len(drawn_scene) == 0:
            for value in card_dictionary[i]["drawing"]:
                drawn_scene.append(value)
        else:
            new_card = card_dictionary[i]["drawing"]
            for num in range(0,6):
                drawn_scene[num] += f" {new_card[num]}"
    for i in drawn_scene:
        print(i)

defeated_monsters = []
graveyard = []
life = 20
equipped_weapon = 0
skip_counter = 0
heal_counter = 0
print("Welcome to Scoundrel Solitaire!\n")
start_game = input("Ready to play? [YES/NO]: ")

if start_game.upper() == "NO":
    print("GOODBYE!")
    exit()
elif start_game.upper() == "YES": 
    random.shuffle (deck)
    room = deck[:4]

    #Game Loop
    while (len(deck) > 0) and (life > 0):
        for i in room:
            if i not in deck:
                continue
            deck.remove (i)
        
        #Room Loop
        while (len(room) > 1 and life > 0) or (len(room) == 1 and len(deck) == 0):
            print (f"\nDungeon: {len(deck)}")
            print (f"Life: {life}")
            card_drawing(room)
            #print (f"[{", ".join(room)}]")
            if equipped_weapon != 0: 
                if defeated_monsters:
                    print (f"Weapon: {equipped_weapon} ({', '.join(defeated_monsters)})")
                else:
                    print (f"Weapon: {equipped_weapon}")
            
            user_int = input("\n")
            
            #Skip Room [COMPLETE]
            if user_int.upper() == "SKIP":
                if len(room) < 4:
                    print ("\nSORRY! CAN'T SKIP!")
                    input("ENTER ANY KEY TO CONTINUE: ")
                    continue
                else:
                    if skip_counter != 0:
                        print ("\nCAN'T SKIP TWICE!")
                        input("ENTER ANY KEY TO CONTINUE: ")
                        continue
                    else:
                        random.shuffle (room)
                        for item in room:
                            deck.append (item)
                        room.clear()
                        skip_counter += 1
                        break
            
            if user_int.upper() == "GRAVEYARD":
                print("--GRAVEYARD 🪦--")
                card_drawing(graveyard)
                input("ENTER ANY KEY TO CONTINUE: ")
                continue
            
            if user_int.upper() == "EXIT":
                print("GOODBYE!")
                exit()
            if user_int.upper() not in room:
                print("THIS CARD IS NOT IN THE ROOM")
                input("ENTER ANY KEY TO CONTINUE: ")
                continue

            #Empty Handed Combat [COMPLETE]
            if user_int.upper() in monsters and equipped_weapon == 0:
                life -= card_dictionary[user_int.upper()]["value"]

            #Equip Weapon [COMPLETE]
            if user_int.upper() in weapons:
                if equipped_weapon != 0:
                    graveyard.append(equipped_weapon)
                    graveyard.extend(defeated_monsters)
                    defeated_monsters.clear()
                equipped_weapon = user_int.upper()
                    
            #Equipped Weapon Combat [COMPLETE]
            if user_int.upper() in monsters and equipped_weapon != 0:
                weapon_attack = input("ATTACK WITH WEAPON?: ")
                if weapon_attack.upper() == "YES":
                    if (defeated_monsters) and (card_dictionary [user_int.upper()]["value"] >= card_dictionary[defeated_monsters[-1]]["value"]):
                            print("MONSTER TOO STRONG FOR WEAPON!")
                            input("ENTER ANY KEY TO CONTINUE: ")
                            continue
                    if card_dictionary[equipped_weapon]["value"] < card_dictionary[user_int.upper()]["value"]:
                        life -= (card_dictionary[user_int.upper()]["value"] - card_dictionary[equipped_weapon]["value"])
                    defeated_monsters.append (user_int.upper())
                elif weapon_attack.upper() == "NO":
                    life -= card_dictionary[user_int.upper()]["value"]
                else:
                    continue

            #Healing [COMPLETE]
            if user_int.upper() in potions:
                if heal_counter != 0:
                    print("\nCAN'T HEAL TWICE! POTION WILL BE DISCARTED!")
                    heal_warning = input("CONTINUE?: ")
                    if heal_warning.upper() != "YES":
                        continue
                else:
                    life = life + card_dictionary[user_int.upper()]["value"]    
                    heal_counter += 1
                    if life > 20:
                        print("\nMAX LIFE REACHED! POTION WILL BE DISCARTED!")
                        heal_warning = input("CONTINUE?: ")
                        if heal_warning.upper() != "YES":
                            continue
                        life = 20 
            
            room.remove (user_int.upper())
            if ((user_int.upper() not in weapons) and (user_int.upper() not in defeated_monsters)):
                graveyard.append (user_int.upper())
            #Reset skip and heal counters after clearing the room
            if len(room) <= 1:
                skip_counter = 0
                heal_counter = 0
        
        if user_int.upper() == "SKIP":
            room.extend (deck[:4])
        else:
            room.extend (deck[:3])

        #Endgame Prints
        if life <= 0:
            print (f"Life: {life}")
            print ("\nYOU DIED ☠️")
        if len(deck) <= 0:
            print (f"Dungeon: {len(deck)}")
            print (f"[{", ".join(room)}]")
            print (f"Life: {life}")
            if equipped_weapon != 0: 
            
                if defeated_monsters:
                    print (f"Weapon: {equipped_weapon} ({', '.join(defeated_monsters)})")
                else:
                    print (f"Weapon: {equipped_weapon}")
            print ("\nYOU HAVE ESCAPED THE DUNGEON! 🙌")
