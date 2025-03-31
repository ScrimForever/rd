def multiply_matrices(A, B):
    # Make transponse to easily access columns of B
    B_Transponse = list(zip(*B))

    return [
        [sum(a * b for a, b in zip(row_a, col_b)) for col_b in B_Transponse]
        for row_a in A
    ]
