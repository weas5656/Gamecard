import os,time # นำเข้าโมดูล os และ time
import random # นำเข้าโมดูล random
class Login: # สร้างคลาส Login
    def __init__(self): # เมท็อดที่ใช้สำหรับการกำหนดค่าเริ่มต้น
        self.users = {} # สร้างพจนานุกรมเปล่าสำหรับเก็บข้อมูลผู้ใช้
    
    def register(self,username,password): # เมท็อดสำหรับการลงทะเบียนผู้ใช้ใหม่
        if username in self.users: # ตรวจสอบว่ามีชื่อผู้ใช้นี้อยู่แล้วหรือไม่
            print("Username already exists..") # พิมพ์ข้อความว่ามีชื่อผู้ใช้นี้อยู่แล้ว
        else:
            self.users[username] = password # เพิ่มชื่อผู้ใช้และรหัสผ่านลงในพจนานุกรม
            print('') # พิมพ์บรรทัดว่าง
            time.sleep(1) # หน่วงเวลา 1 วินาที
            print("Register Successful!") # พิมพ์ข้อความว่าการลงทะเบียนเสร็จสมบูรณ์
    
    def login(self,username,password): # เมท็อดสำหรับเข้าสู่ระบบ
        if username not in self.users: # ตรวจสอบว่ามีชื่อผู้ใช้นี้หรือไม่
            print('') # พิมพ์บรรทัดว่าง
            print("Invalid Username. Please register Again.") # พิมพ์ข้อความว่าชื่อผู้ใช้ไม่ถูกต้อง โปรดลงทะเบียนอีกครั้ง
            print('') # พิมพ์บรรทัดว่าง
            print('--------------------')
            print('') # พิมพ์บรรทัดว่าง
            time.sleep(1.5) # หน่วงเวลา 1.5 วินาที
            os.system('cls') # ลบหน้าจอ terminal
            print('--------------------')
            print('') # พิมพ์บรรทัดว่าง
            a.login(input('Username Again : '),input('Password Again : ')) # ทำการเรียกเมท็อด login อีกครั้ง

        elif self.users[username] != password: # ตรวจสอบว่ารหัสผ่านไม่ถูกต้อง
            print('') # พิมพ์บรรทัดว่าง
            print("Incorrect password. Please try again.") # พิมพ์ข้อความว่ารหัสผ่านไม่ถูกต้อง โปรดลองอีกครั้ง
            print('') # พิมพ์บรรทัดว่าง
            print('--------------------')
            print('') # พิมพ์บรรทัดว่าง
            time.sleep(1.5) # หน่วงเวลา 1.5 วินาที
            os.system('cls') # ลบหน้าจอ terminal
            print('--------------------') # พิมพ์ขีดกลาง
            print('') # พิมพ์บรรทัดว่าง
            a.login(input('Username Again : '),input('Password Again : ')) # ทำการเรียกเมท็อด login อีกครั้ง

        else:
            print('') # พิมพ์บรรทัดว่าง
            time.sleep(1) # หน่วงเวลา 1 วินาที
            print("Login successful!") # พิมพ์ข้อความว่าเข้าสู่ระบบสำเร็จ

