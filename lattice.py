import numpy as np

def create_lattice(L):
    """ランダムスピンの3次元格子を生成 (+1 or -1)"""
    return np.random.choice([-1, 1], size=(L, L, L))

def get_energy(lattice):
    """周期境界条件でのハミルトニアンを計算"""
    L = lattice.shape[0]
    E = 0
    for axis in range(3):
        E -= np.sum(lattice * np.roll(lattice, 1, axis=axis))
    return E