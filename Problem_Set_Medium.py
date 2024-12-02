# Problem Set for GPT API Testing Medium Level
problems_medium_dict = {
    "Arithmetic": [
        "Multiply 123 by 789 and add 456 to the result.",
        "Divide 5000 by 25 and subtract 40 from the quotient.",
        "Calculate the square of 75.",
        "Find the greatest common divisor (GCD) of 120 and 45.",
        "Convert 345 from decimal to hexadecimal.",
    ],
    "Algebra": [
        "Solve for x in the equation 2x + 5 = 21.",
        "Simplify the expression (2x - 3)(x + 4). No brackets in the final answer.",
        "If 3x - 7 = 5x + 1, find the value of x.",
        "Expand (x + 2)^2.",
        "Factorize x^2 - 9. Give the answer in the form ()().",
    ],
    "Linear Algebra": [
        "Find the determinant of the matrix [[2, 3], [1, 4]].",
        "Solve the system of equations: 3x + 4y = 5 and 2x - y = 1. Give the results in fractions (of the form a/b and no '' or '{}' in the answer) and in the form [ , ]",
        "Calculate the dot product of vectors u = [1, 2] and v = [3, 4].",
        "Find the magnitude of the vector u = [3, 4].",
        "Determine the inverse of the matrix [[1, 2], [3, 4]] if it exists. Please represent the final answer in the same form as provided here.",
    ],
    "Geometry": [
        "Calculate the area of a rectangle with length 15 cm and width 10 cm.",
        "Find the circumference of a circle with radius 7 cm (pi approx 3.14).",
        "Calculate the area of a triangle with base 10 cm and height 5 cm.",
        "What is the volume of a rectangular prism with dimensions 3 cm, 4 cm, and 5 cm?",
        "Determine the smallest angle of a right triangle with hypotenuse 13 cm and one leg 5 cm to 2 decimal places.",
    ],
    "Probability and Statistics": [
        "A die is rolled; find the probability of rolling a number greater than 6.",
        "Calculate the mean of the dataset [4, 8, 15, 16, 23, 42].",
        "Find the mode of the numbers [2, 3, 4, 4, 5, 5, 5, 6].",
        "A bag contains 3 red, 4 blue, and 5 green balls. What is the probability of picking a green ball in fraction of the form a/b (no bracket and slash)?",
        "Calculate the standard deviation for the dataset [3, 7, 7, 19, 25] upto 2 decimal places.",
    ],
    "Trigonometry": [
        "Calculate sin(30 degrees).",
        "Find the value of cos(60 degrees) + sin(30 degrees).",
        "Determine the length of the side opposite of a 45 degrees angle in a right triangle with hypotenuse 10 cm upto 2 decimal places.",
        "What is tan(45 degrees) + 5907?",
        "Calculate the angle in degrees for sin^-1(0.5).",
    ],
    "Calculus": [
        "Find the derivative of f(x) = 3x^2 + 5x - 2.",
        "Integrate f(x) = x - 1 from x = 0 to x = 3.",
        "Determine the limit of (x^2 - 4)/(x - 2) as x approaches 2.",
        "Evaluate the definite integral from 1 to 3 of (2x^3 - x + 1) dx.",
        "Find the second derivative of f(x) = x^3 - 6x^2 + 11x - 6.",
    ],
    "Miscellaneous (Combined)": [
        "If a light bulb has a 0.001 probability of failing in any given hour, what is the probability it will not fail in 1000 hours upto 3 decimal places?",
        "Convert 300 degrees to radians upto 3 decimal places.",
        "Using Euler's formula, express e^(iπ) + 1.",
        "Calculate the sum of the infinite series 1 + 1/2 + 1/4 + 1/8 + ...",
        "What is the hexadecimal equivalent of the binary number 110101101?",
    ],
}


correct_answers_dict = {
    "Arithmetic": [
        "97503",
        "160",
        "5625",
        "15",
        "159",
    ],
    "Algebra": [
        "8",
        "2x^2 + 5x - 12",
        "-4",
        "x^2 + 4x + 4",
        "(x - 3)(x + 3)",
    ],
    "Linear Algebra": [
        "5",
        "[9/11, 7/11]",
        "11",
        "5",
        "[[-2, 1], [1.5, -0.5]]",
    ],
    "Geometry": [
        "150",
        "43.96",
        "25",
        "60",
        "22.62",
    ],
    "Probability and Statistics": [
        "0",
        "18",
        "5",
        "5/12",
        "8.35",
    ],
    "Trigonometry": [
        "0.5",
        "1",
        "7.07",
        "5908",
        "30",
    ],
    "Calculus": [
        "6x + 5",
        "1.5",
        "4",
        "38",
        "6x - 12",
    ],
    "Miscellaneous (Combined)": [
        "0.368",
        "5.236",
        "0",
        "2",
        "1AD",
    ],
}

# Print all problems for review
for category, questions in problems_medium_dict.items():
    print(f"Category: {category}")
    for question in questions:
        print(f" - {question}")
