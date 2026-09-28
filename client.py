"""Truncated Singular Value Decomposition (SVD).
100% Python Standard Library.
"""

import math

class TruncatedSVD:
    """Power iteration Truncated SVD computing top k singular triplets."""

    @staticmethod
    def power_svd(A: list, k: int = 1, iterations: int = 50) -> tuple:
        m = len(A)
        n = len(A[0])
        A_curr = [row[:] for row in A]
        U = []
        S = []
        V = []

        for _ in range(k):
            v = [1.0 / math.sqrt(n)] * n
            for _ in range(iterations):
                u = [sum(A_curr[i][j] * v[j] for j in range(n)) for i in range(m)]
                u_norm = math.sqrt(sum(x * x for x in u))
                if u_norm > 1e-12:
                    u = [x / u_norm for x in u]
                v = [sum(A_curr[i][j] * u[i] for i in range(m)) for j in range(n)]
                v_norm = math.sqrt(sum(x * x for x in v))
                if v_norm > 1e-12:
                    v = [x / v_norm for x in v]
            sigma = v_norm
            U.append(u)
            S.append(sigma)
            V.append(v)
            for i in range(m):
                for j in range(n):
                    A_curr[i][j] -= sigma * u[i] * v[j]

        return U, S, V
