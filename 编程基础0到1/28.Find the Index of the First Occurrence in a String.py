class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "": return 0  
        # 如果needle为空字符串，返回0
        needle_len = len(needle)
        # 遍历源字符串中所有可能的起始位置
        # 结束位置为 haystack_len - needle_len，确保子串不会越界
        for i in range(len(haystack) - needle_len + 1):
            # 截取源字符串中从i开始、长度为needle_len的子串
            # 与目标字符串进行比较 
            if haystack[i:i + needle_len] == needle: return i
        return -1  
    # 如果未找到，返回-1
        


if __name__ == "__main__":
    # 用列表存储所有测试用例
    test_cases = [
        ("sadbutsad", "sad"),
        ("leetcode", "leeto"),
        ("heo", "e"),
        ("hello", "ll")
    ]
    
    # 循环遍历测试用例并执行
    for test_x, test_y in test_cases:
        result = Solution().strStr(test_x, test_y)
        # 打印测试结果（包含输入、实际输出和预期输出）
        print(f"输入: '{test_x}', '{test_y}', 输出: '{result}'")
        print("-" * 50)  # 分隔线