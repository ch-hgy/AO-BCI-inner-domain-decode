import random

def generate_indices(length1, length2, x=None):
    '''
    生成不重复的随机索引，且索引值不超过 length2-1
    
    Args:
        length1 (int): 索引范围上限（生成的索引在 [0, length1-1] 之间）
        length2 (int): 要生成的索引数量，且索引值不超过 length2-1
        x (int, optional): 随机种子，用于固定随机结果。默认为 None（不固定）
    
    Returns:
        list: 包含 length2 个不重复的随机索引的列表
    
    Raises:
        TypeError: 如果输入不是整数
        ValueError: 如果输入不合法（如 length2 > length1 或 length1 < length2）
    '''
    # 检查输入是否为整数
    if not (isinstance(length1, int) and isinstance(length2, int)):
        raise TypeError("length1 and length2 must be integers")
    
    # 检查输入是否为正整数
    if length1 <= 0 or length2 <= 0:
        raise ValueError("length1 and length2 must be positive integers")
    
    # 检查 length2 是否超过 length1
    if length2 > length1:
        raise ValueError("length2 cannot be greater than length1")
    
    # 检查 length1 是否足够大（确保索引值不超过 length2-1）
    if length1 < length2:
        raise ValueError("length1 must be >= length2 to ensure indices <= length2-1")
    
    # 设置随机种子（如果提供了 x）
    if x is not None:
        random.seed(x)
    
    # 生成不重复的随机索引（范围 0 到 length2-1）
    indices = random.sample(range(length2), length2)
    
    return indices

def remove_indices(length1, indice_y):
    '''
    从length1中删除indice_y中的元素
    '''
    indice_x = [i for i in range(length1)]
    return [i for i in indice_x if i not in indice_y]