class CardGame: # สร้างคลาส CardGame
    def __init__(self): # เมท็อดที่ใช้สำหรับกำหนดค่าเริ่มต้น
        self.inventory = [] # สร้างลิสต์ว่างสำหรับเก็บรายการการ์ด
        self.credit = 500 # กำหนดเครดิตเริ่มต้น
        self.cards = {             # สร้างพจนานุกรมเก็บข้อมูลการ์ดพร้อมค่าพลังการ์ด
            'Kamado': 90,
            'Uzumaki': 80,
            'Kakashi': 60,
            'Genzo': 60,           #cards ตรงตัวเลขจะเป็นค่าพลังการ์ดยิ่งเยอะ แรร์
            'Obi': 30,
            'Gintama': 20,
            'Hotaki': 10,
            'God': 5,
            'Devil': 5 }

    def main(self):
        print('-----Main Menu-----')
        print('')
        print('1. Random_Box')  # แสดงเมนูสุ่มการ์ด
        print('2. Inventory')  # แสดงเมนูแสดงรายการการ์ด
        print('3. Start Fighting')  # เพิ่มเมนูเปรียบเทียบการ์ด
        print('4. Data Card')  # เมนูแสดงข้อมูลการ์ด
        print('')

        try:
            menu = int(input('Select 1 to 4 : '))
            print('')
        except ValueError:
            print("Please enter a number.")
            time.sleep(2)
            os.system('cls')
            c.main()

        if menu == 1:
            self.random_box()  # ถ้าผู้เล่นเลือก 1: สุ่มการ์ดใหม่
            time.sleep(5)  # หน่วงเวลา
            os.system('cls')  # ลบ terminal
            c.main()
            time.sleep(3)  # หน่วงเวลา 3 วินาที
        elif menu == 2:
            print('Your Credit =', self.credit, ':', 'Your Cards:', self.inventory)  # แสดงรายการการ์ดที่อยู่ใน inventory
            print('-------------------------------')
            print('')
            print('If you want to go back to the main menu?')
            i = input('Press yes or no : ')
            if i == 'yes':
                time.sleep(2)  # หน่วงเวลา
                os.system('cls')  # ลบ terminal
                c.main()  # กลับไปที่ main()
            elif i == 'no':
                exit()
            else:
                exit()
        elif menu == 3:
            self.compare_cards()  # เรียกฟังก์ชันเปรียบเทียบการ์ด
            print('')
            time.sleep(2)
            os.system('cls')
            c.main()  # กลับไปที่ main()
        elif menu == 4:
            os.system('cls')  # ลบ terminal
            d.show_data()  # เรียกฟังก์ดูข้อมูลการ์ด
            print('-------------------------------')
            print('')
            print('If you want to go back to the main menu?')
            i = input('Press yes or no : ')
            if i == 'yes':
                time.sleep(2)  # หน่วงเวลา
                os.system('cls')  # ลบ terminal
                c.main()  # กลับไปที่ main()
            elif i == 'no':
                exit()
        else:
            exit()

    def random_box(self):
        # รายการการ์ดที่เรามีและค่าโจมตีของแต่ละการ์ด
        cards = {
            'Kamado': 5,
            'Uzumaki': 5,
            'Kakashi': 10,
            'Genzo': 20,
            'Obi': 30,               #cards ตรงตัวเลขจะเป็นความแรร์ของการ์ดยิ่งน้อย ยิ่งการ์ดแรร๋
            'Gintama': 60,
            'Hotaki': 60,
            'God': 80,
            'Devil': 90 }

        print('1 Box = 100 Credit') # แสดงราคาของกล่องเกมที่ผู้เล่นสามารถซื้อด้วยเครดิต
        box_amount = int(input('Box Amount : '))  # รับจำนวนกล่องที่ผู้เล่นต้องการซื้อ
        time.sleep(1.5) # หน่วงเวลา
        os.system('cls') # ลบหน้าจอ
        print('')
        print('Total Amount:', box_amount, 'Box') # แสดงจำนวนกล่องทั้งหมดที่ผู้เล่นต้องการ
        print('')
        total_price = box_amount * 100            # คำนวณราคาทั้งหมดของกล่องที่ต้องการซื้อ
        self.credit = self.credit - total_price   # หักเครดิตที่จ่ายไปจากเครดิตที่ผู้เล่นมี
        if self.credit < 0:
            print('Not enough Credit')            # แสดงข้อความเมื่อเครดิตไม่เพียงพอสำหรับการซื้อ
            self.credit = self.credit + total_price   # เพิ่มเครดิตที่หักไว้กลับมา
            time.sleep(5)      # หน่วงเวลา
            os.system('cls')   # ลบ terminal
            self.main()        # กลับไปที่หน้าเมนูหลัก
        print('Price', total_price, 'Credit')            # แสดงราคาทั้งหมดที่จ่ายและเครดิตที่เหลือ
        print('Credit balance remaining:', self.credit)  # แสดงเครดิตที่เหลือในบัญชี
        print('')
        input('Press Enter to continue: ') # รอผู้เล่นกด Enter เพื่อดำเนินการต่อ
        print('Waiting...') # แสดงข้อความ "Waiting..." เพื่อแสดงถึงการรอในขณะนั้น

        random_cards = random.choices(list(cards.keys()), weights=list(cards.values()), k=box_amount)    # สุ่มการ์ดจากรายการ cards ตามจำนวนกล่องที่เลือก
        print(random_cards)   # แสดงรายการการ์ดที่ถูกสุ่ม

        self.inventory.extend(random_cards)       # เพิ่มรายการการ์ดที่สุ่มได้เข้าไปใน inventory

    def compare_cards(self):
        if len(self.inventory) < 2:
            print("Not enough cards to fight.")   # พิมพ์ข้อความเมื่อไม่มีการ์ดเพียงพอสำหรับการประลอง
            return

        print("Your cards: ", self.inventory)     # แสดงรายการการ์ดที่อยู่ใน inventory
        print('')
        player1_card_name = input('Player 1: choose a card from your inventory: ')   # รับข้อมูลการ์ดที่ผู้เล่น 1 เลือก
        player1_card_attack = self.cards.get(player1_card_name)                      # ดึงข้อมูลค่าโจมตีของการ์ดที่ผู้เล่น 1 เลือก

        time.sleep(1.5)    # หน่วงเวลา
        os.system('cls')   # ลบหน้าจอ

        if player1_card_attack is not None:
            print("Waiting for Player 2 to choose a card...")     # พิมพ์ข้อความให้รอผู้เล่น 2 เลือกการ์ด
            print('')
            time.sleep(5)   # หน่วงเวลา

            # ผู้เล่น 2 สุ่มการ์ดและดึงพลังโจมตีของการ์ดที่ถือ
            player2_card_name = random.choice(self.inventory)        # สุ่มการ์ดจาก inventory ของผู้เล่น 2
            player2_card_attack = self.cards.get(player2_card_name)  # ดึงข้อมูลค่าโจมตีของการ์ดที่ถืออยู่จาก dictionary cards
            print(f'Player 2 has a {player2_card_name} card with attack {player2_card_attack}.')

            if player1_card_attack == player2_card_attack:       # เปรียบเทียบค่าโจมตีระหว่างการ์ดของผู้เล่น 1 และ 2
                print("It's a tie!")    # แสดงข้อความเมื่อเสมอ
                time.sleep(7)           # หน่วงเวลา
                os.system('cls')        # ลบหน้าจอ
                c.main()                # กลับไปที่หน้าหลักของเกม
            else:
                if player1_card_attack > player2_card_attack:    # ตรวจสอบผลของการเปรียบเทียบ
                    print("Player 1 Wins.")                      # แสดงผลลัพธ์เมื่อผู้เล่น 1 ชนะ
                    print('You win credit + 700')                # แสดงข้อความว่าได้รับเครดิตเพิ่ม
                    self.inventory = []
                    self.credit += 700                           # เพิ่มเครดิตของผู้เล่น
                    time.sleep(7)                                # หน่วงเวลา
                    os.system('cls')                             # ลบหน้าจอ
                    c.main()
                else:
                    print("Player 2 Wins.")                      # แสดงผลลัพธ์เมื่อผู้เล่น 2 ชนะ
                    self.inventory = []                          # ล้าง inventory ของผู้เล่น 1
                    self.credit += 400                           # เพิ่มเครดิตของผู้เล่น
                    time.sleep(7)                                # หน่วงเวลา
                    os.system('cls')                             # ลบหน้าจอ
        else:
            print("Player 1 selected a card not in their inventory.")       # แสดงข้อความเมื่อผู้เล่น 1 เลือกการ์ดที่ไม่อยู่ใน inventory
            time.sleep(5)
            os.system('cls')
            c.main()

            
