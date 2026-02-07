#
import numpy as np      # Importación librería NumPy
import pandas as pd     # Importación librería Pandas
# %%
''' Lección 1 '''
# Objetivo: Crear un conjunto de datos ficticio utilizando NumPy,
# aplicando operaciones básicas para la preparación inicial.
#
# Creación de Arrays con Datos ficticios
Nombre = np.array( ['Ana', 'Juan', 'Alonso', 'Miguel', 'Luisa', 'Pedro'] )
Edad = np.array( [24, 31, 55, 43, 27, 35] )
Inversion_CLP = np.array( [2550085, 1855030, 5115350, 5550010, 7815020, 10132555] )
Ciudad = np.array( ['Linares', 'Talca', 'Temuco', 'Bulnes', 'Penco', 'Talca'] )
#
# Operaciones Matemáticas Básicas mediante NumPy
suma_inversiones = np.sum(Inversion_CLP)
print('La suma de todas las inversiones es:', suma_inversiones)
media_inversiones = np.mean(Inversion_CLP)
print('El promedio de todas las inversiones es:', media_inversiones)
#
# Convertir "arrays" a listas para usar con Pandas
Nombre_list = Nombre.tolist()
Edad_list = Edad.tolist()
Inversion_CLP_list = Inversion_CLP.tolist()
Ciudad_list = Ciudad.tolist()
#
# README #
# NumPy es eficiente para el manejo de datos numéricos porque almacena los valores
# y utiliza operaciones matemáticas predefinidas, en lugar de bucles,
# lo que permite realizar cálculos de forma mucho más rápida y eficiente.
# %%
''' Lección 2 '''
# Explorar y transformar los datos generados en "Lección 1",
# utilizando la estructura de DataFrame de Pandas.
#
# Leer los datos preparados en NumPy y convertirlos en un DataFrame
#
data = {                        # Creación Diccionario
        'Nombre': Nombre,
        'Edad': Edad,
        'Inversión CLP': Inversion_CLP,
        'Ciudad': Ciudad
        }
#
df = pd.DataFrame(data)         # Creación DataFrame
print(f'Data-Frame:\n{df}\n')
#
print('Visualización Primera fila:')
print(df.head(1))
print ("\n")
print('Visualización Última fila:')
print(df.tail(1))
print ("\n")
# Estadísticas Descriptivas
media = df['Inversión CLP'].mean()
print(f'El promedio de las Inversiones realizadas es: {media}')
mediana = df['Inversión CLP'].median()
print(f'La mediana de las Inversiones realizadas es: {mediana}')
minimo = df['Inversión CLP'].min()
print(f'El mínimo de las Inversiones realizadas es: {minimo}')
maximo = df['Inversión CLP'].max()
print(f'El máximo de las Inversiones realizadas es: {maximo}')
moda = df['Ciudad'].mode()[0]
print(f'La moda para la "Ciudad" es: {moda}')
#
# Filtro Condicional
condicion = df[(df['Edad'] <= 30) & (df['Inversión CLP'] >= 5000000)]
print(f'\nLos Clientes menores a 30 años, con inversiones mayores a 5M CLP son: \n{condicion}')
#
# Guardado de DataFrame como archivo CSV en formato limpio y legible por Excel
df.to_csv('Inversiones_Clientes.csv', sep=';', index = False)
#
# README #
# Pandas es una librería que facilita la manipulación y el análisis de datos
# mediante estructuras como DataFrames (o series indexadas) que permiten almacenar,
# filtrar, agrupar y transformar datos de manera rápida y eficiente.
# %%
''' Lección 3 '''
# Integrar datos de diversas fuentes y unificarlos
# en un solo DataFrame para su posterior limpieza.
#
df_02 = pd.read_csv('Inversiones_Clientes.csv', sep = ';')  # Lee archivo CSV con delimitador generado en "Lección 2"
print('\nEl archivo #1 importado es en resumen:')
print(df_02.head(3))
#
df_03 = pd.read_excel('clientes_ecommerce.xlsx')            # Incorporar nuevas fuentes de datos (p.ej: clientes_ecommerce.xlsx)
print('\nEl archivo #2 importado es en resumen:')
print(df_03.head())                                         # Muestra las 5 primeras filas de "clientes_ecommerce.xlsx"
#
#
DF = pd.concat([df_02, df_03], axis = 0)                    # Unifica (Concatena) archivos #1 y #2 en un único DataFrame
print(f'\nEl DataFrame concatenado (#1 con #2) es: \n {DF}')
DF.to_csv('Clientes_Varios.csv', sep = ';', index = False, encoding = 'utf-8')   # Exportación Formato limpio y legible
#
# README #
# El principal desafío fue que el DataFrame #2 es de mayor ctdad. de columnas.
# A su vez me sorprendió que a pesar de concatnenar hacia abajo "axis=0",
# el proceso de unificado reordena por sí solo los datos de ambos archivos
# que comparten el mismo nombre de columna, aunque la posición de sus columnas
# haya sido distinta originalmente en cada archivo.
# %%
''' Lección 4 '''
# Aplicar técnicas de limpieza de datos,
# resolviendo problemas de valores nulos y datos atípicos.
#
# Identificación Valores Nulos/Perdidos
#
DF_read = pd.read_csv('Clientes_Varios.csv', sep = ';')
#
valores_nulos = DF_read.isnull()                 # Genera DF de valores booleanos; True si es NULO - False si no lo es
nulos_col = DF_read.isnull().sum()               # Cuenta el número de valores nulos por columna
nulos_total = DF_read.isnull().sum().sum()       # Cuenta el número total de valores nulos en el DataFrame
#
print(f'\nDataFrame con Valores Nulos como Booleanos \n(True si es NULO - False si no lo es): \n{valores_nulos}')
print(f'\nLos valores nulos por columna son: \n{nulos_col}')
print(f'\nLos valores nulos en el DataFrame consolidado son: {nulos_total}\n')
#
# Imputación/Eliminación de Valores Nulos/Perdidos
#
DF_copia = DF.copy()                            # Creación Copia DF para modificar sin riesgos
#
DF_v2 = DF_copia.reset_index(drop=True)         # Reordenamiento índices
DF_v2["ID"] = range(1, len(DF_v2) + 1)          # Reordenamiento columna "ID"
#
DF_columnas = DF_v2.columns.tolist()            # Reordenamiento columnas
DF_columnas.insert(0, DF_columnas.pop(DF_columnas.index("ID")))
DF_v2 = DF_v2[DF_columnas]
#
DF_v2['Edad'] = (                               # Reemplaza Nulos de la columna con Valor Predefinido
                 DF_v2['Edad']
                 .fillna(30)
                )
