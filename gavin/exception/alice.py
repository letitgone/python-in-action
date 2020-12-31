# @Author ZhangGJ
# @Date 2020/12/31 09:52

filename = '../../resources/alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file{filename} does not exist.")
else:
    # 计算该文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
