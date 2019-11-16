class Graph():
    def __init__(self, data_file_path):
        import json

        with open(data_file_path, 'r') as file:
            records = file.read()
            self.records = json.loads(records)

    def show_graph(self):
        import plotly.graph_objects as go

        month = self.get_date()[1]
        days = list(self.records[month].keys())
        weight = list(self.records[month].values())

        print('Opening graph in web browser...')

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=days, y=weight,
                            mode='lines+markers',
                            name='lines+markers'))
        fig.update_layout(title=f'{month} {self.get_date()[2]}',
                        xaxis_title=f'Days',
                        yaxis_title='Weight (kg)')
        fig.show()