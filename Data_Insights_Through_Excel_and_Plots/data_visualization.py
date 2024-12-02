import pandas as pd
import plotly.express as px

class DataVisualization:

    def __init__(self):
        laptops_file = "EcomData/laptops_data.xlsx"
        tablets_file = "EcomData/tablets_data.xlsx"
        phones_file = "EcomData/phones_data.xlsx"
        self.laptops_df = pd.read_excel(laptops_file)
        self.tablets_df = pd.read_excel(tablets_file)
        self.phones_df = pd.read_excel(phones_file)

    def scatter_plot_for_laptops(self):    
        # Create a scatter plot for laptops data
        laptop_fig = px.scatter(
            self.laptops_df,
            x='Product',
            y='Price',
            hover_data=['Product', 'Price', 'Description', 'Rating', 'Reviews'],
        )

        laptop_fig.update_traces(
            marker=dict(
                size=12,
                color='blue',
                opacity=0.6,
                line=dict(width=2, color='DarkSlateGrey')
            )
        )

        laptop_fig.update_layout(
            title=dict(text="Laptops Scatter Plot", font=dict(size=20, family='Arial'), x=0.5),
            xaxis_title="Brands",
            yaxis_title="Price (USD)",
            font=dict(size=14),
            plot_bgcolor='lavender',
            paper_bgcolor='ghostwhite',
            margin=dict(l=50, r=50, t=50, b=50),
            legend=dict(
                title='Legend',
                font=dict(size=12),
                bgcolor='rgba(255,255,255,0.8)',
                bordercolor='Black',
                borderwidth=1
            ),
        )

        laptop_fig.show()

    def scatter_plot_for_tablets(self):
        # Create a scatter plot for tablets data
        tablet_fig = px.scatter(
            self.tablets_df,
            x='Product',
            y='Price',
            hover_data=['Product', 'Price', 'Description', 'Rating', 'Reviews'],
        )

        tablet_fig.update_traces(
            marker=dict(
                size=12,
                color='green',
                opacity=0.6,
                line=dict(width=2, color='DarkSlateGrey')
            )
        )

        tablet_fig.update_layout(
            title=dict(text="Tablets Scatter Plot", font=dict(size=20, family='Arial'), x=0.5),
            xaxis_title="Brands",
            yaxis_title="Price (USD)",
            font=dict(size=14),
            plot_bgcolor='lavender',
            paper_bgcolor='ghostwhite',
            margin=dict(l=50, r=50, t=50, b=50),
            legend=dict(
                title='Legend',
                font=dict(size=12),
                bgcolor='rgba(255,255,255,0.8)',
                bordercolor='Black',
                borderwidth=1
            ),
        )

        tablet_fig.show()

    def scatter_plot_for_phones(self):
        # Create a scatter plot for phones data
        phone_fig = px.scatter(
            self.phones_df,
            x='Product',
            y='Price',
            hover_data=['Product', 'Price', 'Description', 'Rating', 'Reviews'],
        )

        phone_fig.update_traces(
            marker=dict(
                size=12,
                color='red',
                opacity=0.6,
                line=dict(width=2, color='DarkSlateGrey')
            )
        )

        phone_fig.update_layout(
            title=dict(text="Phones Scatter Plot", font=dict(size=20, family='Arial'), x=0.5),
            xaxis_title="Brands",
            yaxis_title="Price (USD)",
            font=dict(size=14),
            plot_bgcolor='lavender',
            paper_bgcolor='ghostwhite',
            margin=dict(l=50, r=50, t=50, b=50),
            legend=dict(
                title='Legend',
                font=dict(size=12),
                bgcolor='rgba(255,255,255,0.8)',
                bordercolor='Black',
                borderwidth=1
            )
        )

        phone_fig.show()

    def run(self):
        self.scatter_plot_for_laptops()
        self.scatter_plot_for_tablets()
        self.scatter_plot_for_phones()

if __name__ == '__main__':
    visualize = DataVisualization()
    visualize.run()