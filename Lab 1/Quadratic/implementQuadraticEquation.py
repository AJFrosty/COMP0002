from QuadraticEquation import QuadraticEquationSolver

quad1 = QuadraticEquationSolver(1,2,1)
quad2 = QuadraticEquationSolver(1,5,13)
quad3 = QuadraticEquationSolver(1,-5,6)

print(f"{quad1.get_solution_type()} The roots is: {quad1.solve()}")
print(f"{quad2.get_solution_type()} They are: {quad2.solve()}")
print(f"{quad3.get_solution_type()} The roots are: {quad3.solve()}")