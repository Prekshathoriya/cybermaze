def level2():
    print("\n🔐 LEVEL 2: Cipher Decryption Puzzle")
    print("A secret message is encrypted with a Caesar cipher (shift 3).")
    print("Your mission: Decrypt it to reveal the message.")
    print("Hint: 'Khoor Zruog!' is encrypted. Type 'quit' to skip.\n")

    correct = "hello world"
    attempts = 3

    while attempts > 0:
        user_input = input("Enter decrypted message: ").strip().lower()

        if user_input == "quit":
            print("\n👋 Exiting Level 2.")
            return False

        if user_input == correct:
            print("\n✅ Correct! You've decrypted the message.\n")
            return True
        else:
            attempts -= 1
            print(f"❌ Incorrect. Attempts left: {attempts}")

    print("\n💀 Decryption failed. Try again later.\n")
    return False
