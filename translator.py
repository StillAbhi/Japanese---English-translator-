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

word = input("Enter an English word: ").lower()

if word in translations:
    print("Japanese:", translations[word])
else:
    print("Sorry, I don't know that word yet.")
