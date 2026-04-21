
# counter.py file theke Counter import korteche
from Counter import Counter

def main():
    print("Program starting.")
    print("Initializing counter...")

    # Counter class er object banacche
    counter = Counter()

    print("Counter initialized.")

    # infinite loop er maddhome option dekhabe
    while True:
        print("\nOptions:")
        print("1) Add count")
        print("2) Get count")
        print("3) Zero count")
        print("0) Exit program")

        # user choice
        choice = input("Choice: ")

        if choice == "1":
            # increase count
            counter.addCount()
            print("Count increased")

        elif choice == "2":
            # current count dekhacche
            print(f"Current count '{counter.getCount()}'")

        elif choice == "3":
            # count zero kore dicche
            counter.zeroCount()
            print("Count zeroed")

        elif choice == "0":
            # program closed
            print("Program ending.")
            break

        else:
            # for wrong option
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
