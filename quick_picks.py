import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_PICKS = 6

def generate_quick_pick():
    return sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUM_PICKS))

def display_quick_picks(num_quick_picks):
    for _ in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2d}" for num in quick_pick))

def main():
    num_quick_picks = int(input("How many quick picks? "))
    display_quick_picks(num_quick_picks)

if __name__ == "__main__":
    main()
