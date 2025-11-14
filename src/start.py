import carla

client = carla.Client('192.168.64.1', 2000)

try:
  world = client.get_world()
  print(f"Connected to: ", world.get_map().name)

  blueprints = world.get_blueprint_library()

  vehicle_bp = blueprints.filter("vehicle.tesla.model3")[0]
  spawn_point = world.get_map().get_spawn_points()[0]

  vehicle = world.spawn_actor(vehicle_bp, spawn_point)
  print("spawned: ", vehicle.id)

except RuntimeError as e:
  print(f"Failed, {e}")
