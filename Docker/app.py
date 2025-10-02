from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize result to None
    result = None
    
    # Check if the form was submitted (POST request)
    if request.method == 'POST':
        try:
            # 1. Get numbers from the form fields by their 'name' attribute
            num1_str = request.form.get('number_one')
            num2_str = request.form.get('number_two')
            
            # 2. Convert to integers (or floats if you want decimals)
            num1 = int(num1_str)
            num2 = int(num2_str)
            
            # 3. Perform the calculation
            result = num1 * num2
            
        except ValueError:
            # Handle cases where input is not a valid number
            result = "Error: Please enter valid integers."
            
    # Render the HTML template, passing the result to display
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)