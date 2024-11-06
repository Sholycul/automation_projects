num_list = input("Enter five numbers: ").split()

num = [int(n) for n in num_list]

print(max(num))