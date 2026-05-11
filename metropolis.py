import numpy as np

def metropolis_step(lattice, T):
    """メトロポリス法で1スピンをフリップ"""
    L = lattice.shape[0]
    i, j, k = np.random.randint(0, L, 3)
    
    # 隣接スピンの和（周期境界）
    neighbors = (
        lattice[(i+1)%L, j, k] + lattice[(i-1)%L, j, k] +
        lattice[i, (j+1)%L, k] + lattice[i, (j-1)%L, k] +
        lattice[i, j, (k+1)%L] + lattice[i, j, (k-1)%L]
    )
    
    dE = 2 * lattice[i, j, k] * neighbors
    
    if dE < 0 or np.random.rand() < np.exp(-dE / T):
        lattice[i, j, k] *= -1
    
    return lattice