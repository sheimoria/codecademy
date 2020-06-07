def shipping_price_ground(weight):
  if weight <= 2:
    price_per_pound = 1.50
  elif weight > 2 and weight  <= 6:
    price_per_pound = 3.00
  elif weight > 6 and weight  <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  return 20 + weight * price_per_pound

def shipping_price_drone(weight):
  if weight <= 2:
    price_per_pound = 4.50
  elif weight > 2 and weight  <= 6:
    price_per_pound = 9.00
  elif weight > 6 and weight  <= 10:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25
  return weight * price_per_pound

shipping_price_premium = 125.00

def print_cheapest_shipping(weight):
  
  ground = shipping_price_ground(weight)
  drone = shipping_price_drone(weight)
  premium = shipping_price_premium

  if ground < drone and ground < premium:
    cost = ground
    method = "ground"
  elif drone < ground and drone < premium:
    cost = drone
    method = "drone"
  else:
    cost = premium
    method = "premium ground"

  print("The cheapest option is $%.2f with %s shipping."
       % (cost, method)
       )
  
print_cheapest_shipping(4.8)
print_cheapest_shipping (41.5)