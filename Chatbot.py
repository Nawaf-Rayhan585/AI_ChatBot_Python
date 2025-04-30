import random
import time
import datetime
import difflib
import re
import math
from collections import defaultdict


def o1_mini():
    greetings = [
        "Hello there! 👋", "Hi friend! 😊", "Hey! Nice to meet you! 🎉",
        "Howdy! 😃", "Greetings! 🤖", "Hiya! 👋", "Yo! ✌️"
    ]

    farewells = [
        "Goodbye! 👋", "See you later! 🚀", "Bye bye! 😊",
        "Until next time! ✨", "Catch you later! 🕶️", "Take care! ❤️", "Adios! 👋"
    ]

    jokes = [
        "Why don't scientists trust atoms? Because they make up everything! 🤣",
        "What do you call a fake noodle? An impasta! 🍝",
        "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
        "What do you call a bear with no teeth? A gummy bear! 🐻",
        "Why can’t your nose be 12 inches long? Because then it would be a foot! 👃",
        "I told my computer I needed a break, and now it won’t stop sending me beach pictures! 🏖️",
        "Why did the math book look sad? Because it had too many problems! 📘",
        "What do you call cheese that isn't yours? Nacho cheese! 🧀",
        "Why did the bicycle fall over? It was two-tired! 🚲"
    ]

    facts = [
        "Honey never spoils! Archaeologists found 3000-year-old honey that's still good! 🍯",
        "Octopuses have three hearts! 🐙",
        "A day on Venus is longer than a year on Venus! ☀️",
        "The Hawaiian alphabet has only 12 letters! 🌺",
        "Bananas are berries, but strawberries aren't! 🍌🍓",
        "Sharks existed before trees! 🦈🌲",
        "There are more stars in the universe than grains of sand on Earth. 🌌",
        "Sloths can hold their breath longer than dolphins. 🦥",
        "Wombat poop is cube-shaped! 🟫"
    ]

    quotes = [
        "The only way to do great work is to love what you do. – Steve Jobs 💼",
        "Be yourself; everyone else is already taken. – Oscar Wilde 🎭",
        "In the middle of every difficulty lies opportunity. – Albert Einstein 🧠",
        "Believe you can and you're halfway there. – Theodore Roosevelt 💪",
        "You miss 100% of the shots you don’t take. – Wayne Gretzky 🏒"
    ]

    riddles = [
        "What has to be broken before you can use it? An egg! 🥚",
        "I'm tall when I'm young, and I'm short when I'm old. What am I? A candle! 🕯️",
        "What has hands but can’t clap? A clock! 🕒",
        "What gets wetter the more it dries? A towel! 🧼",
        "The more you take, the more you leave behind. What are they? Footsteps! 👣"
    ]

    bot_name = "o1_mini"
    print(f"🤖 {bot_name} is starting up...")
    time.sleep(1)

    print(f"""
    
        Welcome to {bot_name}!
        
        I can chat about:
        😜 'joke' - Hear a funny joke.
        🧠 'fact' - Learn something new.
        🕒 'quotes' - get motivated
        🧩 'riddles' - riddles that trick your brain.
        🌈 'color' - my favorite color.
        👋 'bye' - end chat.
         
    
    """)

    chatting = True
    while chatting:
        user_input = input("😊 You: ").strip().lower()

        if user_input in ["hi", "hello", "hii", "hiii", "hey", "howdy", "ayo", "helloo"]:
            print("typing...")
            time.sleep(1)
            print(f"🤖 {bot_name}: {random.choice(greetings)}")


        elif "joke" in user_input or "jokes" in user_input:
            print("typing...")
            time.sleep(1)
            print(f"🤖 {bot_name}: {random.choice(jokes)}")

        elif "fact" in user_input or "facts" in user_input:
            print("typing...")
            time.sleep(1)
            print(f"🤖 {bot_name}: {random.choice(facts)}")

        elif "riddle" in user_input or "riddles" in user_input:
            print("typing...")
            time.sleep(1)
            print(f"🤖 {bot_name}: {random.choice(riddles)}")

        elif "quote" in user_input or "quotes" in user_input:
            print("typing...")
            time.sleep(1)
            print(f"🤖 {bot_name}: {random.choice(quotes)}")

        elif "color" in user_input:
            print("typing...")
            time.sleep(1)
            print(
                f"🤖 {bot_name}: I like electric blue! ⚡💙, Blue is a color often associated with feelings of calmness, peace, and serenity, and is also linked to concepts like trust, loyalty, and authority. What About You? What Colors Do You Like?")
            color = input("😊 You: ")
            print(f"🤖 {bot_name}: {color} is a great color! many people really love {color}")

        elif user_input in ["bye", "exit", "quit", "goodbye"]:
            print("typing...")
            time.sleep(1)
            print(f"🤖 {bot_name}: {random.choice(farewells)}")
            chatting = False

        else:
            responses = [
                "sorry, I am not sure about that!"
                "I'm Not Sure i understand, try asking for a joke or fact"
            ]
            print("typing...")
            time.sleep(1)
            print(f"🤖 {bot_name}: {random.choice(responses)}")
    print("Thanks For Chatting With Me, Run To Chat with me later! 👋")

