import turtle  #подключаем модуль черепашки

t = turtle.Turtle() # задаем переменную для отрисовки курсора, вместо прописания длинной команды
i = 0 # простая переменная для цикла рисовки квадрата

t.pensize(2) # устанавливаем размер пера( стрелочки)

t.fillcolor("green") # указываем цвет заливки

t.begin_fill() # начинаем заливку
while(i<=3): # начинаем цикл с нуля до 3(рисуем 4 стороны квадрата)
    t.right(90) #(совершаем поворт вправо)
    t.forward(100) #двигаемся вперед по указанию стрелки
    i+=1 # начисляем переменную для контроля рисовки
t.end_fill() # завершаем заливку
t.right(90) # снова поворот вправо
t.forward(50) # едем в направлении стрелки
t.left(180) # разворот влево
t.pensize(1) # уменьшаем размер
t.circle(50) # рисуем круг с диаметром 50

turtle.done() # не даем закрыться окну рисования Turtle