import random

def word_guess_game():
    slots = [
        [("P_t", ['Pit', 'Pot', 'Put', 'Pet'], 'Pot'), ("R_t", ['Rit', 'Rot', 'Rut', 'Ret'], 'Rot'), ("S_t", ['Sit', 'Sot', 'Sut', 'Set'], 'Sit')],
        [("T_t", ['Tit', 'Tot', 'Tut', 'Tet'], 'Tot'), ("W_t", ['Wit', 'Wot', 'Wut', 'Wet'], 'Wit'), ("B_d", ['Bid', 'Bod', 'Bud', 'Bed'], 'Bed')],
        [("D_d", ['Did', 'Dod', 'Dud', 'Ded'], 'Did'), ("F_d", ['Fid', 'Fod', 'Fud', 'Fed'], 'Fed'), ("H_d", ['Hid', 'Hod', 'Hud', 'Hed'], 'Hid')],
        [("J_d", ['Jid', 'Jod', 'Jud', 'Jed'], 'Jed'), ("L_d", ['Lid', 'Lod', 'Lud', 'Led'], 'Led'), ("M_d", ['Mid', 'Mod', 'Mud', 'Med'], 'Mud')],
        [("P_d", ['Pid', 'Pod', 'Pud', 'Ped'], 'Pod'), ("R_d", ['Rid', 'Rod', 'Rud', 'Red'], 'Red'), ("S_d", ['Sid', 'Sod', 'Sud', 'Sed'], 'Sid')]
    ]
    stacks = 0
    attempts = 5
    random.shuffle(slots)  # Randomize the order of slots
    
    for slot in slots:
        print("\nNew Slot:")
        random.shuffle(slot)  # Randomize the words within the slot
        
        for word, options, correct in slot:
            correct_option = correct[-2].lower()  # Extracting the missing letter
            print(f"Fill in the missing letters: {word}")
            print("Options:", ', '.join(options))
            
            answer = input("Enter your choice (only the missing letter): ").strip().lower()
            
            if answer == correct_option:
                print("Correct! You earned a stack.")
                stacks += 1
                print(f"Total stacks: {stacks}")
            else:
                attempts -= 1
                print(f"Wrong! The correct answer was '{correct_option}'.")
                print(f"You have {attempts} attempts left.")
                if attempts == 0:
                    print("Game Over! You have used all attempts.")
                    return
                break  # Move to the next slot after a wrong answer
        
        if stacks >= 3:
            print("You have earned 3 stacks! Congratulations! You win!")
            return
    
    print("Game Over! You could not collect 3 stacks.")

# Start the game
word_guess_game()
