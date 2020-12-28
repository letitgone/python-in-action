# @Author ZhangGJ
# @Date 2020/12/28 15:06

def greet_user():
    """显示简单的问候语"""
    print("Hello!")


greet_user()


def greet_user(username):
    """显示简单的问候语"""
    print(f"Hello, {username.title()}!")


greet_user("jack")


def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")


describe_pet('hamster', 'harry')
describe_pet(animal_type='hamster', pet_name='harry')


def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")


describe_pet("123")
