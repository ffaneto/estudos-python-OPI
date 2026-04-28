target = 9
nums = [2,1,7,15]
result = []
tamanho = len(nums)

for i in range(tamanho - 1):
    for b in range(i + 1, tamanho):
        if nums[i] + nums[b] == target:
            result = [i,b]
            break

print(result)