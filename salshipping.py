weight = 4.8
#Ground Shipping

if weight <= 2:
  cost_ground = (1.50 * weight) + 20.00
elif weight > 2 and weight <= 6:
  cost_ground = (3.00 * weight) + 20.00
elif weight > 6 and weight <= 10:
  cost_ground = (4.00 * weight) + 20.00
else:
  cost_ground = (4.75 * weight) + 20.00

print("Ground Shipping $", cost_ground)

cost_premium_ground = 125.00

print("Premium Ground Shipping: $", cost_premium_ground)

#Drone Shipping 

if weight <= 2:
  cost_drone = 4.50 * weight + 0.00
elif weight > 2 and weight <= 6:
  cost_drone = 9.00 * weight + 0.00
elif weight > 6 and weight <= 10:
  cost_drone = 12.00 * weight + 0.00
else:
  cost_drone = 14.25 * weight + 0.00

print("Drone Shipping: $", cost_drone)

