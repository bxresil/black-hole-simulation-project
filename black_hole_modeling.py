import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
c = 299792458    # speed of light in m/s

# Simulating black hole masses (in solar masses)
masses = np.linspace(5, 50, 100)  # from 5 to 50 solar masses
masses_kg = masses * 1.98847e30   # converting solar mass to kg

# Calculating Schwarzschild radius for each mass
schwarzschild_radii = 2 * G * masses_kg / c**2

# Simulating curvature of light (simplified)
# This is a simplistic model where the light bending angle increases with mass
light_curvature = schwarzschild_radii / (1.5e11)  # light bending near the sun, using 1 AU as a reference

# Plotting the results
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(masses, schwarzschild_radii, 'b-')
plt.title('Schwarzschild Radius vs Black Hole Mass')
plt.xlabel('Mass (Solar Masses)')
plt.ylabel('Radius (meters)')

plt.subplot(2, 1, 2)
plt.plot(masses, light_curvature, 'r-')
plt.title('Curvature of Light vs Black Hole Mass')
plt.xlabel('Mass (Solar Masses)')
plt.ylabel('Curvature of Light (radians)')

plt.tight_layout()
plt.show()
