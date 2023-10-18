def fill_chessboard():
    n = 8  # Ukuran papan catur 8x8
    x=1
    chessboard = []
    for i in range(n):
        row = []
        for j in range(n):
                row.append(f"{x}")
                x=x*2
        chessboard.append(row)
    for row in chessboard:
        print(" ".join(row))
fill_chessboard()