#
DF_v2['Inversión CLP'] = (                      # Reemplazo Nulos con el promedio de la columna
                         DF_v2['Inversión CLP']
                         .fillna( DF_v2['Inversión CLP'].mean() )
                        )
#
DF_v2['Total_Compras'] = (                      # Reemplaza Nulos de la columna con Valor Predefinido
                          DF_v2['Total_Compras']
                          .fillna(5)
                         )
#
print(np.random.randint(1, 10, size=5))         # Valores enteros aleatorios
vector_nulos = DF_v2['Monto_Total'].isna()
#
min = int(DF_v2['Monto_Total'].min())           # Mínimo de la columna
max = int(DF_v2['Monto_Total'].max())           # Máximo de la columna
#
DF_v2.loc[vector_nulos, 'Monto_Total'] = np.random.randint(             # Imputación columna "Monto_Total" con enteros aleatorios
                                                           min, max + 1,
                                                           size = vector_nulos.sum()
                                                        )
#
print(f'\nEl DataFrame reordenado y arreglado es: \n {DF_v2} \n')
#
valores_nulos_v2 = DF_v2.isnull()
print(f'\nComprobación Valores Nulos en DataFrame editado \n(True si es NULO - False si no lo es): \n{valores_nulos_v2}')
#
# Detección de Outliers mediante Boxplots
import matplotlib.pyplot as plt
import seaborn as sns
#
columnas = ['Edad', 'Inversión CLP', 'Total_Compras', 'Monto_Total']
#
fig, axes = plt.subplots(2, 2, figsize=(20, 6))
axes = axes.flatten()
#
for i, col in enumerate(columnas):
    sns.boxplot(x = DF_v2[col], ax = axes[i])
    axes[i].set_title(f'Boxlpot de Valores: Columna {col}')
    axes[i].ticklabel_format(style = 'plain', axis = 'x')
