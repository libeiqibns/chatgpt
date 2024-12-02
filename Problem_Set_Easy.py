# Problem Set for GPT API Testing
problems_easy_dict = {
    "Arithmetic": [
        "Calculate the sum of 123 and 456.",
        "Subtract 205 from 789.",
        "Multiply 14 by 15.",
        "Divide 180 by 12.",
        "What is 25 percent of 200?",
    ],
    "Algebra": [
        "Solve for x: 2x + 6 = 14.",
        "If 5y - 3 = 2, what is y?",
        "Simplify the expression: 3(a - 4) + 4a.",
        "Solve for z: 3z - 2(z - 4) = 18.",
        "If x + y = 12 and x - y = 4, find x and y in the form [x , y].",
    ],
    "Linear Algebra": [
        "What is the determinant of a 2x2 matrix [[1, 2], [3, 4]]?",
        "Given the vector [7, 3], find its magnitude to 3 decimal places.",
        "What is the result of multiplying the matrix [[1, 2], [3, 4]] by the vector [1, 1]? Represent the result in the same format as provided here.",
        "Find the transpose of the matrix [[1, 2], [3, 4], [5, 6]] and represent in the same format as provided here.",
        "Solve the system of linear equations x + 2y = 3 and 3x + y = 5 (Keep in fractions and in the form [ , ]).",
    ],
    "Geometry": [
        "What is the area of a rectangle with length 8 cm and width 3 cm?",
        "Calculate the perimeter of a triangle with sides 3 cm, 4 cm, and 5 cm.",
        "What is the area of a circle with radius 5 cm? (Use π = 3.14)",
        "Find the volume of a cube with side length 4 cm.",
        "What is the circumference of a circle with diameter 10 cm? (Use π = 3.14)",
    ],
    "Probability and Statistics": [
        "If a die is rolled, what is the probability of getting a number greater than 4 as a fraction? Represent it in the form x/y.",
        "What is the mean of the following numbers: 5, 10, 15, 20, 25?",
        "Find the mode of the dataset [1, 2, 2, 3, 4, 4, 4, 5].",
        "Calculate the standard deviation of the set [2, 4, 4, 4, 5, 5, 7, 9].",
        "If you flip a fair coin three times, what is the probability of getting at least two heads?",
    ],
    "Trigonometry": [
        "What is the sine of 30 degrees? (Use sin(π/6))",
        "Calculate the cosine of 60 degrees. (Use cos(π/3))",
        "What is the tangent of 45 degrees? (Use tan(π/4))",
        "Find the secant of 30 degrees upto 3 decimal places. (Use sec(π/6))",
        "Calculate the cotangent of 60 degrees upto 3 decimal places. (Use cot(π/3))",
    ],
    "Calculus": [
        "Find the derivative of the function f(x) = 3x^2 + 5x + 2.",
        "Calculate the integral of the function f(x) = x^2 + 2x + 1 from x=0 to x=1. Keep it as a fraction.",
        "What is the limit of (2x^2 - x - 1) as x approaches 2?",
        "Integrate the function f(x) = 3x from x=0 to x=4.",
        "Differentiate the function f(x) = x^3 - 3x + 2.",
    ],
    "Miscellaneous (Combined)": [
        "If you invest $100 with an annual interest rate of 5%, compounded annually, what will be the amount after 1 year?",
        "Convert the angle 90 degrees to radians upto 3 decimal places.",
        "If 5 machines take 5 hours to make 5 widgets, how long would it take 100 machines to make 100 widgets?",
        "What is the area of a hexagon with a side length of 6 cm? (Use the formula: (3 * sqrt(3) / 2) * s^2) upto 2 decimal places",
        "What is the binary equivalent of the decimal number 31 using 6 bits?",
    ],
}

correct_answers_dict = {
    "Arithmetic": [
        "579",
        "584",
        "210",
        "15",
        "50",
    ],
    "Algebra": [
        "4",
        "1",
        "7a - 12",
        "10",
        "[8, 4]",
    ],
    "Linear Algebra": [
        "-2",
        "7.616",
        "[3, 7]",
        "[[1, 3, 5], [2, 4, 6]]",
        "[7/5, 4/5]",
    ],
    "Geometry": [
        "24",
        "12",
        "78.5",
        "64",
        "31.4",
    ],
    "Probability and Statistics": [
        "1/3",
        "15",
        "4",
        "2",
        "0.5",
    ],
    "Trigonometry": [
        "0.5",
        "0.5",
        "1",
        "1.155",
        "0.577",
    ],
    "Calculus": [
        "6x + 5",
        "7/3",
        "5",
        "24",
        "3x^2 - 3",
    ],
    "Miscellaneous (Combined)": [
        "105",
        "1.571",
        "5",
        "93.53",
        "011111",
    ],
}

# Print all problems for review
for category, questions in problems_easy_dict.items():
    print(f"Category: {category}")
    for question in questions:
        print(f" - {question}")
