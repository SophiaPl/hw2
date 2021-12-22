def inssort(nums):
    for i in range(1, len(nums)):
        k = nums[i]
        for j in range(i - 1, -1, -1):
            l = nums[j]
            if k >= l:
                break
            else:
                nums[j + 1], nums[j] = l, k
    return nums


# проверка
if __name__ == '__main__':
    l = list(map(int, input('Введите список: ').split()))
    print(*inssort(l))