def o1_pro():
    bot_name = "o1_pro"
    greetings = [
        "Hello there! 👋", "Hi friend! 😊", "Hey! Nice to meet you! 🎉", "Howdy! 😃", "Greetings! 🤖", "Hiya! 👋",
        "Yo! ✌️",
        "Welcome, human! 🌍", "Hey hey! 🙌", "Nice to see you! 😄", "Hi! Ready to chat? 💬", "Aloha! 🌺", "Sup! 😎",
        "Hello sunshine! ☀️", "Hey there, superstar! 🌟", "What's up? ⬆️", "Bonjour! 🇫🇷", "Hola amigo! 🇪🇸",
        "Good to see you! 👀", "Hi there, legend! 🏆"
    ]

    farewells = [
        "Goodbye! 👋", "See you later! 🚀", "Bye bye! 😊", "Until next time! ✨", "Catch you later! 🕶️",
        "Take care! ❤️",
        "Adios! 👋", "Stay awesome! 🌈", "Don't be a stranger! 👻", "Peace out! ✌️", "Later, alligator! 🐊",
        "Have a good one! 🎈", "Talk soon! 📞", "Ciao! 🇮🇹", "See ya on the flip side! 🔄", "Keep smiling! 😁",
        "Farewell, adventurer! 🧭", "Good luck out there! 🍀", "Until we meet again! 🔮"
    ]

    jokes = [
        "Why don't scientists trust atoms? Because they make up everything! 🤣",
        "Why did the math book look sad? Because it had too many problems! 📘",
        "Why did the bicycle fall over? It was two-tired! 🚲",
        "Why can't your nose be 12 inches long? Because then it would be a foot! 👃",
        "I told my computer I needed a break, and now it won’t stop sending me vacation ads. 💻",
        "Parallel lines have so much in common... it’s a shame they’ll never meet. 😢",
        "I’m reading a book on anti-gravity. It’s impossible to put down! 📚",
        "Why don’t skeletons fight each other? They don’t have the guts. 💀",
        "What do you call fake spaghetti? An impasta! 🍝",
        "I used to play piano by ear, but now I use my hands. 🎹"
    ]

    facts = [
        "Honey never spoils! 🍯", "Octopuses have three hearts! 🐙",
        "Sloths can hold their breath longer than dolphins. 🦥",
        "Bananas are berries, but strawberries aren’t! 🍌🍓", "A day on Venus is longer than its year. 🌌",
        "Sharks existed before trees. 🦈", "Wombat poop is cube-shaped. 🧱",
        "The Eiffel Tower can grow taller in summer. 🗼",
        "Your heart beats around 100,000 times a day. ❤️",
        "There are more stars in the universe than grains of sand on Earth. ✨"
    ]

    quotes = [
        "The only way to do great work is to love what you do. – Steve Jobs 💼",
        "Believe you can and you're halfway there. – Theodore Roosevelt 💪",
        "Do what you can, with what you have, where you are. – Theodore Roosevelt 🎯",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill 🛡️",
        "In the middle of every difficulty lies opportunity. – Albert Einstein 💡",
        "Don’t watch the clock; do what it does. Keep going. – Sam Levenson ⏰",
        "Start where you are. Use what you have. Do what you can. – Arthur Ashe 🏁",
        "You miss 100% of the shots you don’t take. – Wayne Gretzky 🏒",
        "Be yourself; everyone else is already taken. – Oscar Wilde 🎭"
    ]

    riddles = [
        "What has to be broken before you can use it? An egg! 🥚",
        "I'm tall when I'm young, and short when I'm old. What am I? A candle! 🕯️",
        "What gets wetter the more it dries? A towel! 🧺",
        "I speak without a mouth and hear without ears. What am I? An echo! 🔊",
        "What has hands but can't clap? A clock! ⏰",
        "The more you take, the more you leave behind. What am I? Footsteps! 👣",
        "What can run but never walks, has a bed but never sleeps? A river! 🌊",
        "What comes once in a minute, twice in a moment, but never in a thousand years? The letter M! 🔠"
    ]

    advice = [
        "Take breaks. It's okay to rest and reset. 🌿",
        "Drink water and take a walk. Simple things help a lot. 🚶‍♂️",
        "Don’t stress over things you can’t control. Focus on what you can. 🧘",
        "Sleep is powerful. Prioritize it. 🛏️",
        "Start small. Progress is progress. 🧱",
        "Listen more than you speak. You’ll learn more that way. 👂",
        "Celebrate your wins, no matter how small. 🎉",
        "Don’t compare your journey to others. 🌄",
        "Ask for help when you need it. That’s strength, not weakness. 💬",
        "Kindness is always a good choice. 💖"
    ]

    circle = """
        , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '
    """

    triangle = r"""
    
                  /\
                 /  \
                /    \
               /______\       
                    
    """

    donut = """
        
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⠤⠤⠶⠒⠒⠒⠲⠦⠤⠤⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠛⠋⠁⣘⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠯⢤⡤⠀⠉⠉⠛⠲⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠛⠁⠀⠀⠀⠀⢘⣯⢿⠂⠀⠀⠀⠀⠀⢀⠀⠀⠀⠛⠛⠋⠃⠀⠀⠀⠀⠀⠀⠀⠉⠓⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠞⠁⠀⢠⡤⢤⣤⡀⠀⠀⠻⠛⠀⠀⠀⠠⣿⣯⣽⠛⠀⠀⠀⠀⠀⠀⠰⣶⣶⠀⠀⠀⢠⣼⢻⡄⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠈⠛⠓⠛⠀⠀⣠⣤⣄⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣼⡆⠀⠀⠈⡿⠟⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⠏⠀⢠⡤⠤⣤⠀⠀⠀⠀⠀⠀⠀⠨⣷⣽⡀⠀⠀⠀⠀⠀⠀⢠⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⢦⡄⠀⠘⢧⡀⠀⠀⠀⠀
⠀⠀⠀⢠⡞⠃⠀⠀⠘⠛⠛⠃⠀⠀⣀⣤⣀⠀⠀⠀⠀⠉⠀⠀⡶⣦⠀⠀⠀⠈⠻⣭⣿⠀⠀⠀⢀⣀⠀⢀⣶⣴⣀⠀⠀⠈⠻⣼⡇⠀⢐⣅⠹⡄⠀⠀⠀
⠀⠀⢠⡏⢰⣆⠀⠀⠀⠀⠀⠀⠠⣾⣯⠿⠛⠀⠀⠀⠀⠀⠀⠀⢿⣼⠀⠀⠀⠀⠈⠁⠀⠀⠀⣴⠟⡿⠀⠈⠛⠲⠿⠇⠀⠀⠀⠀⠀⠀⢸⡟⢷⠼⣆⠀⠀
⠀⢠⡏⠀⢸⣹⡇⠀⠀⡀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠉⠳⣄⠀⠀⠀⠉⠋⠁⠀⠀⠀⠀⠀⠀⢠⣠⡀⠀⠀⠀⠘⠛⠋⠀⠹⡆⠀
⢀⡾⠀⠀⠘⠙⠃⠀⢼⣻⡆⠀⠀⢠⢷⡄⠀⠀⠀⠀⣠⠞⠋⠉⠉⠛⠛⠁⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣯⡽⠋⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆
⢸⠃⠀⠀⠀⠀⠀⠀⠸⢷⠏⠀⠀⢺⣦⣷⠀⠀⠀⡾⠁⠀⠀⠀⠀⣀⣠⠤⠤⠤⣄⣀⠀⠈⠓⠲⠦⣀⠀⠀⠀⠀⠀⠈⠉⠀⠀⢀⡶⢖⣲⡆⠀⡀⠀⠀⢧
⡜⠀⣶⣒⣺⡆⠀⠀⠀⠀⣐⣤⢄⠀⠈⠀⠀⠀⢸⠁⠀⠀⣠⠶⠋⠁⠀⠀⠀⠀⠀⠈⠙⠶⣄⠀⠀⠈⢷⡀⠀⠀⠀⠀⠀⢀⡀⠸⠿⠉⠁⠁⠸⣿⣓⣶⢸
⡇⠀⠈⠉⠉⠀⠀⠀⠀⠘⢿⣍⣷⠆⠀⠀⠀⠀⢸⡀⠀⣶⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠷⡀⠀⢸⡇⠀⠀⠀⠀⠘⢿⣙⣶⡆⠀⠀⠀⠀⠀⠉⠋⢸
⡇⠀⠀⠀⠠⢹⢳⡄⠀⠀⠀⠉⠉⠀⠀⡴⣤⠀⠉⣷⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣤⡟⠁⢀⣴⢶⣄⠀⠀⠹⠛⠁⠀⠀⠀⣠⣤⠀⢀⢸
⣿⠀⠀⠀⠀⠘⠿⡇⠀⠀⠀⠀⠀⠀⠀⢿⣼⡄⠀⠈⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠺⠾⠋⠀⠀⠀⠀⣄⠀⠀⠀⢸⣷⡟⠀⢸⡼
⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠙⠶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⣇⠀⠀⠀⠉⠀⠀⢠⡇
⠸⣇⠀⠀⣴⢖⣳⠆⠀⠀⠀⠀⠀⢀⣤⣴⣶⠀⠀⠀⠀⠀⠀⠉⠙⠶⠤⣄⣀⣀⣀⣤⠶⠞⠉⠀⠀⢀⣶⠶⣄⡀⠀⠀⠀⠀⠈⠛⠛⠀⠀⣀⡀⠀⠀⣸⠇
⠀⠸⣆⠀⠙⠚⠁⠀⠀⠀⣴⡶⡄⢻⡷⠚⠋⠀⠀⠀⠀⣶⢶⡀⠀⠀⠀⠀⢔⣤⣀⠀⠀⠀⠀⠀⠀⠀⠨⠓⠛⠁⠀⠀⣠⡶⣶⡇⠀⠀⠈⣧⣱⠀⢠⡟⠀
⠀⠀⠹⣧⡄⠀⠀⠀⠀⠀⠘⢷⡿⠀⠀⠀⠀⠀⠀⠀⠀⠿⣦⣷⠀⠀⠀⠀⠙⣿⣿⡆⠀⢀⣶⡦⣄⣀⠀⠀⠀⠀⠀⠠⣿⠾⠃⠀⠀⠀⠀⠈⢙⣱⣿⠃⠀
⠀⠀⠀⠸⡏⠳⣤⣄⣀⣀⣀⠀⠀⠀⠀⠴⡟⣦⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠩⠓⢻⠋⠀⠀⠀⢀⣤⣤⣨⠀⠀⠀⠀⢀⣠⡴⠚⢱⠇⠀⠀
⠀⠀⠀⠀⠹⡄⠀⠀⠀⠉⠙⠓⢦⡀⠀⠀⠻⢿⠀⠀⠀⢀⣠⣤⢼⡄⠀⠀⢀⣤⡴⣿⠀⠀⠀⠀⢀⣠⡄⠀⠀⠘⠓⠲⠛⣀⣤⠴⠚⠋⠁⠀⣰⠏⠀⠀⠀
⠀⠀⠀⠀⠀⠸⣆⠀⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀⠀⠀⠈⠻⠿⠋⠀⠀⠀⠼⠿⠛⠋⠀⠀⠀⣴⣿⡴⠃⠀⠀⠀⠀⢀⡼⠋⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⢧⡀⠀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠿⠳⢦⡀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⢠⡞⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠀⠀⠀⠀⠀⠙⢦⣀⠀⠀⠀⣀⣤⠞⠋⠀⠀⠀⠀⠉⠓⢤⣀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⡀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⠒⠐⠒⠚⠉⠀⠀⠀⠀⣀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠓⠒⠤⠤⠤⣤⣤⣤⡤⠤⠤⠤⠒⠒⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   

    """

    square = """                                                                                                                                                                                      
██▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                
▒▒                          ▓▓                                        
▒▒                          ▓▓                                        
▒▒                          ▓▓                                        
▒▒                          ▓▓                                        
▒▒                          ▓▓                                        
▒▒                          ▓▓                                        
▒▒                          ▓▓                                                                                                                   
██▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒ """

    tree = r"""
        
        
          &&& &&  & &&
      && &\/&\|& ()|/ @, &&
      &\/(/&/&||/& /_/)_&/_&
   &() &\/&|()|/&\/ '%" & ()
  &_\_&&_\ |& |&&/&__%_/_& &&
&&   && & &| &| /& & % ()& /&&
 ()&_---()&\&\|&&-&&--%---()~
     &&     \|||
             |||
             |||
             |||
       , -=-~  .-^- _ ,
    """

    image = r"""
              ___   ____
        /' --;^/ ,-_\     \ | /
       / / --o\ o-\ \\   --(_)-- 
      /-/-/|o|-|\-\\|\\   / | \
       '   |-|    '
             |-|
             |-|O
             |-(\,__
          ...|-|\--,\_....
      ,;;;;;;;;;;;;;;;;;;;;;;;;,.
~~,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,  ______   ---------   _____     ------
    """


    def get_time():
        return datetime.datetime.now().strftime("It's %I:%M %p right now. 🕒")

    def process_math(expression):
        """Safely process math expressions."""
        try:
            expression = re.sub(r'[^0-9+\-*/().]', '', expression)  # Remove unsafe characters
            result = eval(expression, {"__builtins__": None}, {"math": math})  # Safer evaluation
            return f"The result is: {result} 🧮"
        except:
            return "Hmm, I couldn't calculate that. Try something like '12 / 4 + 3'."

    def match_input(user_input, keywords):
        """Check if the input matches any keyword."""
        return any(keyword in user_input for keyword in keywords)

    def get_best_match(user_input, options):
        """Find the closest match using fuzzy matching."""
        matches = difflib.get_close_matches(user_input, options, n=1, cutoff=0.6)
        return matches[0] if matches else None

    print(f"🤖 {bot_name} is starting up...")
    time.sleep(1)
    print(f"""
        Welcome to {bot_name}!
        Ask me for:
        😜 'joke', 🧠 'fact', 🧩 'riddle', 🕒 'quote', 🧃 'advice'
        ⏰ 'time', 🧮 'math', 💬 'chat'
        ---------------------------------------------------------------------------
        
        creating image:
        ⭕'circle' ⬜'square' 🍩'donut' 📐'triangle' 🌳'tree' 🌊'sea' 🐦'nature' ☺️'relax'
        
        ---------------------------------------------------------------------------------
        👋 Type 'bye' to exit.
        """)

    chatting = True
    while chatting:
        user_input = input("😊 You: ").strip().lower()

        if match_input(user_input, ["hi", "hello", "hey", "hola", "yo", "howdy"]):
            print(f"🤖 {bot_name}: {random.choice(greetings)}")

        elif match_input(user_input, ["joke"]):
            print(f"🤖 {bot_name}: {random.choice(jokes)}")

        elif match_input(user_input, ["fact"]):
            print(f"🤖 {bot_name}: {random.choice(facts)}")

        elif match_input(user_input, ["quote"]):
            print(f"🤖 {bot_name}: {random.choice(quotes)}")

        elif match_input(user_input, ["riddle"]):
            print(f"🤖 {bot_name}: {random.choice(riddles)}")

        elif match_input(user_input, ["circle"]):
            print(f"🤖 {bot_name}: ")
            print(circle)

        elif match_input(user_input, ["triangle"]):
            print(f"🤖 {bot_name}: ")
            print(triangle)

        elif match_input(user_input, ["donut"]):
            print(f"🤖 {bot_name}: ")
            print(donut)
        elif match_input(user_input, ["square"]):
            print(f"🤖 {bot_name}: ")
            print(square)

        elif match_input(user_input, ["tree"]):
            print(f"🤖 {bot_name}: ")
            print(tree)

        elif match_input(user_input, ["nature" , "image" , "beach" , "sea", "relax"]):
            print(f"🤖 {bot_name}: ")
            print(image)

        elif "color" in user_input:
            print(f"🤖 {bot_name}: I like electric blue! ⚡💙 What's your favorite color?")
            color = input("😊 You: ")
            print(f"🤖 {bot_name}: {color.capitalize()} is beautiful! Great choice.")

        elif "time" in user_input:
            print(f"🤖 {bot_name}: {get_time()}")

        elif "math" in user_input or any(op in user_input for op in "+-*/"):
            expression = ''.join([c for c in user_input if c.isdigit() or c in '+-*/. '])
            print(f"🤖 {bot_name}: {process_math(expression)}")

        elif "advice" in user_input:
            print(f"🤖 {bot_name}: {random.choice(advice)}")

        elif "feel" in user_input or "how are you" in user_input:
            print(f"🤖 {bot_name}: I'm just a bot, but I'm always here to chat. How are you feeling?")
            feeling = input("😊 You: ")
            print(f"🤖 {bot_name}: Thanks for sharing. I’m glad you opened up about feeling {feeling}. 💬")


        elif user_input in ["bye", "exit", "quit", "goodbye"]:
            print(f"🤖 {bot_name}: {random.choice(farewells)}")
            chatting = False

        else:
            best_match = get_best_match(user_input,
                                        ["joke", "fact", "quote", "riddle", "time", "math", "color", "advice"])
            if best_match:
                print(f"🤖 {bot_name}: Did you mean '{best_match}'? Try again with that keyword. 💡")
            else:
                print(f"🤖 {bot_name}: I'm not sure how to respond to that yet. Try asking for a joke, fact, or riddle!")

    print("Thanks for chatting! Run me again anytime. 👋")


def main():
    print("""
        👶 o1-mini - A small chatbot, slow answers.
        🤖🧠 o1-pro - very intelligent and smart chatbot takes no time to give answers.

        type: 'o1-mini', 'o1-pro' to choose

        ==================================================
    """)

    model = input("Which Model Do You You Want To Use? Type: ").strip()

    if (model == "o1 mini"):
        o1_mini()

    elif (model == "o1 pro"):
        o1_pro()


