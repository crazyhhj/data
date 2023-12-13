import random

# 定义地图大小和街区大小
MAP_WIDTH = 50
MAP_HEIGHT = 50
BLOCK_SIZE_MIN = 3
BLOCK_SIZE_MAX = 7
STREET_WIDTH = 1

# 定义要生成的街区数量
num_blocks = 10

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
blocks = []
while True:
    if len(blocks) < num_blocks:
        x = 0 if len(blocks) == 0 else blocks[-1][0] + blocks[-1][2] + STREET_WIDTH
        if x >= MAP_WIDTH:
            break
        y = 0
        while True:
            block_size = get_random_block_size()
            if y + block_size < MAP_HEIGHT:
                block = (x, y, block_size)
                blocks.append(block)
                for i in range(block_size):
                    for j in range(block_size):
                        if x+i < MAP_WIDTH and y+j < MAP_HEIGHT:
                            map[x+i][y+j] = get_block_value(x+i, y+j, block_size)
                y += block_size + STREET_WIDTH
                if len(blocks) == num_blocks or y >= MAP_HEIGHT:
                    break
            else:
                break
    else:
        # optimize roads based on the number of blocks
        for i in range(1, len(blocks)):
            x1 = blocks[i-1][0] + blocks[i-1][2] // 2
            y1 = blocks[i-1][1] + blocks[i-1][2] - 1
            x2 = blocks[i][0] + blocks[i][2] // 2
            y2 = blocks[i][1]
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            step_x = 1 if x1 < x2 else -1
            step_y = 1 if y1 < y2 else -1
            error = dx - dy
            length = 0
            while x1 != x2 or y1 != y2:
                map[x1][y1] = 2
                error2 = error * 2
                if error2 > -dy:
                    error -= dy
                    x1 += step_x
                if error2 < dx:
                    error += dx
                    y1 += step_y
                length += 1
            if length < BLOCK_SIZE_MAX:
                for j in range(length):
                    x = blocks[i-1][0] + blocks[i-1][2] // 2 + j * step_x
                    y = blocks[i-1][1] + blocks[i-1][2] - 1 + j * step_y
                    map[x][y] = 0
        break

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