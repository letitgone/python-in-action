# @Author ZhangGJ
# @Date 2020/12/29 22:44
from car import Car


class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=75):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size} kw/h battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 75:
            mile_range = 206
        elif self.battery_size == 100:
            mile_range = 315

        print(f"This car can go about {mile_range} miles on a full charge.")


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性
        再初始化电动车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    # def describe_battery(self):
    #     """打印一条描述电瓶容量的消息"""
    #     print(f"This car has a {self.battery_size} kw/h battery.")


my_tesla = ElectricCar("tesla", 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

my_tesla.battery.get_range()
