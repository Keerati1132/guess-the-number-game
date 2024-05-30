import random

def play_game():
    print("ยินดีต้อนรับสู่เกมทายเลข!")
    player_name = input("โปรดป้อนชื่อของมึง: ")
    secret_number = random.randint(1, 10)
    attempts = 0
    score = 5  

    while True:
        guess = int(input("โปรดเดาตัวเลข (1-10): "))
        attempts += 1

        if guess < secret_number:
            print("ตัวเลขของมึงน้อยเกินไป!")
            score -= 1  
        elif guess > secret_number:
            print("ตัวเลขของมึงมากเกินไป!")
            score -= 1  
        else:
            print(f"ยินดีด้วย {player_name}! มึงทายถูกต้องแล้วเป็นตัวเลข {secret_number} ในครั้งที่ {attempts}!")
            print(f"คะแนนของมึงคือ: {score}") 
            break

    play_again = input("ต้องการเล่นอีกครั้งหรือไม่? (ใช่/ไม่): ")
    if play_again.lower() == "ใช่":
        play_game()
    else:
        print("ขอบคุณที่ร่วมเล่นเกมกับเรา!")

play_game()
