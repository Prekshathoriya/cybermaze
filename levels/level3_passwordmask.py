def level3():
    print("\n🔐 LEVEL 3: Password Masking Challenge")
    print("Hackers often disguise passwords with symbols.")
    print("Your mission: Decode the real password from this clue.")
    print("Clue: P@$$w0rd")
    print("Hint: Replace symbols with letters. You have 3 tries. Type 'quit' to exit.\n")

    correct_answer = "password"
    attempts = 3

    while attempts > 0:
        user_input = input("Enter decoded password: ").strip().lower()

        if user_input == "quit":
            print("\n👋 Exiting Level 3.")
            return False

        if user_input == correct_answer:
            print("\n✅ Well done! You’ve unm@sked the password.\n")
            return True
        else:
            attempts -= 1
            print(f"❌ Incorrect. Attempts left: {attempts}")

    print("\n💀 Challenge failed. The masked password remains a mystery.\n")
    return False
