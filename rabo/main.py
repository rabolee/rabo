import random
import time
import keyboard
import copy


monster = ['π€’','π€','π','π»','π§','π','π']

def map(): # λ³΄μ¬μ£ΌκΈ°μ© λ§΅

       a = [['β¬'] * 15 for i in range(15)]
       return a

def realMap(): # κ·Έλ¦Όμμ²λ¦¬ μ€μ  λ§΅

       rmap = [['π¨'] * 17 for i in range(17)]
       for i in range(0, 17): # λ§΅μ λμ΄κ°λ©΄ λ²½μΌλ‘ λλ¬μ£ΌκΈ°
              rmap[0][i-1] = 'β'
              rmap[i-1][0] = 'β'
              rmap[-1][i] ='β'
              rmap[i][-1] ='β'

       for i in range (0,50):
              x = random.randrange(1, 15)
              y = random.randrange(1, 15)
              rmap[x][y] = 'β' # λͺ¬μ€ν° λλ€
       while True:
              x = random.randrange(1, 15)
              y = random.randrange(1, 15)
              if rmap[x][y] == 'β':
                     continue
              rmap[x][y] = 'π' # ν¬ν λλ€
              break

       for i in range(0, 30):
              x = random.randrange(1, 15)
              y = random.randrange(1, 15)
              if rmap[x][y] == 'β' or rmap[x][y] =='π':
                     continue
              rmap[x][y] = 'β€' # ν¬μ λλ€

       return rmap

def move(): # λ§΅ νΈμΆ, μΊλ¦­ν°μ΄λ

       count = 0
       x=1
       y=1
       a = map()
       c = copy.deepcopy(a)
       b= realMap()
       a[x][y] = 'π―' # μΊλ¦­ν° μμΉ
       for i in b:  # μ½μμ μΆλ ₯
              for j in i:
                     print(j, end=" ")
              print()

       for i in a:  # μ½μμ μΆλ ₯
              for j in i:
                     print(j, end=" ")
              print()

       print(" [β μ, β ν, β μ’, β μ°] λ°©ν₯μ λλ¬ μ΄λνμΈμ")

       while True:
              if keyboard.is_pressed('right'):
                     time.sleep(0.1) # μ€λ₯Έμͺ½ μ΄λ
                     if y == 'β':
                            print('βμ€λ₯Έμͺ½μΌλ‘ μ΄λλΆκ°β')
                            continue

                     a = copy.deepcopy(c)
                     a[x][y + 1] = 'π―'
                     y += 1  # λ΄ μμΉ μ μ₯
                     a[x-1][y-1] = b[x-1][y-1] # μ’μ
                     a[x-1][y] = b[x-1][y] # μ
                     a[x - 1][y + 1] = b[x - 1][y + 1]  # μ°μ
                     a[x][y - 1] = b[x][y - 1]  # μ’
                     a[x][y +1] = b[x][y + 1] #μ°
                     a[x+1][y-1] = b[x+1][y - 1] # μ’ν
                     a[x + 1][y] = b[x+1][y]  # ν
                     a[x + 1][y + 1] = b[x + 1][y + 1]  # μ°ν
                     count += 1
                     for i in a:
                            for j in i:
                                   print(j, end=" ")
                            print()
                     print(' ')

              if keyboard.is_pressed('left'):
                     time.sleep(0.1) # μΌμͺ½ μ΄λ
                     if y == 'β':
                            print('βμΌμͺ½μΌλ‘ μ΄λλΆκ°β')
                            continue
                     a = copy.deepcopy(c)
                     a[x][y - 1] = 'π―'
                     y -= 1  # λ΄ μμΉ μ μ₯
                     a[x - 1][y - 1] = b[x - 1][y - 1]  # μ’μ
                     a[x - 1][y] = b[x - 1][y]  # μ
                     a[x - 1][y + 1] = b[x - 1][y + 1]  # μ°μ
                     a[x][y - 1] = b[x][y - 1]  # μ’
                     a[x][y + 1] = b[x][y + 1]  # μ°
                     a[x + 1][y - 1] = b[x + 1][y - 1]  # μ’ν
                     a[x + 1][y] = b[x + 1][y]  # ν
                     a[x + 1][y + 1] = b[x + 1][y + 1]  # μ°ν
                     count += 1
                     for i in a:
                            for j in i:
                                   print(j, end=" ")
                            print()
                     print(' ')

              if keyboard.is_pressed('up'):
                     time.sleep(0.1) # μμͺ½ μ΄λ
                     if x == 'β':
                            print('βμμͺ½μΌλ‘ μ΄λλΆκ°β')
                            continue
                     a = copy.deepcopy(c)
                     a[x - 1][y] = 'π―'
                     x -= 1  # λ΄ μμΉ μ μ₯
                     a[x - 1][y - 1] = b[x - 1][y - 1]  # μ’μ
                     a[x - 1][y] = b[x - 1][y]  # μ
                     a[x - 1][y + 1] = b[x - 1][y + 1]  # μ°μ
                     a[x][y - 1] = b[x][y - 1]  # μ’
                     a[x][y + 1] = b[x][y + 1]  # μ°
                     a[x + 1][y - 1] = b[x + 1][y - 1]  # μ’ν
                     a[x + 1][y] = b[x + 1][y]  # ν
                     a[x + 1][y + 1] = b[x + 1][y + 1]  # μ°ν
                     count += 1
                     for i in a:
                            for j in i:
                                   print(j, end=" ")
                            print()
                     print(' ')

              if keyboard.is_pressed('down'):
                     time.sleep(0.1) # μλμͺ½ μ΄λ
                     if x == 'β':
                            print('βμλμͺ½μΌλ‘ μ΄λλΆκ°β')
                            continue
                     a = copy.deepcopy(c)
                     a[x + 1][y] = 'π―'
                     x += 1  # λ΄ μμΉ μ μ₯
                     a[x - 1][y - 1] = b[x - 1][y - 1]  # μ’μ
                     a[x - 1][y] = b[x - 1][y]  # μ
                     a[x - 1][y + 1] = b[x - 1][y + 1]  # μ°μ
                     a[x][y - 1] = b[x][y - 1]  # μ’
                     a[x][y + 1] = b[x][y + 1]  # μ°
                     a[x + 1][y - 1] = b[x + 1][y - 1]  # μ’ν
                     a[x + 1][y] = b[x + 1][y]  # ν
                     a[x + 1][y + 1] = b[x + 1][y + 1]  # μ°ν
                     count += 1
                     for i in a:
                            for j in i:
                                   print(j, end=" ")
                            print()
                     print(' ')


