class Graph:
    # Create and show traces
    def show_graph(self):
        self.read_file('weight_data.txt')
        
        import plotly.graph_objects as go

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=self.days, y=self.weight_data,
                            mode='lines+markers',
                            name='lines+markers'))

        fig.update_layout(title='Bulking in November 2019',
                        xaxis_title='Days in November 2019',
                        yaxis_title='Weight (kg)')

        fig.show()