import random

Tie_counter = 0


def eyes():
    print(
        "A very powerful item; capable of turning your foes into stone. It shall only be used when it's energy is synced with the soul of its wielder.")


def watch():
    print(
        "A magnificent piece, stylish enough so it can be worn with any outfit. It gives its wielder 10 minutes to have the time stopped for. Very powerful if used wisely")


def robe():
    print(
        "Although it can be wrongfully thought of as 'out of style', but in spite of its archaic appearance, this robe is able to render its wielder invisible to the naked eye. Careful, the user is still tangible...")


def necklace():
    print(
        "A necklace that stores in its center socket an armonium core stone. It grants its user unbalanced luck. That means that it should be fixed in the next patch; it won't be")


def staff():
    print(
        "At the very end of the staff stands the eye of Necron. It grants it user the ability to fly above all, as the user progresses, the staff does too. Ultimately, the user is granted the ultimate ability of Necron; the ability to fly.")


def prize():
    print(
        "Master's Slave:\n-Well, Slayer, you have rightfully beaten 'The Master'. What reward shall you choose from our stash?")
    print("""
    1. { Agamemnon Eyes }
    2. { Blissful Watch }
    3. { Nefertiti's Robe }
    4. { Traveller's Necklace of Impure Luck }
    5. { Necromancer's Staff }
        """)


def game(component, master_choice):
    if (component.lower() == 'scissors' and master_choice.lower() == 'rock') or (
            component.lower() == 'rock' and master_choice.lower() == 'paper') or (
            component.lower() == 'paper' and master_choice.lower() == 'scissors'):
        return 'Lose'
    elif (component.lower() == 'scissors' and master_choice.lower() == 'paper') or (
            component.lower() == 'paper' and master_choice.lower() == 'rock') or (
            component.lower() == 'rock' and master_choice.lower() == 'scissors'):
        return 'Win'
    elif Component.lower() == master_pick.lower():
        return 'Tie'


def game2(component2, master_choice2):
    if (component2.lower() == 'scissors' and master_choice2.lower() == 'rock') or (
            component2.lower() == 'rock' and master_choice2.lower() == 'paper') or (
            component2.lower() == 'paper' and master_choice2.lower() == 'scissors'):
        return 'Lose'
    elif (component2.lower() == 'scissors' and master_choice2.lower() == 'paper') or (
            component2.lower() == 'paper' and master_choice2.lower() == 'rock') or (
            component2.lower() == 'rock' and master_choice2.lower() == 'scissors'):
        return 'Win'
    elif Component.lower() == master_pick.lower():
        return 'Tie'


