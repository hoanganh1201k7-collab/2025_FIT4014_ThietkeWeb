import random

def choi_doan_so():
    print("🎮 Chào mừng bạn đến với trò chơi Đoán số!")
    so_dung = random.randint(1, 100)
    so_lan_doan = 0

    while True:
        try:
            doan = int(input("👉 Nhập một số từ 1 đến 100: "))
            so_lan_doan += 1

            if doan < 1 or doan > 100:
                print("⚠️ Số phải nằm trong khoảng từ 1 đến 100.")
            elif doan < so_dung:
                print("🔻 Số bạn đoán nhỏ hơn.")
            elif doan > so_dung:
                print("🔺 Số bạn đoán lớn hơn.")
            else:
                print(f"🎉 Chúc mừng! Bạn đã đoán đúng số {so_dung} sau {so_lan_doan} lần thử.")
                break
        except ValueError:
            print("❌ Vui lòng nhập một số hợp lệ.")

# Bắt đầu trò chơi
choi_doan_so()
