nums = []
for i in range(3):
    prompt = float(input(f"Enter Your {i+1} numer: "))
    nums.append(prompt)

nums.sort()

for k in range(3):
    print(nums[k], end = " ")