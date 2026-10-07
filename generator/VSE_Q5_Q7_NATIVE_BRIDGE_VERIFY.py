#!/usr/bin/env python3
"""Public finite verifier for VSE-C004.

This script does not regenerate the full v38 R01 graph. It independently verifies
the published q5/q7 peripheral incidence matrix -> complex Fourier cross block ->
rank-2 bridge calculation used in the bounded public claim.
"""
import json
import math
import numpy as np

M = np.array([
    [0,1,0,1,0,0,1],
    [1,0,1,0,0,1,0],
    [1,1,1,1,1,0,1],
    [1,0,1,1,0,0,0],
    [1,0,1,1,0,0,0],
], dtype=float)

def real_fourier_basis(p):
    cols = []
    for k in range(1, (p - 1)//2 + 1):
        cols.append(np.sqrt(2/p) * np.array(
            [math.cos(2*math.pi*k*j/p) for j in range(p)]))
        cols.append(np.sqrt(2/p) * np.array(
            [math.sin(2*math.pi*k*j/p) for j in range(p)]))
    return np.column_stack(cols)

B5, B7 = real_fourier_basis(5), real_fourier_basis(7)
A = B5.T @ M @ B7

J5 = np.kron(np.eye(2), np.array([[0., -1.], [1., 0.]]))
J7 = np.kron(np.eye(3), np.array([[0., -1.], [1., 0.]]))
A_complex_linear = (A - J5 @ A @ J7) / 2

C = np.zeros((2, 3), dtype=complex)
for i in range(2):
    for j in range(3):
        b = A_complex_linear[2*i:2*i+2, 2*j:2*j+2]
        C[i,j] = (b[0,0] + b[1,1])/2 + 1j*(b[1,0] - b[0,1])/2

singular_values = np.linalg.svd(C, compute_uv=False)
result = {
    "peripheral_cross_seams": int(M.sum()),
    "real_rank_M": int(np.linalg.matrix_rank(M)),
    "complex_bridge_matrix": [
        [{"re": float(z.real), "im": float(z.imag)} for z in row] for row in C
    ],
    "complex_bridge_rank": int(np.linalg.matrix_rank(C)),
    "singular_values": [float(x) for x in singular_values],
}
result["pass"] = (
    result["peripheral_cross_seams"] == 18
    and result["real_rank_M"] == 4
    and result["complex_bridge_rank"] == 2
    and np.allclose(
        singular_values,
        [0.9385525288416152, 0.391988837759743],
        rtol=1e-12,
        atol=1e-12,
    )
)
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["pass"] else 1)
