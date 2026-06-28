class Solution:
    x=0.0
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        x=init
        for _ in range(iterations):
            y= x**2
            # Derivative:         f'(x) = 2x
            y1=2*x
            # Update rule:        x = x - learning_rate * f'(x)
            x = x - (learning_rate*y1)
            # Round final answer to 5 decimal places
            #round(x,4)
        return round(x,5)
        pass
