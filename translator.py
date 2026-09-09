translations = {
    "hello": "こんにちは",
    "good morning": "おはようございます",
    "thank you": "ありがとう",
    "school": "学校",
    "student": "学生",
    "teacher": "先生",
    "friend": "友達",
    "cat": "猫",
    "dog": "犬"
}

japanese_translations = {
    value: key for key, value in translations.items()
}

while True:
    print("\n1. English → Japanese")
    print("2. Japanese → English")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        word = input("Enter English word: ").lower()

        if word in translations:
            print("Japanese:", translations[word])
        else:
            print("Sorry, I don't know that word.")

    elif choice == "2":
        word = input("Enter Japanese word: ")

        if word in japanese_translations:
            print("English:", japanese_translations[word])
        else:
            print("Sorry, I don't know that word.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Please choose 1, 2, or 3.")
