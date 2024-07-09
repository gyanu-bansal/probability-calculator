# Probability Calculator

This project is a Python script to calculate probabilities, created as part of my freeCodeCamp certification. The script uses a class to simulate a hat containing balls of different colors and calculates the probability of drawing a specific combination of balls over multiple experiments.

## How to Use

### Prerequisites

- Python 3.x installed on your system.
- No additional libraries are required.

### Running the Script

1. **Save the script** as `probability_calculator.py` or any name you prefer.
2. **Open a terminal or command prompt**.
3. **Navigate to the directory** where the script is saved.
4. **Run the script** by executing the following command:

    ```bash
    python probability_calculator.py
    ```

### Script Details

The script defines two main components: the `Hat` class and the `experiment` function.

#### Hat Class

- **Initialization (`__init__` method)**:
  - Takes any number of keyword arguments representing the colors of the balls and their respective counts.
  - Initializes the contents of the hat with the given balls.

- **Draw Method (`draw` method)**:
  - Takes an integer `num_balls` representing the number of balls to draw from the hat.
  - Returns a list of drawn balls. If the number of balls to draw exceeds the available balls, it returns all the remaining balls.

#### Experiment Function

- **Parameters**:
  - `hat`: An instance of the `Hat` class.
  - `expected_balls`: A dictionary representing the expected balls to draw and their counts.
  - `num_balls_drawn`: The number of balls to draw in each experiment.
  - `num_experiments`: The number of experiments to perform.

- **Returns**:
  - The probability of drawing the expected combination of balls over the specified number of experiments.

### Example

The following example demonstrates how to use the `Hat` class and the `experiment` function:

```python
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={"red": 2, "green": 1}, num_balls_drawn=5, num_experiments=2000)
print("Probability:", probability)
