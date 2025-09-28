#==================================================================
# DATE: 2025-09-17
# AUTHOR: CiMorn
#==================================================================


#==================================================================
# 方法二：先把非0的数放到新数组里，最后补0,但是LeetCode会报错
#==================================================================
class Solution(object):
    def moveZeroes(self, nums):
        for num in nums:
            if num==0:
                continue
            else:
                move_nums.append(num)
        move_nums=move_nums+[0]*(len(nums)-len(move_nums))
        return move_nums


#==================================================================
# 方法一：先把非0的数放到新数组里，最后补0,但是LeetCode会报错
#==================================================================
class Solution(object):
    def moveZeroes(self, nums):
        move_nums=[]
        for num in nums:
            if num==0:
                continue
            else:
                move_nums.append(num)
        move_nums=move_nums+[0]*(len(nums)-len(move_nums))
        return move_nums

        


if __name__ == "__main__":
    # 用列表存储所有测试用例
    test_cases = [
        ([0,1,0,3,12]),
        ([0])
    ]
    
    print("-" * 50)  # 分隔线
    # 循环遍历测试用例并执行
    for test_x in test_cases:
        print(f"输入: '{test_x}'")
        result = Solution().moveZeroes(test_x)
        # 打印测试结果（包含输入、实际输出和预期输出）
        print(f"输出: '{result}'")
        print("-" * 50)  # 分隔线