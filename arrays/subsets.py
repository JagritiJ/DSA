
def subarraySum(nums, k):
    count = 0
    sum_ = 0
    left = 0
    right = 0
    while right < len(nums):
        if nums[right] == k:
            count
        else:
            right += 1
            for el in range(left, right):
                sum_ += nums[el]
                if sum_ == k:
                    count += 1
                    sum_ = 0
                    left += 1

                elif sum_ < k:
                    right += 1
                else:
                    break

        return count
def main():
    nums =[1,2, 3]
    k =3
    count = subarraySum(nums, k)
    print(count)
main()