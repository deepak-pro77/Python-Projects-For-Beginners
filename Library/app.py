#################################################

# Books in Library
library_books = [
    # Fiction & Novels
    "Harry Potter and the Philosopher's Stone",
    "Harry Potter and the Chamber of Secrets",
    "The Hobbit",
    "The Lord of the Rings",
    "The Alchemist",
    "To Kill a Mockingbird",
    "1984",
    "Animal Farm",
    "The Great Gatsby",
    "Pride and Prejudice",
    "The Catcher in the Rye",
    "Life of Pi",

    # Self-Help & Motivation
    "Atomic Habits",
    "Rich Dad Poor Dad",
    "Think and Grow Rich",
    "The Power of Now",
    "The 7 Habits of Highly Effective People",
    "How to Win Friends and Influence People",
    "The Subtle Art of Not Giving a F*ck",

    # Education & Study
    "Physics for Class 10",
    "Chemistry for Class 10",
    "Biology for Class 10",
    "Mathematics for Class 10",
    "Advanced Mathematics",
    "English Grammar in Use",
    "Oxford Dictionary",

    # Computer & Programming
    "Python Crash Course",
    "Automate the Boring Stuff with Python",
    "Learning Python",
    "Clean Code",
    "Introduction to Algorithms",
    "Data Structures and Algorithms in Python",
    "Computer Networking Basics",

    # History & Biography
    "Wings of Fire",
    "The Diary of a Young Girl",
    "Long Walk to Freedom",
    "Steve Jobs Biography",
    "Elon Musk",
    "A Brief History of Time",

    # Religious / Spiritual
    "Bhagavad Gita",
    "Guru Granth Sahib",
    "The Holy Quran",
    "The Bible",
    "The Dhammapada"
]


library_book_summaries = {

    # Fiction & Novels
    "Harry Potter and the Philosopher's Stone": "A young boy discovers he is a wizard and begins his magical journey at Hogwarts.",
    "Harry Potter and the Chamber of Secrets": "Harry uncovers a dark secret hidden within Hogwarts that threatens students.",
    "The Hobbit": "A simple hobbit is pulled into an epic adventure to reclaim a lost kingdom.",
    "The Lord of the Rings": "A quest to destroy a powerful ring and save Middle-earth from evil.",
    "The Alchemist": "A shepherd follows his dream and learns about destiny and self-belief.",
    "To Kill a Mockingbird": "A story about justice, racism, and moral growth in a small town.",
    "1984": "A dystopian novel about a society under constant surveillance and control.",
    "Animal Farm": "An allegorical tale showing how power can corrupt ideals.",
    "The Great Gatsby": "A tragic story of love, wealth, and the American Dream.",
    "Pride and Prejudice": "A romantic novel about manners, marriage, and misunderstandings.",
    "The Catcher in the Rye": "A teenager’s journey through alienation and self-identity.",
    "Life of Pi": "A survival story exploring faith and the power of storytelling.",

    # Self-Help & Motivation
    "Atomic Habits": "A practical guide to building good habits through small daily changes.",
    "Rich Dad Poor Dad": "Teaches financial literacy and mindset through contrasting life lessons.",
    "Think and Grow Rich": "Focuses on mindset and persistence to achieve success.",
    "The Power of Now": "Encourages living fully in the present moment.",
    "The 7 Habits of Highly Effective People": "A framework for personal and professional effectiveness.",
    "How to Win Friends and Influence People": "Teaches communication and relationship-building skills.",
    "The Subtle Art of Not Giving a F*ck": "Promotes focusing on what truly matters in life.",

    # Education & Study
    "Physics for Class 10": "Introduces basic physics concepts for secondary students.",
    "Chemistry for Class 10": "Covers foundational chemical principles and reactions.",
    "Biology for Class 10": "Explains life processes and biological systems.",
    "Mathematics for Class 10": "Builds core mathematical concepts and problem-solving skills.",
    "Advanced Mathematics": "Explores higher-level mathematical theories and applications.",
    "English Grammar in Use": "A comprehensive guide to English grammar rules.",
    "Oxford Dictionary": "Provides definitions and meanings of English words.",

    # Computer & Programming
    "Python Crash Course": "A beginner-friendly introduction to Python programming.",
    "Automate the Boring Stuff with Python": "Shows how to automate everyday tasks using Python.",
    "Learning Python": "A detailed guide to Python fundamentals and concepts.",
    "Clean Code": "Teaches how to write readable and maintainable software.",
    "Introduction to Algorithms": "Explains core algorithms and computational theory.",
    "Data Structures and Algorithms in Python": "Covers efficient data handling using Python.",
    "Computer Networking Basics": "Introduces how computer networks and the internet work.",

    # History & Biography
    "Wings of Fire": "The inspiring autobiography of Dr. A. P. J. Abdul Kalam.",
    "The Diary of a Young Girl": "A young girl’s diary during the Holocaust.",
    "Long Walk to Freedom": "Nelson Mandela’s journey against apartheid.",
    "Steve Jobs Biography": "The life and innovation of Apple’s co-founder.",
    "Elon Musk": "A biography of the entrepreneur behind Tesla and SpaceX.",
    "A Brief History of Time": "Explains complex ideas about the universe and time.",

    # Religious / Spiritual
    "Bhagavad Gita": "A spiritual dialogue on duty, life, and devotion.",
    "Guru Granth Sahib": "The central religious scripture of Sikhism.",
    "The Holy Quran": "The Islamic holy book containing divine guidance.",
    "The Bible": "Sacred scriptures of Christianity.",
    "The Dhammapada": "Sayings of Buddha focused on wisdom and ethics."
}


def read_book():

    print("\n📚WELCOME TO THE LIBRARY")

    while True:

        print("\nEnter the book you want the ONE-LINE Summary OF 🧐:")

        book = input("\n📙Book: ").strip()

        matches = {b.lower(): b for b in library_books}

        if book.lower() in matches:
            real_name = matches[book.lower()]

        if real_name in library_books:
            print(f"✨Book Exits: ({real_name})")
            print("\nHere's The (ONE-LINE) Summary")
            print(f"\nSummary: {library_book_summaries[real_name]}")

            export = input("\nWant to Export the Summary to File (yes/no): ")
            if export == "yes":
                print(f"✅Exported to (Summary.txt)")
                export_file(real_name, library_book_summaries[real_name])

            ask = input("\nWant to Check More (yes/no)? ")
            if ask == "yes":
                continue
            else:
                print("👋 GoodBye")

                break
        else:
            print("❌ Book Does Not Exist in the Library")
            continue


def export_file(book, booksummary):

    filename = "Summary.txt"

    with open(filename, "a") as f:
        f.write(f"{book} - {booksummary}\n")


read_book()
