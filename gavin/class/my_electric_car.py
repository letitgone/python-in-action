# @Author ZhangGJ
# @Date 2020/12/30 16:50

from electric_car import ElectricCar

my_tesla = ElectricCar('tesla', 'model', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
