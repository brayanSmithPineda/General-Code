"""
Collaborated closely with operations managers to analyze sales and renewal data, contributing to a 7% increase in renewal rates and a 5% uptick in overall sales performance.

1- Analizando los datos de renovaciones cada vez que se llena una renuncia o porque no se quiere seguir el cliente llena un formulario poniendo el motivo, y desistiendo de la renovación, se analiza esos datos segmentando el motivo, la mayoría de las razones eran problemas económicos, decisión del cliente y venta de vehículo, con están no podíamos hacer nada, sin embargo había una razón “Alza en la prima de renovación” donde si podíamos intervenir, para esto empezamos a llamar a todos los clientes que tenían alza en su prima significativa y le empezábamos a ofrecer un seguro que tuviera las mismas características por el mismo precio, solo que con una compañía diferente y de esa manera inicialmente logramos retener al 7% de los clientes que renunciaron, y un 90% que le habían subido la prima decidieron continuar con nosotros con esta llamada, el proyecto inicial tuvo un gran éxito que se creo un pequeño grupo piloto de retención que se encarga únicamente de llamar a los clientes que tenían alza en su prima, ahora las cifras son mucho mayores sin embargo yo ya no soy parte de ese proyecto porque continue en el equipo mas grande. Para analizar los datos emplee Python para segmentar los datos y clasificar los motivos de rechazo

2- El incremento del 5% en ventas también se logro analizando los motivos de no renovación, había una proporción de clientes a los que la compañía de seguro decidía no renovarles por diferentes circunstancias, el auto se volvió mas robable, ya no existe esa cobertura, etc. Para esos casos decidimos llamar a los clientes para volver a cotizar un seguro totalmente nuevo, a este tipo de casos los contamos como ventas nuevas
"""

"""
Step 1: Data Analysis on Renewal Rates
I conducted an in-depth analysis of the renewal data to understand the reasons behind policy non-renewals.
"""

import pandas as pd

# Load the renewal data
df = pd.read_csv('renewal_data.csv')

# Segment data based on the reason for non-renewal
reason_counts = df['non_renewal_reason'].value_counts()

# Focus on the segment where intervention is possible ('Increase in renewal premium')
target_segment = df[df['non_renewal_reason'] == 'Increase in renewal premium']

"""
Step 2: Intervention Strategy
Based on the analysis, we implemented a targeted intervention strategy for customers facing an increase in their renewal premium.
"""

# Assuming a function to contact customers and offer an alternative insurance option
def contact_customer(offer, customer_id):
    # Placeholder function to illustrate the process
    # In reality, this would involve complex logic and interaction with customer communication systems
    return True

# Apply the intervention
successful_contacts = 0
for index, row in target_segment.iterrows():
    if contact_customer('alternative insurance offer', row['customer_id']):
        successful_contacts += 1

retention_rate = successful_contacts / len(target_segment)

"""
Step 3: Analysis on Non-Renewal for Re-quoting
For the segment where the insurance company decided not to renew policies due to various risk factors, we proactively reached out to offer new quotes.
"""

# Segment customers where the company initiated non-renewal
company_initiated_non_renewals = df[df['non_renewal_initiator'] == 'company']

# Assuming a function to contact these customers for new quotes
def offer_new_quote(customer_id):
    # Similar placeholder function for customer contact
    return True

# Apply the re-quoting strategy
new_sales = 0
for index, row in company_initiated_non_renewals.iterrows():
    if offer_new_quote(row['customer_id']):
        new_sales += 1

new_sales_rate = new_sales / len(company_initiated_non_renewals)
