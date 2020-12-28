# @Author ZhangGJ
# @Date 2020/12/28 15:58

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