Game_Component = ["Rock", "Paper", "Scissors"]
Answer = input("Welcome, stranger! This is a game of Rock, Paper, Scissors on the bet of death. Are you willing to play?\nYour answer: ")
negative_answer = ['No', 'Nope', 'Maybe sometime else', 'Let me be', 'exit', 'bye', 'next time', 'no', 'nope']
for n_answer in negative_answer:
    if n_answer in Answer:
        print("Begone then, puny mortal! You shall not waste more of my time!")
        break
    else:
        master_pick = random.choice(Game_Component)
        Component = input("Great then! You shall amuse me today, mortal! Make your pick!\nYour pick: ")
        if game(Component, master_pick) == 'Win':
            print("How could this be? How could a ... mortal ... beat me?!\nFine, mortal, choose the prize you want.\n")
            print(f"Master's choice was {master_pick}")
            prize()
            chosen_prize = int(input("So, what shall it be? Choose the number adjacent to your choice.\n"))
            if chosen_prize not in range(1, 5):
                while chosen_prize not in range(1, 5):
                    chosen_prize = input("That is not a valid answer! Choose a number in range 1 - 5!\nYour choice: ")
            elif chosen_prize == 1:
                print("So your choice was 'Agamemnon Eyes'. Here you have information about this item:\n")
                eyes()
            elif chosen_prize == 2:
                print("So your choice was 'Blissful Watch'. Here you have information about this item:\n")
                watch()
            elif chosen_prize == 3:
                print("So your choice was 'Nefertiti's Robe'. Here you have information about this item:\n")
                robe()
            elif chosen_prize == 4:
                print(
                    "So your choice was 'Traveller's Necklace of Impure Luck'. Here you have information about this item:\n")
                necklace()
            elif chosen_prize == 5:
                print("So your choice was 'Necromancer's Staff'. Here you have information about this item:\n")
                staff()
            break
        elif game(Component, master_pick) == 'Tie':
            master_pick2 = random.choice(Game_Component)
            component2 = input(
                "What were the chances? It is a ... tie! You just prolonged your life by a insignificant margin! Let's choose again!\nYour choice: ")
            if game2(component2, master_pick2) == 'Win':
                print(
                    "How could this be? How could a ... mortal ... beat me?!\nFine, mortal, choose the prize you want.\n")
                print(f"Master's choice was {master_pick2}")
                prize()
                chosen_prize = int(input("So, what shall it be? Choose the number adjacent to your choice.\n"))
                if chosen_prize not in range(1, 5):
                    while chosen_prize not in range(1, 5):
                        chosen_prize = int(input("That is not a valid answer! Choose a number in range 1 - 5!\nYour choice: "))
                elif chosen_prize == 1:
                    print("So your choice was 'Agamemnon Eyes'. Here you have information about this item:\n")
                    eyes()
                elif chosen_prize == 2:
                    print("So your choice was 'Blissful Watch'. Here you have information about this item:\n")
                    watch()
                elif chosen_prize == 3:
                    print("So your choice was 'Nefertiti's Robe'. Here you have information about this item:\n")
                    robe()
                elif chosen_prize == 4:
                    print(
                        "So your choice was 'Traveller's Necklace of Impure Luck'. Here you have information about this item:\n")
                    necklace()
                elif chosen_prize == 5:
                    print("So your choice was 'Necromancer's Staff'. Here you have information about this item:\n")
                    staff()
                break
            elif game2(component2, master_pick2) == 'Tie':
                Tie_counter += 1
                master_pick2 = random.choice(Game_Component)
                component2 = input(
                    "What were the chances? It is a ... tie! You just prolonged your life by a insignificant margin! Let's choose again!\nYour choice: ")
                if game2(component2, master_pick2) == 'Win':
                    print(
                        "How could this be? How could a ... mortal ... beat me?!\nFine, mortal, choose the prize you want.\n")
                    print(f"Master's choice was {master_pick2}")
                    prize()
                    chosen_prize = int(input("So, what shall it be? Choose the number adjacent to your choice.\n"))
                    if chosen_prize not in range(1, 5):
                        while chosen_prize not in range(1, 5):
                            chosen_prize = int(
                                input("That is not a valid answer! Choose a number in range 1 - 5!\nYour choice: "))
                    elif chosen_prize == 1:
                        print("So your choice was 'Agamemnon Eyes'. Here you have information about this item:\n")
                        eyes()
                    elif chosen_prize == 2:
                        print("So your choice was 'Blissful Watch'. Here you have information about this item:\n")
                        watch()
                    elif chosen_prize == 3:
                        print("So your choice was 'Nefertiti's Robe'. Here you have information about this item:\n")
                        robe()
                    elif chosen_prize == 4:
                        print(
                            "So your choice was 'Traveller's Necklace of Impure Luck'. Here you have information about this item:\n")
                        necklace()
                    elif chosen_prize == 5:
                        print("So your choice was 'Necromancer's Staff'. Here you have information about this item:\n")
                        staff()
                    break
                elif game2(component2, master_pick2) == 'Tie':
                    Tie_counter += 1
                    master_pick2 = random.choice(Game_Component)
                    component2 = input(
                        "What were the chances? It is a ... tie! You just prolonged your life by a insignificant margin! Let's choose again!\nYour choice: ")
                    if game2(component2, master_pick2) == 'Win':
                        print(
                            "How could this be? How could a ... mortal ... beat me?!\nFine, mortal, choose the prize you want.\n")
                        print(f"Master's choice was {master_pick2}")
                        prize()
                        chosen_prize = int(input("So, what shall it be? Choose the number adjacent to your choice.\n"))
                        if chosen_prize not in range(1, 5):
                            while chosen_prize not in range(1, 5):
                                chosen_prize = int(input("That is not a valid answer! Choose a number in range 1 - 5!\nYour choice: "))
                        elif chosen_prize == 1:
                            print("So your choice was 'Agamemnon Eyes'. Here you have information about this item:\n")
                            eyes()
                        elif chosen_prize == 2:
                            print("So your choice was 'Blissful Watch'. Here you have information about this item:\n")
                            watch()
                        elif chosen_prize == 3:
                            print("So your choice was 'Nefertiti's Robe'. Here you have information about this item:\n")
                            robe()
                        elif chosen_prize == 4:
                            print("So your choice was 'Traveller's Necklace of Impure Luck'. Here you have information about this item:\n")
                            necklace()
                        elif chosen_prize == 5:
                            print("So your choice was 'Necromancer's Staff'. Here you have information about this item:\n")
                            staff()
                        break
                    elif game2(component2, master_pick2) == 'Tie':
                        print(
                            "What were the chances? It is a ... tie! You just prolonged your life by a insignificant margin! Let's choose again!\nYour pick: ")
                    else:
                        print("Ha ha! Puny mortal! You've lost! How could you think you could beat me?\n")
                        print(f"Master's choice was {master_pick2}\n")
                    if Tie_counter >= 2:
                        print("And so was that 'The master' and the slayer have fought 'till the end of time...")
                        break
                else:
                    print("Ha ha! Puny mortal! You've lost! How could you think you could beat me?\n")
                    print(f"Master's choice was {master_pick2}\n")
            else:
                print("Ha ha! Puny mortal! You've lost! How could you think you could beat me?\n")
                print(f"Master's choice was {master_pick2}\n")
        else:
            print("Ha ha! Puny mortal! You've lost! How could you think you could beat me?\n")
            print(f"Master's choice was {master_pick}\n")
            break