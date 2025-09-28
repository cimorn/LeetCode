class Solution(object):
    def findTheDifference(self, s, t):
    # 初始化ASCII码差值（t的和 - s的和）
        ascii_diff = 0

        for char in t: ascii_diff += ord(char)  
        # 累加t中每个字符的ASCII码值
        for char in s: ascii_diff -= ord(char)  
        # 减去s中每个字符的ASCII码值
        
        return chr(ascii_diff)  # 将差值转换回字符并返回

    # ====================================================================
    # 逐步替换
    # def findTheDifference(self, s, t):
    #     # 遍历字符串t中的每个字符
    #     for char in t:
    #         # 检查当前字符是否存在于s中
    #         if char in s:
    #             # 若存在，则从s中移除该字符（只移除一个，避免重复字符误删）
    #             # replace的第三个参数1表示只替换一次
    #             s = s.replace(char, "", 1)
    #         else:
    #             # 若不存在，说明该字符就是t比s多出的字符，直接返回
    #             return char
    # ====================================================================


    # ====================================================================
    # 这种方式只能用于s是t顺序的，不是随机的
    # def findTheDifference(self, s, t):
    #     return t.replace(s, "",1)
    #     # 把s中的替换掉，1是替换1次，剩下的就是多出来的那个字符
    # ====================================================================


if __name__ == "__main__":
    # 用列表存储所有测试用例
    test_cases = [
        ("abcd", "abcde"),
        ("", "y"),
        ("a", "aa"),
        ("aa", "aaa")     
    ]
    
    # 循环遍历测试用例并执行
    for test_x, test_y in test_cases:
        result = Solution().findTheDifference(test_x, test_y)
        # 打印测试结果（包含输入、实际输出和预期输出）
        print(f"输入: '{test_x}', '{test_y}', 输出: '{result}'")
        print("-" * 50)  # 分隔线