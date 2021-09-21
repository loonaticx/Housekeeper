sizes = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]  # po2 sizes


def get_closest(y):
    """ Return the closest power of 2 in either direction"""
    return min(sizes, key=lambda x: abs(x - y))
    
x = get_closest(1600)
print(x)