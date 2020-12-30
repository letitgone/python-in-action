# @Author ZhangGJ
# @Date 2020/12/28 23:11

from pizza import make_pizza
import person
from gavin import function as fu
from formatted_name import get_formatted_name as name
from greeter import *

print(make_pizza('test'))
print(person.build_person('test1', 'test2'))
print(fu.person)
print(name('test1', 'test2'))
print(get_formatted_name('test1', 'test2'))