def win (): # μΉλ¦¬μ
    print("""
   _   _  _____  _____  _                       
 | | | ||_   _|/  __ \| |                      
 | | | |  | |  | /  \/| |_   ___   _ __  _   _ 
 | | | |  | |  | |    | __| / _ \ | '__|| | | |
 \ \_/ / _| |_ | \__/\| |_ | (_) || |   | |_| |
  \___/  \___/  \____/ \__| \___/ |_|    \__, |
                                          __/ |
                                         |___/ 
""")
def lose (): # ν¨λ°°μ
    print("""
  _____   ___  ___  ___ _____   _____  _   _  _____ ______ 
|  __ \ / _ \ |  \/  ||  ___| |  _  || | | ||  ___|| ___ |
| |  \// /_\ \| .  . || |__   | | | || | | || |__  | |_/ /
| | __ |  _  || |\/| ||  __|  | | | || | | ||  __| |    / 
| |_\ \| | | || |  | || |___  \ \_/ /\ \_/ /| |___ | |\ \ 
 \____/\_| |_/\_|  |_/\____/   \___/  \___/ \____/ \_| \_|
 
""")

def battle_monster(): # λͺ¬μ€ν° μΆν
    rand=random.randrange(100)
    M_HP=0
    M_power=0
    M_name=0
    monster_list=['π€’ μ’λΉ','π€ κ΅¬μΈ','π ν΄κ³¨','π» λ²κ·Έλ² μ΄','π§ λνλ','π νκ±°λ¦¬','π λμλ³΅λ‘']

    if rand < 48:
        M_name = monster_list[0]
        M_HP = random.randrange(300,501)
        M_power = 100
    elif 48 <= rand < 78:
        M_name=monster_list[1]
        M_HP = random.randrange(450, 701)
        M_power = 180
    elif 78 <= rand < 90:
        M_name=monster_list[2]
        M_HP = random.randrange(480, 801)
        M_power = 220
    elif 90 <= rand < 95:
        M_name=monster_list[3]
        M_HP = random.randrange(550, 901)
        M_power = 350
    elif 95 <= rand < 97:
        M_name=monster_list[4]
        M_HP = random.randrange(3000, 8001)
        M_power = random.randrange(1000, 3001)
    elif 97 <= rand < 99:
        M_name=monster_list[5]
        M_HP = random.randrange(3000, 8001)
        M_power = random.randrange(1000, 3001)
    elif rand == 99:
        M_name=monster_list[6]
        M_HP = random.randrange(5000, 15001)
        M_power = random.randrange(2500, 8001)
    return M_name, M_HP, M_power



