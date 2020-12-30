# @Author ZhangGJ
# @Date 2020/12/28 16:36

def print_models(unprinted_designs_1, completed_models_1):
    """模拟打印每个设计"""
    while unprinted_designs_1:
        current_design = unprinted_designs_1.pop()
        print(f"Printing model: {current_design}")
        completed_models_1.append(current_design)


def show_completed_models(completed_models_1):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models_1:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
# 传递副本
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
