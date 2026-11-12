from bike import Bike, ElectroBike
from client import Client
from rental_logic import RentalService
from station import Stations


def print_admin_report(stations, rental_service):
    print("Звіт")
    print(f"Загальна виручка мережі: {rental_service.total_revenue} грн")

    print("Залишки на станціях:")
    for station in stations:
        print(f"Станція {station.name}: {station.count()} велосипедів")

    print("Електровелосипеди з низьким зарядом (< 20):")
    for station in stations:
        low_bikes = station.low_charge_bikes()
        for b_numb, st_name, charge in low_bikes:
            print(f"Велосипед {b_numb}, Станція: {st_name}, Заряд: {charge}%")


def main():
    print("Демо")

    st_a = Stations("Університет")
    st_b = Stations("Вокзал")
    stations = [st_a, st_b]

    bike1 = Bike(numb="B01")
    bike2 = Bike(numb="B02")

    ebike1 = ElectroBike(numb="E01")
    ebike1.charge = 100

    ebike2 = ElectroBike(numb="E02")
    ebike2.charge = 50

    ebike_low = ElectroBike(numb="E03")
    ebike_low.charge = 15

    st_a.add_bike(bike1)
    st_a.add_bike(ebike1)
    st_a.add_bike(ebike_low)
    st_b.add_bike(bike2)
    st_b.add_bike(ebike2)

    client1 = Client(name="Оля", balance=150)
    client2 = Client(name="Іван", balance=10)

    rental = RentalService()

    print("-> Оля на Університеті, їде 20 хв і повертає на Вокзал...")
    rented_bike1 = rental.take_bike(client1, st_a)
    if rented_bike1:
        rental.return_bike(client1, rented_bike1, st_b, minutes=20)

    print("-> Іван електровелосипед на Вокзалі, їде 5 хв і повертає туди ж...")
    rented_bike2 = rental.take_bike(client2, st_b)
    if rented_bike2:
        rental.return_bike(client2, rented_bike2, st_b, minutes=5)

    print("-> Оля бере ще один електровелосипед на Університеті, їде 10 хв і повертає на Вокзал...")
    rented_bike3 = rental.take_bike(client1, st_a)
    if rented_bike3:
        rental.return_bike(client1, rented_bike3, st_b, minutes=10)

    print("-> Спроба взяти велосипед на пустій станції:")
    empty_station = Stations("Парк")
    if not rental.take_bike(client1, empty_station):
        print("Помилка: На цій станції немає вільних велосипедів.")

    print("Баланс")
    print(f"{client1.name}: {client1.balance} грн")
    print(f"{client2.name}: {client2.balance} грн")

    print_admin_report(stations, rental)


if __name__ == "__main__":
    main()