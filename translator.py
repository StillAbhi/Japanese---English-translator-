translations = {
    "hello": "こんにちは",
    "hi": "やあ",
    "good morning": "おはようございます",
    "good evening": "こんばんは",
    "good night": "おやすみなさい",
    "goodbye": "さようなら",
    "thank you": "ありがとう",
    "thanks": "ありがとう",
    "sorry": "ごめんなさい",
    "please": "お願いします",
    "yes": "はい",
    "no": "いいえ",
    "okay": "大丈夫",
    "see you": "またね",
    "nice to meet you": "はじめまして",
    "how are you": "元気ですか",
    "i am fine": "元気です",
    "what is your name": "あなたの名前は何ですか",
    "my name is": "私の名前は",
    "where are you": "どこにいますか",
    "what are you doing": "何をしていますか",
    "i understand": "分かりました",
    "i don't understand": "分かりません",
    "help me": "助けてください",
    "wait": "待って",
    "come here": "ここに来て",
    "let's go": "行きましょう",
    "i am hungry": "お腹が空きました",
    "i am tired": "疲れました",
    "i am happy": "嬉しいです",
    "i am sad": "悲しいです",
    "i like it": "それが好きです",
    "i don't like it": "それが好きではありません",
    "i am going home": "家に帰ります",
    "i am going to school": "学校に行きます",
    "mother": "母",
    "father": "父",
    "brother": "兄弟",
    "sister": "姉妹",
    "family": "家族",
    "friend": "友達",
    "teacher": "先生",
    "student": "学生",
    "school": "学校",
    "class": "クラス",
    "book": "本",
    "pen": "ペン",
    "bag": "バッグ",
    "house": "家",
    "room": "部屋",
    "door": "ドア",
    "window": "窓",
    "car": "車",
    "train": "電車",
    "bus": "バス",
    "road": "道",
    "food": "食べ物",
    "water": "水",
    "milk": "牛乳",
    "rice": "ご飯",
    "bread": "パン",
    "tea": "お茶",
    "coffee": "コーヒー",
    "cat": "猫",
    "dog": "犬",
    "bird": "鳥",
    "today": "今日",
    "tomorrow": "明日",
    "yesterday": "昨日",
    "morning": "朝",
    "afternoon": "午後",
    "evening": "夕方",
    "night": "夜",
    "time": "時間",
    "money": "お金",
    "phone": "電話",
    "computer": "コンピューター",
    "music": "音楽",
    "movie": "映画",
    "game": "ゲーム",
    "work": "仕事",
    "shop": "店",
    "hospital": "病院",
    "city": "街",
    "country": "国",
    "good": "良い",
    "bad": "悪い",
    "big": "大きい",
    "small": "小さい",
    "beautiful": "美しい",
    "happy": "嬉しい",
    "sad": "悲しい",
    "hot": "暑い",
    "cold": "寒い",
    "fast": "速い",
    "slow": "遅い",
    "easy": "簡単",
    "difficult": "難しい",
    "new": "新しい",
    "old": "古い",
    "go": "行く",
    "come": "来る",
    "eat": "食べる",
    "drink": "飲む",
    "sleep": "寝る",
    "wake up": "起きる",
    "see": "見る",
    "listen": "聞く",
    "speak": "話す",
    "read": "読む",
    "write": "書く",
    "learn": "学ぶ",
    "play": "遊ぶ",
    "want": "欲しい",
    "like": "好き",
    "love": "愛する",
    "help": "助ける",
    "know": "知る",
"i am hungry": "お腹が空きました",
"i am tired": "疲れました",
"i am happy": "嬉しいです",
"i am going home": "家に帰ります",
"i am going to school": "学校に行きます",
"what are you doing": "何をしていますか",
"how are you": "元気ですか",
"what is your name": "あなたの名前は何ですか",
"nice to meet you": "はじめまして",
"i don't understand": "分かりません",
"please help me": "助けてください",
"where are you": "どこにいますか",
"what time is it": "今何時ですか",
"see you tomorrow": "また明日",
"have a good day": "良い一日を"}


while True:
    print("\n===== JAPANESE TRANSLATOR =====")
    print("1. English → Japanese")
    print("2. Japanese → English")
    print("3. Exit")

    choice = input("Choose 1, 2 or 3: ")

    if choice == "3":
        print("Goodbye!")
        break

    if choice == "1":
        text = input("Enter English word or sentence: ").lower()

        if text in translations:
    print("Japanese:", translations[text])

elif text.startswith("i like "):
    thing = text[7:]
    if thing in translations:
        print("Japanese:", "私は" + translations[thing] + "が好きです")
    else:
        print("Japanese:", "私は" + thing + "が好きです")

elif text.startswith("i want "):
    thing = text[7:]
    if thing in translations:
        print("Japanese:", "私は" + translations[thing] + "が欲しいです")
    else:
        print("Japanese:", "私は" + thing + "が欲しいです")

elif text.startswith("i am going to "):
    place = text[14:]
    if place in translations:
        print("Japanese:", "私は" + translations[place] + "に行きます")
    else:
        print("Japanese:", "私は" + place + "に行きます")

else:
    words = text.split()
    result = []

    for word in words:
        if word in translations:
            result.append(translations[word])
        else:
            result.append("[" + word + "]")

    print("Japanese:", " ".join(result))

    elif choice == "2":
        text = input("Enter Japanese word or sentence: ")

        if text in reverse_translations:
            print("English:", reverse_translations[text])
        else:
            print("Sorry, I don't know that Japanese phrase yet.")

    else:
        print("Please choose 1, 2 or 3.")
