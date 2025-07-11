def level1():
    print("\n🔐 LEVEL 1: Brute Force Simulation")
    print("Mission: Guess the 3-digit admin PIN to unlock the system.")
    print("You have 5 attempts.")
    print("Hint: It’s a number between 400 and 450.\n")
    print("Type 'quit' anytime to exit this level.\n")

    secret_pin = "431"
    attempts = 5

    while attempts > 0:
        guess = input("Enter 3-digit PIN: ").strip()

        if guess.lower() == 'quit':
            print("\n👋 Exiting Level 1. See you next time!")
            return False

        if guess == secret_pin:
            print("\n✅ Access Granted! You've cracked the system.\n")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"❌ Incorrect. Attempts left: {attempts}")
            else:
                print("\n💀 Mission Failed. System locked down.\n")
                return False
