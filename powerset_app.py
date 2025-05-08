from itertools import chain, combinations

def get_user_set():
    print("Enter elements of the set separated by commas (e.g., a,b,c):")
    user_input = input("Set: ")
    elements = [item.strip() for item in user_input.split(",") if item.strip()]
    return elements

def generate_powerset(s):
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

def display_powerset(powerset):
    print("\n--- Power Set ---")
    for subset in powerset:
        print(set(subset))

def main():
    print("Welcome to the Power Set Generator!")
    user_set = get_user_set()

    if not user_set:
        print("Empty set provided. The power set is: {{}}")
        return

    powerset = generate_powerset(user_set)
    display_powerset(powerset)
    print(f"\nTotal subsets: {len(powerset)}")

if __name__ == "__main__":
    main()
