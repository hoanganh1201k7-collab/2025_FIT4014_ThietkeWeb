import os
import time

heart_frames = [
    """
     .:::.   .:::.
    :::::::.:::::::
    :::::::::::::::
    ':::::::::::::'
      ':::::::::'
        ':::::'
          ':'
    """,
    """
      .:::.     .:::.
    ::::::::. .:::::::
    ::::::::::::::::::
    '::::::::::::::::'
      '::::::::::::'
        '::::::::'
          '::::'
            ':'
    """,
    """
       .::::.     .::::.
    ::::::::::. .:::::::::
    ::::::::::::::::::::::
    '::::::::::::::::::::'
      '::::::::::::::::'
        '::::::::::::'
          ':::::::' 
            ':::'
              '
    """
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def heartbeat():
    try:
        while True:
            for frame in heart_frames + heart_frames[::-1]:
                clear()
                print(frame)
                time.sleep(0.2)
    except KeyboardInterrupt:
        clear()
        print("❤️ Kết thúc hiệu ứng.")

heartbeat()
