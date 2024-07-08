# Import some python packages for calculations and plotting
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter 


# Define the parameters of the simulation
a = 0.1  # Slit width in meters
L = 1.0  # Distance from slit to screen in meters
N = 10000  # Number of particles
chunk_size = 100  # Number of particles to add per frame
screen_width = 0.2  # Width of the screen in meters
num_bins = 500  # Number of bins on the screen

# Generate particle at the slit, we assume a uniform distribution that covers the slit
particles_x = np.random.uniform(-a/2, a/2, N)

# Define the screen coordinates
screen_x = np.linspace(-screen_width/2, screen_width/2, num_bins)
dx = screen_x[1] - screen_x[0]

# Here we calculate the intensity distribution using single-slit diffraction formula
# I(theta) = I0 * (sin(beta)/beta)^2, where beta = (pi * a * sin(theta)) / lambda
lambda_ = 700e-9  # Wavelength of particles in meters
theta = np.arctan(screen_x / L)
beta = (np.pi * a * np.sin(theta)) / lambda_
intensity = (np.sin(beta) / beta)**2
intensity[np.isnan(intensity)] = 1  # Handle the division by zero at beta = 0

# Here we normalize the intensity distribution
intensity /= np.sum(intensity * dx)

# Now we randomly sample particle positions on the screen based on the intensity distribution
particles_screen_x = np.random.choice(screen_x, N, p=intensity * dx)

# We generate y-coordinates for the particles to simulate the 2D screen projection
particles_screen_y = np.random.uniform(-screen_width/2, screen_width/2, N)


# Let's make the plot!
fig, ax = plt.subplots(figsize=(12, 6))
scat = ax.scatter([], [], s=1, color='red', alpha=0.6) #You can change the color and the size of the particles here
ax.set_xlim(-screen_width/2, screen_width/2)
ax.set_ylim(-screen_width/2, screen_width/2)
ax.set_ylabel('y-position on screen (m)')
ax.set_xlabel('x-position on screen (m)')
ax.set_title('Slit width w= {} m'.format(a))

# Initialize the scatter plot with no data
def init():
    scat.set_offsets([])
    return scat,

# Update function for animation
def update(frame):
    # Add the next chunk of particles to the plot
    end = frame * chunk_size
    current_data = np.column_stack((particles_screen_x[:end], particles_screen_y[:end]))
    scat.set_offsets(current_data)
    return scat,

# Create the animation
frames = N // chunk_size
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=50, repeat=False)

# Save the animation as a GIF
gif_writer = PillowWriter(fps=20)
ani.save("single_slit_diffraction_open.gif", writer=gif_writer)

# Show the plot
plt.show()
