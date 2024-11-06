from flask import Flask, render_template, request, redirect, url_for
import apod
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def home():
    # Get APOD for today
    apod_data = apod.get_apod()
    if apod_data:
        return render_template('index.html', apod=apod_data, today=datetime.today().strftime('%Y-%m-%d'))
    else:
        return "Error fetching APOD data"


@app.route('/history', methods=['GET', 'POST'])
def history():
    if request.method == 'POST':
        date = request.form['date']
        if apod.validate_date(date):
            apod_data = apod.get_apod(date)
            if apod_data:
                return render_template('history.html', apod=apod_data, date=date)
            else:
                return "Error fetching APOD data for the selected date"
        else:
            return "Invalid date. Please choose a date between June 16, 1995, and today."

    return render_template('history.html')


if __name__ == '__main__':
    app.run(debug=True)
