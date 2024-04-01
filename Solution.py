import matplotlib.pyplot as plt

# Function to solve a polynomial expression2
def solve_polynomial(coefficients, x):
    result = 0
    for i in range(len(coefficients)):
        result += coefficients[i] * (x ** (len(coefficients) - i - 1))
    return result

# Read problems from the text file
with open("c:/Users/PERSONAL/Documents/BSCS/codes/2ND SEM/DATA STRUCTURE/problems.txt", "r", encoding="utf-8") as file:
    problems = file.readlines()

solutions = []

# Solve each problem for x from 1 to 50
for problem in problems:
    problem = problem.strip()
    if problem.startswith("x"):
        problem = "1" + problem
    coefficients = []
    for term in problem.split('+'):
        term = term.strip()
        if term.isdigit() or term.startswith('-'):
            coefficients.append(int(term))
        else:
            coefficients.append(1)
    solutions_for_x = []
    for x in range(1, 51):
        solutions_for_x.append(solve_polynomial(coefficients, x))
    solutions.append(solutions_for_x)

# Plot the solutions of all given problems
def plot_all_problems():
    for i in range(len(solutions)):
        plt.plot(range(1, 51), solutions[i], label=f"Problem {i+1}")
    plt.xlabel('x')
    plt.ylabel('Solution')
    plt.title('Solutions to the Given Problems')
    plt.legend()
    plt.show()

# Plot the solution of a specific problem chosen by the user
def plot_specific_problem(problem_number):
    if 1 <= problem_number <= len(solutions):
        plt.plot(range(1, 51), solutions[problem_number - 1])
        plt.xlabel('x')
        plt.ylabel('Solution')
        plt.title(f'Solution to Problem {problem_number}')
        plt.show()
    else:
        print("Invalid problem number. Please choose a number within the range.")

# Function to display all given problems with numbers
def display_problems():
    print("List of Available Problems:")
    for i in range(len(problems)):
        print(f"{i+1}. {problems[i].strip()}")

# Ask the user what action they want to perform
while True:
    print("Choose an action:")
    print("1. Plot all given problems")
    print("2. Plot a specific problem")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        plot_all_problems()
    elif choice == '2':
        display_problems()  # Display all available problems with numbers
        problem_number = int(input("Enter the number of the problem.: "))
        plot_specific_problem(problem_number)
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")