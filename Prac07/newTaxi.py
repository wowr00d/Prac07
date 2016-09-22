from Prac07.test_taxi import Taxi, UnreliableCar
def main():
    badCar = UnreliableCar("Bad Car", 100)
    if badCar.drive(distance=30):
        print("works fine")
    else:
        print("it didnt work")
    print(badCar)


    Prius1 = Taxi("Prius1",100)
    Prius1.drive(40)
    print(Prius1)
    print("Fare costs $",Prius1.get_fare())

    Prius1.start_fare()
    Prius1.drive(100)
    print(Prius1)
    print("Fare costs $",Prius1.get_fare())

main()

