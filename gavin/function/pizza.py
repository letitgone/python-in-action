# @Author ZhangGJ
# @Date 2020/12/28 17:13

def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers')


def make_pizza(size, *toppings):
    """打印顾客点的所有配料"""
    print(size, toppings)
