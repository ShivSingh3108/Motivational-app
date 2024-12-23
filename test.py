import tkinter as tk
from tkinter import messagebox 

quotes=motivational_quotes=["Believe in yourself and all that you are.","Your only limit is your mind.","Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Dream bigger. Do bigger.",
    "Don’t stop when you’re tired. Stop when you’re done.","Wake up with determination. Go to bed with satisfaction.",
    "Do something today that your future self will thank you for.",
    "Little things make big days.",
    "It’s going to be hard, but hard does not mean impossible.",
    "Don’t wait for opportunity. Create it.",
    "Sometimes we’re tested not to show our weaknesses, but to discover our strengths.",
    "The key to success is to focus on goals, not obstacles.",
    "Dream it. Believe it. Build it.",
    "Your limitation—it’s only your imagination.",
    "Work hard in silence. Let success be your noise.",
    "If people are doubting how far you can go, go so far that you can’t hear them anymore.",
    "Be proud of how far you’ve come and have faith in how far you can go.",
    "Doubt kills more dreams than failure ever will.",
    "Success is what happens after you have survived all of your mistakes.","Don’t count the days, make the days count.",
    "Act as if what you do makes a difference. It does.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Never bend your head. Always hold it high. Look the world straight in the eye.",
    "What you get by achieving your goals is not as important as what you become by achieving your goals.",
    "Believe you can and you’re halfway there.",
    "When you have a dream, you’ve got to grab it and never let go.",
    "I can’t change the direction of the wind, but I can adjust my sails to always reach my destination.",
    "No matter what you’re going through, there’s a light at the end of the tunnel.",
    "It is our attitude at the beginning of a difficult task which, more than anything else, will affect its successful outcome.",
    "Life is like riding a bicycle. To keep your balance, you must keep moving.",
    "Just don’t give up trying to do what you really want to do.",
    "Limit your 'always' and your 'nevers.'",
    "Nothing is impossible. The word itself says 'I’m possible!'",
    "You are never too old to set another goal or to dream a new dream.","Try to be a rainbow in someone’s cloud.",
    "You do not find the happy life. You make it.",
    "Keep your face always toward the sunshine, and shadows will fall behind you.",
    "Stay close to anything that makes you glad you are alive.",
    "Happiness often sneaks in through a door you didn’t know you left open.",
    "Be the change that you wish to see in the world.",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us.",
    "Believe you can and you’re halfway there.",
    "No matter what people tell you, words and ideas can change the world.",
    "You don’t have to be perfect to be amazing.",
    "Do what you feel in your heart to be right—for you’ll be criticized anyway.",
    "Happiness is not by chance, but by choice.",
    "Life is not about waiting for the storm to pass but about learning to dance in the rain.",
    "Keep going. Everything you need will come to you at the perfect time.",
    "Failure is not the opposite of success; it’s part of success.",
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    "If you can dream it, you can achieve it.",
    "It’s not whether you get knocked down; it’s whether you get up.",
    "The only way to do great work is to love what you do.",
    "Don’t let yesterday take up too much of today.","The future belongs to those who believe in the beauty of their dreams.",
    "Do what you can, with what you have, where you are.",
    "You are enough just as you are.",
    "Start where you are. Use what you have. Do what you can.",
    "Opportunities don’t happen. You create them.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "Your passion is waiting for your courage to catch up.",
    "Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart.",
    "Make each day your masterpiece.",
    "It’s not what we do once in a while that shapes our lives, but what we do consistently.",
    "Life isn’t about finding yourself. It’s about creating yourself.",
    "The best way to predict the future is to create it.",
    "You don’t need to be perfect to start. Just start.", "The man on top of the mountain didn’t fall there.",
    "Success usually comes to those who are too busy looking for it.","Every day is a chance to get better.",
    "The best way to cheer yourself is to try to cheer someone else up.","Your time is limited, so don’t waste it living someone else’s life.",
    "Don’t limit your challenges. Challenge your limits.",
    "Be so good they can’t ignore you.","A goal is a dream with a deadline.",
    "Action is the foundational key to all success.",
    "The only way to achieve the impossible is to believe it is possible.",
    "If opportunity doesn’t knock, build a door.",
    "You are stronger than you think.",
    "It always seems impossible until it’s done.",
    "The harder the battle, the sweeter the victory.",
    "Perseverance is not a long race; it is many short races one after the other.",
    "Turn your wounds into wisdom.","Don’t quit. Suffer now and live the rest of your life as a champion.","Discipline is the bridge between goals and accomplishment.",
    "Do not wait; the time will never be ‘just right.’","Don’t let what you cannot do interfere with what you can do.","Set your goals high, and don’t stop till you get there.",
    "Honesty is the best policy","Old is Gold","health is wealth", "Time is money","Your strength is your foundation.","Every experience teaches you something valuable.","Just COOKKK!!!!!"]

def show_quote():
    try:
        number = int(entry.get())
        if 1 <= number <= len(quotes):
            quote_label.config(text=quotes[number - 1])
        else:
            messagebox.showerror("Invalid Input", "Enter a number between 1 and 100")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

root =  tk.Tk()
root.title("||||||Motivational App||||||Ahoy , Get your motivation")
root.geometry("400x400")
root.config(bg="#942222")
title= tk.Label(root, text="Motivational App For youuu", font=("Lucida Calligraphy", 24), bg="#942222",fg="Gold")
title.pack(pady=10)
instruction = tk.Label( root, text="Pirates!!!!!! Enter a number between 1 and 100:", font=("Arial", 12), bg="#942222",fg="Gold")
instruction.pack(pady=5)
entry =tk.Entry(root, justify="center",font=("Arial", 10),)
entry.pack(pady=5)
button = tk.Button(root, text="Ahoy Pirates , Get Motivation", font=("Pixal", 12), command=show_quote, bg="#056995", fg="white")
button.pack(pady=10)
quote_label = tk.Label(root, text="", font=("Lucida Calligraphy", 20), wraplength=300, bg="#942222", fg="Gold")
quote_label.pack(pady=20)
title =tk.Label(root, text="Thanks for Sailing here --by SHIV SINGH", font=("Lucida Calligraphy", 10 ), bg="#942222",fg="Gold")
title.pack(pady=10)
title =tk.Label(root, text="Just took motivational quotes and bit help from chatgpt", font=("Arial", 5), bg="#942222",fg="Black")
title .pack(pady=10)
root.mainloop()

