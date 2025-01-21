"""
Aumente el recupero general en 12%, paso de 43% a 55% en un lapso de 4 meses, esto lo logre automatizando tareas rutinarias a aumentar la productividad del equipo lo que permitió que pudieran gestionar sus clientes mejor y por lo tanto aumentar el recupero. También genere reportes para el equipo de cobranza que ayudaron a tomar mejores decisiones

1-Se saco el porcentaje de respuesta y de recupero por cada medio de comunicación y se descubrió que la secuencia de WhatsApp era la mas efectiva era la mas efectiva una vez el cliente estaba morosa, seguida de un Email y por último el SMS

2- Integración de TOKU con la base de datos de clientes de cobranza para mitigar errores y eliminar la tarea manual de estar subiendo las bases de cobros todos lo días

3-Dashboard con la cantidad de la catera de clientes de cada ejecutivo, con esto ellos podían visualizar el estado de la póliza y del pago de cada uno de sus clientes, cuanto tiempo llevaban morosos, y el monto que debían, con esto ellos podían entender y tener una foto bien clara de como iba su cartera individual y llevar un seguimiento a sus clientes, esto aumento significativamente la productividad

"""

"""
Step 1: Communication Channel Effectiveness Analysis
The first task involved analyzing the effectiveness of various communication channels (WhatsApp, Email, SMS) in the collections process.
"""
import pandas as pd

# Load the data
df = pd.read_csv('communication_data.csv')

# Calculate recovery rates by communication channel
recovery_rates = df.groupby('communication_channel')['recovery_rate'].mean()

# Identify the most effective sequence
print("Recovery rates by channel:")
print(recovery_rates)

"""
Step 2: Automating Data Integration with TOKU
While I can't provide the exact API interaction code without more details, the process would involve using the TOKU API to automatically send messages based on the data from our collections database. This eliminated the need for manual uploads, reducing errors and saving time
"""

"""
Step 3: Dashboard Creation for Collections Monitoring
I developed a dashboard to provide a clear view of each collection executive's portfolio, including policy status, payment status, delinquency duration, and outstanding amounts
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# Assume df is the DataFrame with all the necessary collections data

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='executive-dropdown',
        options=[{'label': name, 'value': name} for name in df['executive'].unique()],
        value=df['executive'].unique()[0]
    ),
    dcc.Graph(id='portfolio-overview'),
])

@app.callback(
    Output('portfolio-overview', 'figure'),
    [Input('executive-dropdown', 'value')]
)
def update_graph(selected_executive):
    filtered_df = df[df['executive'] == selected_executive]
    traces = []
    traces.append(go.Bar(x=filtered_df['customer'], y=filtered_df['amount_due'], name='Amount Due'))
    
    return {
        'data': traces,
        'layout': go.Layout(title=f'Portfolio Overview for {selected_executive}', xaxis={'title': 'Customer'}, yaxis={'title': 'Amount Due'})
    }

if __name__ == '__main__':
    app.run_server(debug=True)
