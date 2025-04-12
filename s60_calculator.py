import math
def calculate_trajectory(v0, angle_deg, distance, g=9.81):
    angle_rad = math.radians(angle_deg)
    t = distance / (v0 * math.cos(angle_rad))
    y = v0 * math.sin(angle_rad) * t - 0.5 * g * t**2
    return round(t, 2), round(y, 2)