class Data(CardGame):
     def show_data(self):
          A = [['Kamado','90','SSR'],
             ['Uzumaki','80','SSR'],
             ['Kakashi','60','SR'],
             ['Genzo','60','SR'],
             ['Obi','30','SR'] ,
             ['Gintama','20','R'],
             ['Hotaki','10','R'],
             ['God','5','CM'],
             ['Devil','5','CM']]
          
          for i in A:
                print('----- Data Card -----')  # พิมพ์ข้อความหัวข้อส่วนข้อมูลการ์ด
                print('Name :',i[0])            # แสดงชื่อการ์ด
                print('Card power :',i[1])      # แสดงพลังโจมตีของการ์ด
                print('Rank :',i[2])            # แสดงระดับของการ์ด
                print('')                       # สร้างบรรทัดว่าง

a = Login()                                     # สร้างอ็อบเจกต์ a จากคลาส Login
print('--------------------')                   # พิมพ์ข้อความขั้นบรรทัด
print('') #ช่องว่าง
a.register(input('Register Username : '),       # เรียกใช้เมธอด register เพื่อลงทะเบียน
           input('Register Password : '))
print('') #ช่องว่าง
print('--------------------')
time.sleep(2) #หน่วงเวลา
os.system('cls') #ลบ terminal

print('--------------------')
print('') #ช่องว่าง
a.login(input('Login Username : '),              # เรียกใช้เมธอด login เพื่อเข้าสู่ระบบ
        input('Login Password : '))
print('') #ช่องว่าง
print('--------------------')
time.sleep(2.5) #หน่วงเวลา
os.system('cls') #ลบ terminal

c = CardGame()                                   # สร้างอ็อบเจกต์ c จากคลาส CardGame
d = Data()                                       # กำหนด d เป็นอ็อบเจกต์ของคลาส data
c.compare_cards()                                # เรียกใช้เมธอด compare_cards
c.main()                                         # เรียกใช้เมธอด main
c.random_box()                                   # เรียกใช้เมธอด random_box
d.show_data()                                    # เรียกใช้เมธอด show_data