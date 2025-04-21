import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Function to simulate orbit based on given initial conditions
def simulate_orbit(initial_conditions, full_output=False):
    """
    This function simulates the orbit of an object in space given initial conditions.

    Parameters:
    initial_conditions (dict): Dictionary containing orbital parameters like semi-major axis and eccentricity.
        - 'semi_major_axis': The semi-major axis (in AU).
        - 'eccentricity': The eccentricity of the orbit (dimensionless).
    full_output (bool): Whether to return full results (True) or summary (False).

    Returns:
    dict: The orbital result including time, position, and velocity vectors.
    """
    # Constants
    mu = 1.0  # Gravitational parameter (AU^3/day^2)
    a = initial_conditions['semi_major_axis']  # Semi-major axis in AU
    e = initial_conditions['eccentricity']     # Eccentricity (dimensionless)

    # Define the system of equations for orbital motion
    def orbit_eq(t, y):
        x, vx, y_pos, vy = y
        r = np.sqrt(x**2 + y_pos**2)
        ax = -mu * x / r**3
        ay = -mu * y_pos / r**3
        return [vx, ax, vy, ay]

    # Initial state: [position, velocity] (initially at periapsis)
    initial_state = [a * (1 - e), 0.0, 0.0, np.sqrt(mu / a)]  # Periapsis, with the corresponding velocity

    # Time span for the simulation: 1 year (365 days)
    t_span = (0, 365)
    t_eval = np.linspace(*t_span, 1000)  # 1000 time points for smooth plotting

    # Run the ODE solver (solve_ivp) to integrate the orbit equation
    sol = solve_ivp(orbit_eq, t_span, initial_state, t_eval=t_eval)

    # Prepare the result based on user preference (summary or full output)
    if full_output:
        return {
            'time': sol.t,  # Full time data
            'position': sol.y[:2],  # Full position data
            'velocity': sol.y[2:],  # Full velocity data
            'eccentricity': e  # Use initial eccentricity as the result
        }
    else:
        # Return a summary with only first 5 points of data
        return {
            'time': sol.t[:5],  # First 5 time points
            'position': sol.y[:2][:, :5],  # First 5 position values
            'velocity': sol.y[2:][:, :5],  # First 5 velocity values
            'eccentricity': e  # Use initial eccentricity as the result
        }

# Function to classify the type of orbit based on eccentricity
def classify_orbit(result):
    """
    Classifies the orbit type based on the calculated orbital eccentricity.

    Parameters:
    result (dict): Dictionary containing the orbital data, including position and velocity.

    Returns:
    str: The type of orbit (e.g., 'Circular', 'Elliptical', 'Parabolic', etc.).
    """
    e = result['eccentricity']
    
    if e < 0.1:
        return "Circular Orbit"
    elif 0.1 <= e < 0.5:
        return "Elliptical Orbit"
    elif 0.5 <= e < 1:
        return "Hyperbolic Orbit"
    else:
        return "Parabolic Orbit"

# Function to plot the orbit based on the simulation results
def plot_orbit(result):
    """
    This function visualizes the orbit using matplotlib, showing the object's path in space.

    Parameters:
    result (dict): Dictionary containing the orbital data, including position at each time step.
    """
    # Extract position data
    x = result['position'][0]  # x positions
    y = result['position'][1]  # y positions
    
    # Plot the orbit
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label="Orbit Path")
    plt.scatter([0], [0], color="red", label="Star/Planet", s=100)  # The center (Sun/Planet)
    plt.title("Orbital Path")
    plt.xlabel("X Position (AU)")
    plt.ylabel("Y Position (AU)")
    plt.legend()
    plt.grid(True)
    plt.show()