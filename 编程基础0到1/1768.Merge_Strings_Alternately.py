class Solution(object):
    def mergeAlternately(self, word1, word2):

        # 计算两个字符串中较短的长度，用于确定交替合并的轮次
        min_length=min(len(word1),len(word2))
        word=[]

        # 循环处理两个字符串的共同长度部分，交替添加字符
        # i的取值范围是0到min_length-1，共min_length次循环
        for i in range(min_length):
            # 左闭右开区间
            word.append(word1[i])
            word.append(word2[i])

        # 处理较长字符串的剩余部分
        word.append(word1[min_length:])
        word.append(word2[min_length:])

        # 将列表连接成字符串并返回
        return ''.join(word)



if __name__ == "__main__":
    # 用列表存储所有测试用例
    test_cases = [
        ("abc", "pqr"),
        ("ab", "pqrs"),
        ("abcd", "pq")
    ]
    
    # 循环遍历测试用例并执行
    for test_x, test_y in test_cases:
        result = Solution().mergeAlternately(test_x, test_y)
        # 打印测试结果（包含输入、实际输出和预期输出）
        print(f"输入: '{test_x}', '{test_y}', 输出: '{result}'")
        print("-" * 50)  # 分隔线