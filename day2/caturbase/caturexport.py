import pandas as pd
import zipfile

def fill_chessboard():
    n = 8  # Ukuran papan catur
    x = 1
    chessboard = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(f"{x}")
            x = x * 2
        chessboard.append(row)

    for i, row in enumerate(chessboard):
        row_total = sum(map(int, row))
        row.append(str(row_total))
        chessboard[i] = row
    column_totals = [sum(int(row[i]) for row in chessboard) for i in range(n)]

    # Menambahkan baris terakhir dengan total per kolom
    last_row = [str(total) for total in column_totals]
    chessboard.append(last_row)


    return chessboard

chessboard_data = fill_chessboard()

chessboard_df = pd.DataFrame(chessboard_data)
chessboard_df = chessboard_df.rename({chessboard_df.index[-1]: 'Total'})
chessboard_df.rename(columns={chessboard_df.columns[-1]: 'Total'}, inplace=True)
print(chessboard_df)

chessboard_df.to_excel("tugascatur_fayyad.xlsx")


#membuat zip
zip_filename = "Tugas_Fayyad.zip"

files_to_zip = ["tugascatur_fayyad.xlsx", "caturexport.py", "catursendemail.py"]

with zipfile.ZipFile(zip_filename, "w") as zipf:
    for file in files_to_zip:
        zipf.write(file)