def user_attack (M_name, M_HP,user_power): # μ΄μ½μμ© κ³΅κ²©
    print()
    print(f'β μ΄μ½μμ© κ³΅κ²© β')
    print(f' [κ³΅κ²©λ ₯ : {user_power}]')
    M_HP -= user_power
    print(f'{M_name} λ¨μ μ²΄λ ₯ : {M_HP}')
    return M_name, M_HP

def monster_attack (M_name, M_power, user,count_Exturn): # λͺ¬μ€ν°μ μ ν¬
    if count_Exturn >=0:
        print(f'β {M_name} κ³΅κ²©β!')
        user[1] -= 0
        print(f'μ΄μ½μμ© λ¨μ μ²΄λ ₯ : ({M_power}-{user[1]})')
        print(f'ν¬μ μ {user[2]}\n')
        print(f"μλ¦­μ μ {user[3]}")
        return M_name, M_power, user
    else:
        print(f'{M_name} κ³΅κ²© β!')
        user[1] -= M_power
        print(f'μ΄μ½μμ© λ¨μ μ²΄λ ₯ : {user[1]}')
        return M_name, M_power, user

def run(): # λλ§κ°κΈ°
    rand = random.randrange(2)
    if rand == 0:
        print()
        print(f'λλ§μ±κ³΅ π³')
        print(f'λ§΅μΌλ‘ λμκ°λλ€!!!\n')
    else:
        print()
        print(f'λλ§μ€ν¨ π΄')
        print(f'μ ν¬λ³΅κ· β!\n')
    return rand

def potion(user): # ν¬μ μ¬μ©
    user[1] = user[0] #λ³νλ hpμ κΈ°λ³Έhp λμ, μ΄κΈ°ν
    if user[2] >= 1: #ν¬μκ°μκ° 1κ°μ΄μμ΄λ©΄
        print()
        print(f'β€ ν¬μμ¬μ© β€!')
        print(f'μ΄μ½μμ©HP {user[1]}λ§νΌ νλ³΅')
        user[2] -= 1     # ν¬μκ°μμ°¨κ°
        # print(f'β€ ν¬μλ¨μκ°μ: {user[2]}\n')
        return user, 1
    else :     # ν¬μμμΌλ©΄
        print()
        print(f'β€ν¬μλ¨μκ°μ: 0')
        print(f'μ ν¬λ³΅κ·!!!\n')
        return user, 0


def elixir(user): # μλ¦­μ μ¬μ©
    if user[3] > 0:  # μλ¦­μ κ°μ
        print("β¨μλ¦­μλ₯Ό μ¬μ©ν©λλ€")
        print("β¨μμΌλ‘ 10ν΄ λμ λ¬΄μ μνκ° λ©λλ€β¨")
        user[3] -= 1    # μλ¦­μ κ°μ μ°¨κ°
        return user, 10    # 10ν΄ λμ λλ¦¬κΈ° μν¨
    else:
        print("μλ¦­μκ° μμ΅λλ€")
        return user, 0

