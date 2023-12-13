import random

# 定义地图大小和街区大小
MAP_WIDTH = 50
MAP_HEIGHT = 50
BLOCK_SIZE_MIN = 3
BLOCK_SIZE_MAX = 7
STREET_WIDTH = 1

# 创建地图列表
map = [[0 for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)]

# 定义辅助函数

def get_random_block_size():
    """返回随机街区大小（在 BLOCK_SIZE_MIN 和 BLOCK_SIZE_MAX 之间）"""
    return random.randint(BLOCK_SIZE_MIN, BLOCK_SIZE_MAX)

def get_block_value(x, y, size):
    """为给定坐标和大小的街区生成随机值"""
    values = []
    for i in range(size):
        for j in range(size):
            value = 1 if random.random() < 0.5 else 0
            values.append(value)
    # 计算平均值并将其四舍五入为最接近的整数
    avg_value = round(sum(values) / len(values))
    return avg_value

# 生成街区
x = 0
while x < MAP_WIDTH:
    y = 0
    while y < MAP_HEIGHT:
        block_size = get_random_block_size()
        block_value = get_block_value(x, y, block_size)
        for i in range(block_size):
            for j in range(block_size):
                if x+i < MAP_WIDTH and y+j < MAP_HEIGHT:
                    map[x+i][y+j] = block_value
        y += block_size + STREET_WIDTH
    x += block_size + STREET_WIDTH

# 生成街道
for x in range(MAP_WIDTH):
    for y in range(STREET_WIDTH, MAP_HEIGHT, BLOCK_SIZE_MAX+STREET_WIDTH):
        map[x][y] = 2

for y in range(MAP_HEIGHT):
    for x in range(STREET_WIDTH, MAP_WIDTH, BLOCK_SIZE_MAX+STREET_WIDTH):
        map[x][y] = 2

# 打印地图
for row in map:
    print(" ".join(str(cell) for cell in row))