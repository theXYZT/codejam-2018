# Codejam 2018, Practice Session: Steed 2: Cruise Control

class Horse():
    """Class for Horse."""
    def __init__(self, position, speed, destination):
        self.position = position
        self.speed = speed
        self.time_to_destination = (destination - self.position) / self.speed


def find_max_speed(horses):
    """Finds max speed to reach destination."""
    max_time = max([horse.time_to_destination for horse in horses])
    return destination / max_time

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    destination, num_horses = [int(i) for i in input().split()]

    horses = []
    for _ in range(num_horses):
        position, speed = [int(i) for i in input().split()]
        horses.append(Horse(position, speed, destination))

    max_speed = find_max_speed(horses)
    print('Case #{}: {:.6f}'.format(case, max_speed))