def potion_drop(user): # ν¬μ μ»κΈ°
    rand = random.randrange(2) # 50%νλ₯ λ‘ ν¬μ λ°μ.
    if rand == 0: # ν¬μλ°μ
        rand = random.uniform(0,100) #uniform 0λΆν° 100κΉμ§ μ€μ μΆλ ₯
        # print(rand)
        if rand <= 1:
            print("β¨ μλ¦­μ νλ β¨")
            user[3] += 1 # μλ¦­μ κ°μ λνκΈ°
        else :
            print("β€ ν¬μ νλ β€")
            user[2] += 1 # ν¬μ κ°μ λνκΈ°
            print(f"ν¬μ μ: {user[2]}")
    else : #ν¬μ λͺ»λ°μ
        print("βν¬μ νλ μ€ν¨β")

    return user

def test (): # μ΄μ½μμ© νμ¬μν
    user = [500, 500, 5, 5,0] # κΈ°λ³Έhp, hpλ³ν, ν¬μμ, μλ¦­μμ
    print('----' * 15)
    print("              π― μ΄μ½μμ©κ΅° νμ¬ μν π―")
    print(f"     [κΈ°λ³ΈHP:{user[0]}]  [HPλ³ν:{user[1]}]  [ν¬μμ:{user[2]}]  [μλ¦­μμ:{user[3]}]")
    print('----' * 15)
    count_Exturn = 0
    M_name, M_HP, M_power = battle_monster()
    print(f"                   {M_name} λ±μ₯")
    print(f'           {M_name} [HP {M_HP}] [κ³΅κ²©λ ₯ {M_power}]')
    print('----' * 15)

    while True:
        user_power = random.randrange(100,151)  # κ³΅κ²©λ ₯, λ¦¬μ€νΈ λ§μ§λ§μ μΆκ°λ¨
        user[4] = user_power
        if count_Exturn >=0:
            count_Exturn-=1
        choice = int(input(f"[1.β κ³΅κ²©νκΈ°]  [2.π΄β λλ§κ°κΈ°]  [3.β€ν¬μ({user[2]}κ°)]  [4.β¨μλ¦­μ({user[3]}κ°)]"))
        if choice == 1:
            M_name, M_HP = user_attack (M_name, M_HP,user_power)
            if M_HP > 0:   # HP -λλ©΄ κ³΅κ²© λͺ»ν¨
                M_name,M_power, user = monster_attack(M_name, M_power, user, count_Exturn)
        elif choice == 2:
            rand = run()
            if rand == 0:    # λλ§ μ±κ³΅
                break
            else:    # λλ§ μ€ν¨
                M_name, M_power, user = monster_attack(M_name, M_power, user,count_Exturn)
        elif choice == 3:
            succes = potion(user)    # ν¬μ μ±κ³΅
            M_name, M_power, user = monster_attack(M_name, M_power, user, count_Exturn)
        elif choice == 4:
            count_Exturn = elixir(user)[1]
            M_name, M_power, user = monster_attack(M_name, M_power, user, count_Exturn)
        else:
            print("μλͺ»λλ μ΅λλ€. λ€μ μ νν΄μ£ΌμΈμ")
            continue
        if M_HP <= 0:
            print("                                 [μ΄μ½μμ© μΉπ]")
            print(win())
            print("π₯ μ΄μ½μμ© λ λ²¨μ π₯")
            user_copy = user[:]    # HPλ³ν μ μ§νλ €κ³  λ³΅μ¬
            user_copy[4] = user_copy[4] + (user_copy[4]*0.05)    # κ³΅κ²©λ ₯ μ¦κ°
            user_copy[0] = user_copy[0] + (user_copy[0]*0.05)    # HP μ¦κ°
            user[1] = user[0]     # HP λ³ν μ΄κΈ°ν
            user = potion_drop(user)
            break
        elif user[1] <= 0:
            print("                                 [μ΄μ½μμ© ν¨π³]")
            print(lose())

            break
    return user_copy



# ----------------------------mainν¨μ μμ --------------------------------------
print(f'{monster}κ° λνλ©λλ€')
print(' ')
user = test()
print(user)
