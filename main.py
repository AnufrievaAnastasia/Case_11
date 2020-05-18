class Information:
    ''''''

    def __init__(self, line):
        line_main = line.split(' ')
        self.line_main = line_main
        self.booking_date = line_main[0]
        self.last_name = line_main[1]
        self.first_name = line_main[2]
        self.middle_name = line_main[3]
        self.number_pers = line_main[4]
        self.date = line_main[5]
        self.number_days = line_main[6]
        self.max_price = int(line_main[7])

    def __str__(self):
        s = '--------------------------------------------------------------------------------------' + '\n'
        s += 'Поступила заявка на бронирование:' + '\n'
        s += '{} {} {} {} {} {} {} {}'.format(self.booking_date, self.last_name, self.first_name, self.middle_name,
                                              self.number_pers, self.date, self.number_days, self.max_price) + '\n'
        s += 'Найден:' + '\n'

        return s

    def __repr__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.booking_date, self.last_name, self.first_name, self.middle_name,
                                                self.number_pers, self.date, self.number_days, self.max_price)


class Room:
    ''''''

    price_type_room = {'одноместный': 2900, 'двухместный': 2300, 'полулюкс': 3200, 'люкс': 4100}
    comfort = {'стандарт': 1, 'стандарт_улучшенный': 1.2, 'апартамент': 1.5}

    def __init__(self, line, occupancy = 'Свободно', place = '0'):
        line_main = line.split(' ')
        self.room = line_main[0]
        self.type = line_main[1]
        self.people = line_main[2]
        self.comfort = line_main[3][:len(line_main[3]) - 1]
        self.price = Room.price_type_room[self.type] * Room.comfort[self.comfort]
        self.food = 'Без питания'
        self.occupancy = occupancy
        self.place = place

    def update(self):
        if self.occupancy != 'Свободно':
            return 'Свободных варинатов нет'
        elif self.place != 0:
            return 'Занят на ' + str(self.place) + 'суток'


    def __str__(self):
        s = '{} {} {} {} {} {} {}'.format(self.room, self.type, self.people, self.comfort,
                                             self.price, self.food, self.occupancy)
        return s

    def __repr__(self):
        return '{} {} {} {} {} {} {}'.format(self.room, self.type, self.people, self.comfort,
                                             self.price, self.food, self.occupancy)


customers = []
with open('booking.txt', 'r') as booking:
    for line in booking.readlines():
        customer = Information(line)
        customers.append(customer)
print(customers)

hotel = []

with open('fund.txt', 'r') as fund:
    for line_2 in fund.readlines():
        room = Room(line_2)
        hotel.append(room)
    print(hotel)

for customer in customers:
    for room in hotel:
        if int(customer.max_price) >= int(room.price) and int(customer.number_pers) == int(room.people) and \
                room.occupancy == 'Свободно':
            print(customer, 'номер {} {} расчитан на {} человека фактически {} человек стоимость {} руб./сутки '.format
            (room.room, room.type, room.people, customer.number_pers,room.price))
            room.occupancy = 'Занято'

#дописать метод который зависит от времени, то есть параметр занято/свободно меняется после определенной даты