#
plt.tight_layout()
plt.show()
#
DF_v2.to_csv('Clientes_Varios_v2.csv', sep = ';', index = False)        # Exportación Formato limpio y legible
#
# README #
# Se generó un reordenamiento y limpieza del DataFrame/DataSet que se generó en "Lección 3"
# Se identificaron valores nulos, y se imputaron con criterios varios para obtener datos razonables
# Se detectaron outliers mediante métodos estadísticos (IQR) y visuales (Boxplots),
# pudiendo observarse valores extremos principalmente en la columna: Inversión CLP.
# %%
''' Lección 5 '''
# Transformar y enriquecer los datos mediante técnicas
# de manipulación avanzada.
#
DF_v3 = pd.read_csv('Clientes_Varios_v2.csv', sep = ';')
#
duplicados = DF_v3.duplicated()
print(f'\nLos valores duplicados en el DataSet son: \n{duplicados}')
#
DF_v3['Total_Compras'] = DF_v3['Total_Compras'].replace({0:5})         # Reemplazo valores
DF_v3['Monto_Total']  = DF_v3['Monto_Total'].replace({0:5000})         # Reemplazo valores
#
DF_v3['Total c/IVA'] = DF_v3['Monto_Total'].apply( lambda x: x * 1.19 )     # Creación de nueva columna
# (Aplica una función a cada elemento en la columna original mediante una expresión lambda, y crea una nueva)
#
DF_v4 = DF_v3.copy()                                # Creación Copia DF para modificar sin riesgos
DF_v4 = DF_v4.drop(columns = ['Inversión CLP'])     # Eliminación columna "Inversión CLP"
#
DF_v4 = DF_v4.rename(columns = {'Total_Compras' : 'Total Compras'})     # Cambio de nombre a columna
DF_v4 = DF_v4.rename(columns = {'Monto_Total' : 'Monto Total'})         # Cambio de nombre a columna
#
print(f'\nEl DataSet nuevo es: \n{DF_v4}')
DF_v4.to_csv('Clientes_Varios_v3.csv', sep = ';', index = False)        # Exportación Formato limpio y legible
#
# %%
''' Lección 6 '''
# Organizar y estructurar los datos para el análisis
# utilizando técnicas de agrupamiento y pivotado.
#
DF_v5 = pd.read_csv('Clientes_Varios_v3.csv', sep = ';')
#
Ciudad_edad_promedio = (                                # Agrupamiento para columna "Ciudad"
                        DF_v5.groupby('Ciudad')['Edad'].mean()
                       )
print(f'\nEl promedio de la Edad para "Co-Ciudadanos" es: \n{Ciudad_edad_promedio}')
#
Nombre_compras_totales = (                              # Agrupamiento para columna "Total Compras"
                          DF_v5.groupby('Nombre').agg({'Total Compras':[np.min, np.max, np.sum]})
                         )
print(f'\nLas métricas: mínimo, máximo, nombre \npara el "Total de Compras" es: \n{Nombre_compras_totales}')
#
DF_v5_pivot = DF_v5.pivot_table(                        # Pivotar DataFrame Nombre/Ciudad para el "Total c/IVA"
                                index = 'Nombre',
                                columns = 'Ciudad',
                                values = 'Total c/IVA'
                               )
print(f'\nEl DataFrame Pivotado es: \n{DF_v5_pivot}')
#
DF_v5_melt = DF_v5_pivot.reset_index().melt(            # DataFrame Des-Pivotado (y resumido a 3 columnas)
                                            id_vars = 'Nombre',
                                            var_name = 'Ciudad',
                                            value_name = 'Total c/IVA'
                                           )
DF_v5_melt = DF_v5_melt.dropna()                        # Eliminar filas vacías/inútiles
print(f'\nEl DataFrame Des-Pivotado es: \n{DF_v5_melt}')
#
# README #
# Los valores nulos generados por el uso de pivot_table()
# corresponden a combinaciones Nombre–Ciudad inexistentes en el conjunto de datos original.
# Al aplicar melt(), los valores se mantienen y pueden eliminarse de ser necesario.
#
''' Impresión Documento Final '''
#
with pd.ExcelWriter('DataSet.xlsx') as writer:
    DF.to_excel(writer, sheet_name='DF_v1', index=False)
    DF_v2.to_excel(writer, sheet_name='DF_v2', index=False)
    DF_v3.to_excel(writer, sheet_name='DataSet_v1', index=False)
    DF_v4.to_excel(writer, sheet_name='DataSet_v2', index=False)
    DF_v5.to_excel(writer, sheet_name='DataSet_v3', index=False)
#
#

