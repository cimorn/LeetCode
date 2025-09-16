
#=====================================================================
# 方法三: 通过判断出现个数是否相等，来判断是否为变位词
#=====================================================================
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t): return False
        for char in set(t):
            if s.count(char)!=t.count(char):
                return False
        return True



#=====================================================================
# 方法一：转化成ASCII码值，排序后比较
#=====================================================================
# class Solution(object):
#     def isAnagram(self, s, t):
#     # 初始化ASCII码值
#         ascii_s, ascii_t = [], []

#         for char in t: ascii_t.append(ord(char))
#         for char in s: ascii_s.append(ord(char))
      
#         return sorted(ascii_s)==sorted(ascii_t)


#=====================================================================
# 方法二（失败）：用字典统计每个字符出现的次数，然后比较两个字典是否相等
#=====================================================================
# 特例 "ggii" "eekk"
# 转化成ascii码值后，求和不一定对的
#=====================================================================
# class Solution(object):
#     def isAnagram(self, s, t):
#     # 初始化ASCII码值
#         ascii_s = 0
#         ascii_t = 0

#         for char in t: ascii_s += ord(char)  
#         # 累加t中每个字符的ASCII码值
#         for char in s: ascii_t += ord(char)  
#         # 减去s中每个字符的ASCII码值
        
#         return ascii_s==ascii_t

if __name__ == "__main__":
    # 用列表存储所有测试用例
    test_cases = [
        ("anagram", "nagaram"),
        ("rat", "car"),
        ("ggii", "eekk")
    ]
    
    # 循环遍历测试用例并执行
    for test_x, test_y in test_cases:
        result = Solution().isAnagram(test_x, test_y)
        # 打印测试结果（包含输入、实际输出和预期输出）
        print(f"输入: '{test_x}', '{test_y}', 输出: '{result}'")
        print("-" * 50)  # 分隔线