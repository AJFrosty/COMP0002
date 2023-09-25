from QuadraticEquation import QuadraticEquationSolver

quad1 = QuadraticEquationSolver(4,20,25)
quad2 = QuadraticEquationSolver(1,5,13)
quad3 = QuadraticEquationSolver(1,-5,6)

print(f"{quad1.get_solution_type()}", end=" ")
quad1.solve()
print(f"{quad2.get_solution_type()}", end=" ")
quad2.solve()
print(f"{quad3.get_solution_type()}", end=" ")
quad3.solve()