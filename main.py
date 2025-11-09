def has_duplicates(lst):
    """判断列表中是否存在重复元素，存在则返回True，否则返回False"""
    # 利用集合的特性（元素唯一），比较列表长度和集合长度
    return len(lst) != len(set(lst))


# 测试程序
if __name__ == "__main__":
    # 定义测试用例
    test_cases = [
        [1, 2, 3, 4, 5],          # 无重复元素
        [1, 2, 3, 2, 4],          # 有重复元素
        ["a", "b", "c", "a"],     # 字符串重复
        [],                       # 空列表
        [10],                     # 单元素列表
        [5, 5, 5, 5],             # 全重复元素
        [1, "1", 2, "2"]          # 不同类型元素（不视为重复）
    ]
    
    # 执行测试并输出结果
    for i, case in enumerate(test_cases, 1):
        result = has_duplicates(case)
        print(f"测试用例 {i}: {case}")
        print(f"是否存在重复元素: {result}\n")
