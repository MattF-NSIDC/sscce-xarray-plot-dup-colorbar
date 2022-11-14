import base64
from io import BytesIO

from flask import Flask, render_template

from sscce_xarray_plot_dup_colorbar.util import make_plot

app = Flask(__name__)

@app.route('/')
def index():
    fig = make_plot()

    # Convert figure to bytes for embedding
    buf = BytesIO()
    fig.savefig(buf, format='png')
    img_data = base64.b64encode(buf.getbuffer()).decode('ascii')

    return render_template('plot.html.j2', img_data=img_data)

app.run(host='0.0.0.0', port=5000, debug=True)
