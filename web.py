from flask import Flask, render_template, request, jsonify
import plotly.express as px
import plotly.io as pio
import pandas as pd
import openai
import ai

openai.api_key = "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"

app = Flask(__name__)

# Sample data (keep your existing data and plot functions as they are)
POPULATION_DATA = pd.DataFrame({
    'Year': [2010, 2012, 2014, 2016, 2018, 2020],
    'Tiger Population': [1400, 1700, 2000, 2200, 2300, 2500]
})

# Plotly chart functions
def create_population_chart():
    fig = px.line(
        POPULATION_DATA,
        x='Year',
        y='Tiger Population',
        title='Bengal Tiger Population Trends',
        labels={'Tiger Population': 'Number of Tigers'}
    )
    return pio.to_html(fig, full_html=False)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/dashboard.html', methods=['GET'])
def dashboard():
    # Get the tiger's name from the query string (default to 'Anonymous Tiger' if not provided)
    tiger_name = request.args.get('tiger_name', 'Anonymous Tiger')
    

    # Render the dashboard with the tiger name and other relevant data
    return render_template(
        'dashboard.html',
        tiger_name=tiger_name,
    )

# New route to handle AI questions
@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '')
    if not question:
        return jsonify({'error': 'No question provided.'}), 400

    # Use the AI module to get a response
    answer = ai.prompt(question)

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
