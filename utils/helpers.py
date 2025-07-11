def save_score(name, score):
    with open("leaderboard.txt", "a") as f:
        f.write(f"{name}:{score}\n")

def show_leaderboard():
    print("\n🏆 Leaderboard:")
    try:
        with open("leaderboard.txt", "r") as f:
            scores = [line.strip().split(":") for line in f if ":" in line]
            scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)[:5]
            for i, (name, score) in enumerate(scores, start=1):
                print(f"{i}. {name} - {score} pts")
    except FileNotFoundError:
        print("No leaderboard data yet.")
