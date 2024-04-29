field=[['-']*3 for _ in range(3)] #три раза повторяем '-' в столбец, затем в строку
def show_field(f): #создаем функцию для вывода таблицы
      print('  0 1 2') #для вывода горизонтали
      for i in range(len(field)): #len-длина
            print(str(i),*field[i]) #выводим строку и распаковываем
show_field(field)

def user_input(f): #функция для ввода значений
      while True: #нужно для того, чтобы сделать перебор введенных значений
            place=input('Введите координаты : ').split() #split делит список значений, который вводим
            if len(place)!=2: #если длина введенных значений не равно 2, то выведет подсказку ниже
                  print('Введите две координаты')
                  continue #продолжает пока не найдет нужное значение
            if not(place[0].isdigit() and place[1].isdigit()): #если оба из возможных значений не числа, выведет подсказку
                  print('Введите числа')
                  continue #продолжает пока не найдет нужное значение
            x,y=map(int,place) #задаем условие, что числа болжны быть больше или равны 0, но меньше 3
            if not(x>=0 and x<3 and y>=0 and y<3):
                  print('Вышли из диапазона')
                  continue  # продолжает пока не найдет нужное значение
            if f[x][y]!='-': #условие чтоб в заполненную клетку не вводилось новое значение
                  print('Клетка занята')
                  continue  # продолжает пока не найдет нужное значение
            break #останавливает цикл как только найдет
      return x,y #выводим результат в память
user_input(field)

def win1(f, user):
      def chek(a1,a2,a3,user):
            if a1==user and a2==user and a3==user: #при условии что все значения одинаковы (или все х или все 0)
                  return True
      for n in range(3): #перебираем всевозможные комбинации
            if chek(f[n][0], f[n][1], f[n][2], user) or \
                    chek(f[0][n], f[1][n], f[2][n], user) or \
                    chek(f[0][0], f[1][1], f[2][2], user) or \
                    chek(f[2][0], f[1][1], f[0][2], user):
                  return True
            return False


count=0 #начало каунт
while True:
      if count%2==0: #если каунт четное, то х
            user='x'
      else:
            user='0'
      show_field(field)
      x,y=user_input(field)
      field[x][y]=user
      if count==9: #когда достигнет 9 ходов, игра окончена
            print('Ничья')
      if win1(field,user):
            print(f"Выиграл {user}")
            show_field(field)
            break
      count+=1 #прибавляется шаг плюс 1

