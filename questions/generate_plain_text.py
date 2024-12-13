def generate_prompts():
    questions = [    
        {"role": "user", "content": "For the following questions, only give me the answer. Skip though process."},
        {"role": "user", "content": "In a box, there are balls that are either black or blue. You draw a ball for 100 times from the box. What is the probability that you draw at least a white ball?"},
        {"role": "user", "content": "There are two ducks in front of a duck, two ducks behind a duck and a duck in the middle. How many ducks are there?"},
        {"role": "user", "content": "Five people were eating apples, A finished before B, but behind C. D finished before E, but behind B. What was the finishing order?"},
        {"role": "user", "content": "If five cats can catch five mice in five minutes, how long will it take one cat to catch one mouse?"},
        {"role": "user", "content": "A bad guy is playing Russian roulette with a six-shooter revolver. He puts in one bullet, spins the chambers and fires at you, but no bullet comes out. He gives you the choice of whether or not he should spin the chambers again before firing a second time. Should he spin again?"},

        {"role": "user", "content": "What is the converse negative proposition of the statement:\" Dogs love sausages. \" "},
        {"role": "user", "content": "What is the converse negative proposition of the statement:\" If it does not love sausages, then it is not dog. \" "},

        {"role": "user", "content": "A girl meets a lion and unicorn in the forest. The lion lies every Monday, Tuesday and Wednesday and the other days he speaks the truth. The unicorn lies on Thursdays, Fridays and Saturdays, and the other days of the week he speaks the truth. “Yesterday I was lying,” the lion told the girl. “So was I,” said the unicorn. What day is it?"},
        {"role": "user", "content": "You are given three doors to choose from, one of which contains a car and the other two contain goats. After you've chosen one but haven't opened it, Monty, who knows where everything is, reveals the location of a goat from behind one of the other two doors. Should you stick with your original choice or switch, if you want the car?"},
        {"role": "user", "content": "A teacher writes six words on a board: “cat dog has max dim tag.” She gives three students, Albert, Bernard and Cheryl each a piece of paper with one letter from one of the words. Then she asks, “Albert, do you know the word?” Albert immediately replies yes. She asks, “Bernard, do you know the word?” He thinks for a moment and replies yes. Then she asks Cheryl the same question. She thinks and then replies yes. What is the word?"},
        
        {"role": "user", "content": "The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other. Given an integer n, return the number of distinct solutions. Give me the answer when n = 7"},
        {"role": "user", "content": "The n-queens puzzle is the problem of placing n queens on an 8 x 8 chessboard such that no two queens attack each other. Given an integer n, return the number of distinct solutions. Give me the answer when n = 7"},
    ]
    return questions