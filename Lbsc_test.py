import numpy as np
import matplotlib.pyplot as plt

# Create simulated test data
time = np.linspace(0, 1e-3, 2500)  # 1 millisecond total duration, 2500 points
signal1 = np.ones_like(time) * 5    # Beam signal starts at 5 V
signal2 = np.ones_like(time) * 5    # System signal starts at 5 V

# Simulate turn-off points
signal1[800:] = 0                   # Beam turns off at index 800
signal2[850:] = 0                   # System turns off at index 850

# Plot with blue and orange colors
plt.plot(time*1e6, signal1, label='Beam (CH1)', color='blue')
plt.plot(time*1e6, signal2, label='System (CH2)', color='orange')

plt.axvline(time[800]*1e6, color='blue', linestyle='--', alpha=0.7, label='Beam Off')
plt.axvline(time[850]*1e6, color='orange', linestyle='--', alpha=0.7, label='System Off')

plt.xlabel("Time [µs]")
plt.ylabel("Voltage [V]")
plt.title("LINAC Signal Analysis (Simulated Data)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
