import random

# 创建两个账户列表
accounts1 = list(range(1, 151))
accounts2 = list(range(151, 301))

# 随机打乱两个列表
random.shuffle(accounts1)
random.shuffle(accounts2)

# 创建一个用来存储分组结果的列表
groups = []

# 当两个列表中任何一个还有元素时
while accounts1 or accounts2:
    # 随机确定新组的大小
    group_size = random.randint(4, 7)

    group = []
    for _ in range(group_size):
        # 确保一组中的账户不会全部来自同一部分
        if len(group) == 0:
            # 第一个元素随机从两个列表中取
            if accounts1 and accounts2:
                group.append(accounts1.pop() if random.random() < 0.5 else accounts2.pop())
            elif accounts1:
                group.append(accounts1.pop())
            else:
                group.append(accounts2.pop())
        else:
            # 非第一个元素尝试均衡从两个列表中取
            if group[0] <= 150:
                if accounts2:
                    group.append(accounts2.pop())
                elif accounts1:
                    group.append(accounts1.pop())
            else:
                if accounts1:
                    group.append(accounts1.pop())
                elif accounts2:
                    group.append(accounts2.pop())

    groups.append(group)

# 打印分组结果
for i, group in enumerate(groups):
    print(f"Group {i+1}: {group}")
