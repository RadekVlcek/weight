class Graph():
    def __init__(self, data_file_path):
        import json

        with open(data_file_path, 'r') as file:
            records = file.read()
            self.records = json.loads(records)

    def show_graph(self, date):
        import plotly.graph_objects as go

        month, year = date[1], date[2]
        days = list(self.records[month].keys())
        weight = list(self.records[month].values())

        print('Opening graph in web browser...')

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=days, y=weight,
                            mode='lines+markers',
                            name='lines+markers'))
        fig.update_layout(title=f'{month} {year}',
                        xaxis_title=f'Day',
                        yaxis_title='Weight (kg)')
        fig.show()