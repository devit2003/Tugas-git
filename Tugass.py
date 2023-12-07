import pandas as pd

data = {
    'Nama': ['Karyawan1', 'Karyawan2', 'Karyawan3'],
    'Gaji': [5000, 6000, 7000],
    'Usia': [25, 35, 28]
}

df = pd.DataFrame(data)

# df['Gaji'] = df['Gaji'] * 1.05
# print("\nSetelah peningkatan gaji 5%:\n", df, "\nRingkasan:\nGaji setiap karyawan dinaikkan 5%.")

df['Gaji'] = df.apply(lambda row: row['Gaji'] * 1.02 if row['Usia'] > 30 else row['Gaji'], axis=1)
print("\nSetelah peningkatan gaji tambahan:\n", df, "\nRingkasan:\nGaji karyawan di atas 30 tahun dinaikkan 2%.")