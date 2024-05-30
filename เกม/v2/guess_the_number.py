import time
import sys

def main():
    # รับข้อความจากผู้ใช้
    user_input = input("Not done yet.: ")

    print("กำลังตั้งเวลา...")

    # รับเวลาที่ต้องการตั้ง
    hours = int(input("กรุณากรอกชั่วโมง (0-0): "))
    minutes = int(input("กรุณากรอกนาที (0-1): "))

    # คำนวณเวลาที่ต้องการ
    target_time = hours * 3600 + minutes * 60

    # แสดงข้อความที่ผู้ใช้กรอกด้วยขนาดที่ผู้ใช้กำหนด
    print("ข้อความที่คุณกรอกคือ: ", user_input)
    print("ขนาดของข้อความ: ", font_size)

    # รอจนกว่าจะถึงเวลาที่ต้องการ
    while True:
        current_time = time.localtime()
        current_seconds = current_time.tm_hour * 3600 + current_time.tm_min * 60 + current_time.tm_sec
        if current_seconds == target_time:
            print("เวลาที่ตั้งถึงแล้ว!")
            sys.exit()  # ปิดโปรแกรม
        time.sleep(1)

if __name__ == "__main__":
    main()
