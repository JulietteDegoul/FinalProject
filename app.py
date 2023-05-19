
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Make the prediction
    prediction = model.predict(new_campaign_df)[0]

    # Render the template with the prediction result
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run()
