from flask import Flask, request, render_template
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_pen_size')
def calculate_pen_size():
    chicken_count = int(request.args.get('chickenCount'))

    # The recommended square feet per chicken without nesting boxes
    recommended_size_without_boxes = 10

    # Additional square feet per nesting box
    box_size = 2

    # Calculate the number of nesting boxes needed
    nesting_boxes = math.ceil(chicken_count / 4)

    # Calculate the total square feet required for chickens and nesting boxes
    total_size = chicken_count * recommended_size_without_boxes + nesting_boxes * box_size

    # Round up the total size to the nearest whole number
    pen_size = math.ceil(total_size)

    return str(pen_size)

if __name__ == '__main__':
    app.run()
