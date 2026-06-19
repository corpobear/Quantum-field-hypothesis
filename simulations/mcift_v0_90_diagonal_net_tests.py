import numpy as np

D = np.array([
    [1, 1, 1],
    [1, -1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
], dtype=float) / np.sqrt(3.0)


def q_inv(weights):
    q = np.zeros((3, 3))
    for w, d in zip(weights, D):
        q += w * np.outer(d, d)
    return 0.75 * q


def metrics(name, weights):
    q = q_inv(np.array(weights, dtype=float))
    eig = np.linalg.eigvalsh(q)
    anis = eig.max() / eig.min() - 1.0
    frob = np.linalg.norm(q - np.eye(3), ord="fro")
    det = np.linalg.det(q)
    tick = [np.inf if w <= 0 else 1.0 / np.sqrt(w) for w in weights]
    return {
        "case": name,
        "weights": weights,
        "q_inv": q,
        "eig_min": eig.min(),
        "eig_max": eig.max(),
        "anisotropy": anis,
        "frob_I": frob,
        "det": det,
        "tick_ratio_max": max(tick),
    }


if __name__ == "__main__":
    cases = [
        ("flat", [1.0, 1.0, 1.0, 1.0]),
        ("single_defect_half", [0.5, 1.0, 1.0, 1.0]),
    ]
    for name, weights in cases:
        m = metrics(name, weights)
        print(name, m)
