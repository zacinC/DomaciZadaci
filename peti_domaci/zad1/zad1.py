from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


def function_loop():
    while True:
        key = input("Input 'y' to continue and 'n' to exit the program: ")
        if key == 'y' or key == 'n':
            return key
        else:
            continue


dataset = pd.read_csv('DomaciZadaci/peti_domaci/zad1/hepatitis.csv')
data = dataset[['ALB', 'ALP', 'ALT', 'AST', 'BIL',
                'CHE', 'CHOL', 'CREA', 'GGT', 'PROT']].values
# print(data)

while True:
    program = input(
        """
Choose an option:
1. Find min and max value
2. Calculate average value
3. Percentage difference between average and max value
4. Normalize values
5. Max Positice and Negative Corelation
6. Standard Deviation
7. Exit
""")
    if int(program) == 1:
        column_number = input("Input the column number (0 based): ")
        column_data = data[:, int(column_number)]

        max_value = np.nanmax(column_data)
        min_value = np.nanmin(column_data)

        print("Maximum value for column {}: {}".format(column_number, max_value))
        print("Minimum value for column {}: {}".format(column_number, min_value))
        key = function_loop()
        if key == 'y':
            continue
        else:
            break
    elif int(program) == 2:
        column_number = input("Input the column number (0 based): ")
        column_data = data[:, int(column_number)]
        average_value = np.nanmean(column_data)

        print("Average value for column {}: {}".format(
            column_number, average_value))
        key = function_loop()
        if key == 'y':
            continue
        else:
            break
    elif int(program) == 3:
        column_number = input("Input the column number (0 based): ")
        column_data = data[:, int(column_number)]

        max_value = np.nanmax(column_data)
        average_value = np.nanmean(column_data)
        percentage_diff = abs((max_value - average_value))/100

        print("Percentage difference between max and average value for column {}: {}".format(
            column_number, percentage_diff))
        key = function_loop()
        if key == 'y':
            continue
        else:
            break
    elif int(program) == 4:
        column_number = int(input("Unesite broj kolone (počevši od 0): "))
        column_name = dataset.columns[column_number]

        # Izdvajanje odabrane kolone
        column_data = dataset.iloc[:, column_number]

        # Min-Max normalizacija
        min_value = column_data.min()
        max_value = column_data.max()
        normalized_column = (column_data - min_value) / (max_value - min_value)

        # Ažuriranje CSV datoteke s normaliziranom kolonom
        dataset[column_name] = normalized_column

        # Čuvanje ažurirane datoteke
        updated_file_path = 'DomaciZadaci/peti_domaci/zad1/hepatitis_normalized.csv'
        dataset.to_csv(updated_file_path, index=False)

        print(
            f"Normalizirane vrijednosti za kolonu '{column_name}' su spremljene u '{updated_file_path}'.")

        key = function_loop()
        if key == 'y':
            continue
        else:
            break
    elif int(program) == 5:
        dataset = pd.read_csv('DomaciZadaci/peti_domaci/zad1/hepatitis.csv')
        numeric_columns = dataset.select_dtypes(include=['float64', 'int64'])
        # Izračunavanje matrice korelacije
        correlation_matrix = numeric_columns.corr()

        # Pronalaženje dviju kolona s najvećom pozitivnom korelacijom (osim dijagonale)
        max_positive_correlation = correlation_matrix.unstack().sort_values(
            ascending=False)[correlation_matrix.shape[0]:][0]
        max_positive_corr_columns = correlation_matrix.columns[(
            correlation_matrix == max_positive_correlation).any()]

        # Pronalaženje dviju kolona s najvećom negativnom korelacijom
        max_negative_correlation = correlation_matrix.unstack().sort_values()[
            0]
        max_negative_corr_columns = correlation_matrix.columns[(
            correlation_matrix == max_negative_correlation).any()]

        print("Dvije kolone s najvećom pozitivnom korelacijom:")
        print(max_positive_corr_columns)
        print("Vrijednost korelacije:", max_positive_correlation)

        print("\nDvije kolone s najvećom negativnom korelacijom:")
        print(max_negative_corr_columns)
        print("Vrijednost korelacije:", max_negative_correlation)
        key = function_loop()
        if key == 'y':
            continue
        else:
            break
    elif int(program) == 6:
        numeric_columns = dataset.select_dtypes(include=['float64', 'int64'])

        # Izračunavanje standardne devijacije za svaku kolonu
        std_dev = numeric_columns.std()

        # Prikazivanje raspodjele vrijednosti za svaku numeričku kolonu
        for column in numeric_columns.columns:
            plt.figure(figsize=(8, 6))
            plt.hist(numeric_columns[column], bins=20,
                     color='skyblue', edgecolor='black', density=True)
            plt.title(f'Raspodjela vrijednosti u koloni {column}', fontsize=16)
            plt.xlabel('Vrijednost', fontsize=14)
            plt.ylabel('Relativna frekvencija', fontsize=14)
            plt.grid(True)
            plt.show()

            print(
                f'Standardna devijacija za kolonu {column}: {std_dev[column]}')
        key = function_loop()
        if key == 'y':
            continue
        else:
            break
    elif int(program) == 7:
        break
    else:
        print("You must choose one of the listed options!")
