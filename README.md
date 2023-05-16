# Chicken-pen-nesting-calc



---

# Chicken Pen Size Calculator

The Chicken Pen Size Calculator is a web application that helps you calculate the recommended size of a chicken pen based on the number of chickens and the addition of nesting boxes. This calculator provides an estimate of the required square footage for the chickens to ensure they have enough space to move and lay eggs comfortably.

## HTML Code

The HTML code (`index.html`) contains the structure and user interface for the web application. It consists of a form where the user can input the number of chickens they have. Upon submitting the form, the JavaScript code sends a request to the server to calculate the pen size. The result is then displayed on the page.

## Python Code

The Python code (`app.py`) is built using the Flask web framework. It handles the server-side processing of the application. When the server receives a request to calculate the pen size, it extracts the number of chickens from the query parameters and performs the necessary calculations. The calculated pen size is then returned as a response to the client.

### Dependencies

The Python code requires the Flask framework to be installed. You can install it by running the following command:

```
pip install flask
```

### Running the Application

To run the Chicken Pen Size Calculator:

1. Make sure you have Python installed on your system.
2. Install Flask by running `pip install flask` in your terminal.
3. Save the HTML code as `index.html` and the Python code as `app.py`.
4. Open a terminal or command prompt and navigate to the directory where the files are saved.
5. Run the command `python app.py` to start the server.
6. Open your web browser and go to `http://localhost:5000` to access the Chicken Pen Size Calculator.

### Usage

1. Enter the number of chickens you have in the input field.
2. Click the "Calculate" button.
3. The recommended pen size will be displayed below, taking into account the number of chickens and the addition of nesting boxes.

---

