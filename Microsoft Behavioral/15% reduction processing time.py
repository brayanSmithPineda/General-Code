"""
Cleaned and transformed auto insurance sales data using Python, leading to a 15% reduction in processing time (Limpieza y transformación de datos de ventas CICO llevando a una reducción del 15% en el tiempo de procesamiento)

1- Cuando recién me uní al equipo de operaciones de Colombia el equipo de ventas tenia un reto y era el largo tiempo que tomaba procesar la información relacionada con la venta ( Tipo de seguro, información del cliente, valor póliza, información compañía, canal venta, fechas), lo que impactaba la capacidad de tomar decisiones rápidas y mirar el comportamiento del área. Para mejorar esto use Python, Pandas para manipular los datos y Numpy para operaciones, limpiar y transformar los datos. 

El proceso de limpiado incluía quitar registros duplicados, Valores no existentes, errores en los datos, variables categóricas. Una vez teniendo los datos limpios construíamos métricas, nuevas columnas y gráficos para mirar que tal le estaba yendo al área. Este proceso se hacía todo en Excel y después de la implementación con Python el tiempo se redujo drásticamente. Como resultado no solo redujimos los tiempos sino que obtuvimos una vista mas limpia, estructura y precisa  de lo que estaba pasando en el área diariamente
"""

"""
Step 1: Data Cleaning
The initial task involved cleaning the data, which was crucial to ensure accuracy and reliability for subsequent analysis and processing.
"""
import pandas as pd
import numpy as np

# Load the sales data
df = pd.read_csv('auto_insurance_sales_data.csv')

# Remove duplicate records
df.drop_duplicates(inplace=True)

# Fill in missing values or drop rows/columns with missing values
df.fillna(method='ffill', inplace=True)  # Forward fill to propagate last valid observation forward
# or df.dropna(inplace=True) to remove rows with missing values

# Correcting errors in data (e.g., fixing data entry mistakes)
df['policy_value'] = np.where(df['policy_value'] < 0, np.abs(df['policy_value']), df['policy_value'])

# Convert categorical variables using one-hot encoding
df = pd.get_dummies(df, columns=['insurance_type', 'sales_channel'])

"""
Step 2: Data Transformation
After cleaning, I transformed the data to make it more conducive to analysis, building metrics and new columns that would provide insights into the sales area's performance.
"""

# Creating new columns for analysis
df['sale_month'] = pd.to_datetime(df['sale_date']).dt.month
df['customer_age_group'] = pd.cut(df['customer_age'], bins=[18, 30, 45, 60, 75, 90], labels=['18-30', '31-45', '46-60', '61-75', '76-90'])

# Generating summary metrics for each sales channel
sales_summary = df.groupby('sales_channel').agg({'policy_value': ['mean', 'sum'], 'customer_id': 'count'}).reset_index()
sales_summary.columns = ['sales_channel', 'average_policy_value', 'total_policy_value', 'customer_count']

"""
Step 3: Visualization and Reporting
With the data cleaned and transformed, I utilized Python to create visualizations and reports that were previously done manually in Excel, significantly speeding up the process.
"""
import matplotlib.pyplot as plt

# Plotting the average policy value by sales channel
plt.figure(figsize=(10, 6))
sales_summary.plot(kind='bar', x='sales_channel', y='average_policy_value', title='Average Policy Value by Sales Channel')
plt.show()
