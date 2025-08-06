import datetime # เพิ่มบรรทัดนี้

# ... โค้ดเดิม

def say_hello(name):
   now = datetime.datetime.now() # เพิ่มบรรทัดนี้
   print(f"Sayonara, {name} from {config.APP_NAME}!")
   print(f"Today is {now.strftime('%Y-%m-%d')}.") # เพิ่มบรรทัดนี้

# ... โค้ดเดิม
