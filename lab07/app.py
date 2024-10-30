from flask import Flask, render_template, request
import segno
import base64
import io

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    qrcode_data = None
    message = None

    if request.method == 'POST':
        # Get user input from form
        message = request.form['data']

        # Generate QR code
        qr = segno.make(message)

        # Save QR code to a binary buffer
        buffer = io.BytesIO()
        qr.save(buffer, kind='png', scale=10, border=10)

        # Encode to base64 for HTML embedding
        qrcode_data = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return render_template('index.html', qrcode_data=qrcode_data, message=message)


if __name__ == '__main__':
    app.run(debug=True)
