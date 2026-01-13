# story generator function
def generate_story(name, place, noun, verb, adjective):
    print(f"""
Once upon a time, there was a person named {name} who lived in {place}.
They were very {adjective} and loved {noun}.
One day, they decided to {verb}, and it turned into an unforgettable adventure!
""")


def main():
    print("--------- Mad Lib Story Generator ----------")

    while True:
        print("-" * 40)

        name = input("Name: ")
        place = input("Place: ")
        noun = input("Noun: ")
        adjective = input("Adjective: ")
        verb = input("Verb: ")

        if all([name, place, noun, adjective, verb]):
            generate_story(name, place, noun, verb, adjective)
        else:
            print("❌ Please fill all words!")
            continue

        again = input("\nMake another story? (yes/no): ").lower()
        if again == "no":
            print("👋 Goodbye, storyteller!")
            break


if __name__ == "__main__":
    main()
