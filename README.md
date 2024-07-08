# Single Slit Diffraction Simulation

This script simulates the diffraction pattern produced by particles passing through a single slit.

## Overview

The simulation uses the single-slit diffraction formula to calculate the intensity distribution on a screen placed at a distance `L` from the slit. Particles are initially generated at the slit with a uniform distribution and their positions on the screen are determined based on the intensity distribution.

## Parameters

- `a`: Slit width in meters.
- `L`: Distance from slit to screen in meters.
- `N`: Number of particles.
- `chunk_size`: Number of particles added per animation frame.
- `screen_width`: Width of the screen in meters.
- `num_bins`: Number of bins on the screen for intensity calculation.
- `lambda_`: Wavelength of particles in meters.

## Installation and Usage

1. **Dependencies**: Ensure you have Python 3 installed with the following packages:
   - `numpy`
   - `matplotlib`

2. **Running the Script**:
   - Clone the repository.
   - Navigate to the directory containing `single_slit_diffraction.py`.
   - Run `python single_slit_diffraction.py`.
   - The script will generate an animation showing the particle distribution on the screen.

3. **Output**:
   - The script will save an animated GIF (`single_slit_diffraction_open.gif`) of the simulation.

## Customize

- You can adjust the parameters such as `a`, `L`, `N`, `screen_width`, and `lambda_` to see how they affect the diffraction pattern.
- Modify the plot settings in the script (`fig, ax`) to change the appearance of the animation, such as particle size and color.

## Example Output

![Simulation Animation](single_slit_diffraction_open.gif)

## Notes

- The simulation assumes a uniform distribution of particles at the slit and calculates the intensity distribution using the single-slit diffraction formula.
- Adjust the frame rate (`fps`) and other animation settings in `ani.save` for different visual effects.

## License

This project is licensed under the GPL-3.0 license - see the LICENSE file for details.
