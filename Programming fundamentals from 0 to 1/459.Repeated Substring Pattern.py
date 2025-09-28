

#=====================================================================
# 方法二:  s= Y Y Y Y, 2s= Y Y Y Y Y Y Y Y, (2s)[1:-1]= Y Y Y Y Y Y 中间可以找到s
# s= Y Y' Y Y, 2s= Y Y' Y Y Y Y' Y Y, (2s)[1:-1]= Y' Y Y Y Y' Y 中间找不到s
#=====================================================================
class Solution(object):
    def repeatedSubstringPattern(self, s):
        return (s+s)[1:-1].find(s)!=-1


#=====================================================================
# 方法一（失败）: 通过判断字符出现的次数是否相等来判断 ababab
#=====================================================================
# class Solution(object):
#     def repeatedSubstringPattern(self, s):
#         if len(s)<=1: return False
#         for char in set(s):
#             if s.count(s[0])!=s.count(char):
#                 return False
#         return True


if __name__ == "__main__":
    # 用列表存储所有测试用例
    test_cases = [
        ("abab"),
        ("aba"),
        ("abcabcabcabc"),
        ("ababba"),
        ("ababab"),
        ("aaa")
    ]
    
    # 循环遍历测试用例并执行
    for test_x in test_cases:
        result = Solution().repeatedSubstringPattern(test_x)
        # 打印测试结果（包含输入、实际输出和预期输出）
        print(f"输入: '{test_x}', 输出: '{result}'")
        print("-" * 50)  # 分隔线