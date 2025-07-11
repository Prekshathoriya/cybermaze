from levels import level1_bruteforce, level2_decryption, level3_passwordmask
from utils.helpers import save_score, show_leaderboard

def welcome():
    print("\n🧠 Welcome to CyberMaze!")
    print("You are an ethical hacker solving puzzles to test your skills.")
    print("Good luck, Agent.\n")

def start_game():
    score = 0

    if level1_bruteforce.level1():
        print("🎉 You passed Level 1!")
        score += 10

        if level2_decryption.level2():
            print("🎉 You passed Level 2!")
            score += 15

            if level3_passwordmask.level3():
                print("🏆 Congratulations, you completed CyberMaze!")
                score += 25
            else:
                print("💡 Come back for Level 3.")
        else:
            print("💡 Come back for Level 2.")
    else:
        print("💡 Come back for Level 1.")

    print(f"\n🧮 Final Score: {score} points")

    name = input("Enter your name for the leaderboard: ")
    save_score(name, score)
    show_leaderboard()

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Start Game")
        print("2. Quit")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == '1':
            start_game()
        elif choice == '2' or choice.lower() == 'quit':
            print("👋 Goodbye, Agent.")
            break
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    welcome()
    main_menu()
