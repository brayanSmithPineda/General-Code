"""
1-	improve the on-time payment rate by 10%
o	Envié un mensaje automático SMS 3 días antes del vencimiento de la cuota para recordar al cliente su fecha limite de pago y no entrar en mora, utilice TOKU para enviar el mensaje masivo
o	Analizando los datos me dí cuenta que podía hacer una clasificación de los clientes que fueran mas propensos a entrar en mora, una gran parte era clientes eran personas de la tercera edad, ellos pagaban sin embargo después que recibían el primer mensaje de cobranza, así que por eso sabía que tenían el dinero, mi suposición era que olvidaban su fecha de pago, así que por esa razón empecé a enviar el SMS
o	Otro hallazgo importante es que la mayoría de clientes que no pagaban a tiempo era aquellos que no tenia inscrito un medio de pago automático, sino que todos los meses manualmente debían pagar por webpay, así que empecé a hacer una campaña para empezar a cambiar a esos clientes a medio de pago automático.
"""

"""
Step 1: Data Preprocessing
First, I needed to clean and prepare the data for analysis. This involved handling missing values, encoding categorical variables, and normalizing the data.
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Load the dataset
df = pd.read_csv('customer_payments.csv')

# Fill missing values
df.fillna(method='ffill', inplace=True)

# Encode categorical variables
label_encoder = LabelEncoder()
df['customer_segment'] = label_encoder.fit_transform(df['customer_segment'])

# Normalize numerical features
scaler = MinMaxScaler()
df['age'] = scaler.fit_transform(df[['age']])

"""
Step 2: Customer Segmentation Analysis
I performed an analysis to identify customer segments more prone to late payments. For this, I might have used a simple classification model or clustering to segment the customers.
"""
from sklearn.cluster import KMeans

# Selecting relevant features for clustering
features = df[['age', 'payment_history', 'customer_segment']]

# Applying K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=0).fit(features)
df['cluster'] = kmeans.labels_

"""
Step 3: Identifying Patterns
Using the clusters and additional analysis, I identified patterns, such as the elderly being more prone to late payments and the impact of non-automated payment methods
"""

# Analyzing the clusters
for cluster in df['cluster'].unique():
    cluster_data = df[df['cluster'] == cluster]
    print(f"Cluster {cluster}:")
    print(cluster_data.describe())
    
# Identifying customers without automated payment methods
non_auto_payment_customers = df[df['payment_method'] != 'automatic']
