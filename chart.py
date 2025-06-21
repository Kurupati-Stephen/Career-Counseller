import matplotlib.pyplot as plt

def plot_scores(scores):
    traits = list(scores.keys())
    values = list(scores.values())

    plt.figure(figsize=(8, 5))
    bars = plt.bar(traits, values, color="skyblue")
    plt.ylim(0, 5)
    plt.title("Your Strength Profile")
    plt.xlabel("Traits")
    plt.ylabel("Score (1–5)")

    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width()/2, value + 0.1, str(value),
                 ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.show()
