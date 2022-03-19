from utils import Direction
from utils import LOG

# Define directions to be cancelled out
opposite_directions: dict = {Direction.SOUTH: Direction.NORTH, Direction.NORTH: Direction.SOUTH,
                             Direction.EAST: Direction.WEST, Direction.WEST: Direction.EAST}


# Returns the optimized list of paths
def pathReduc(path: list):
    # Return immediately
    if len(path) <= 1:
        return path
    # Path to be returned
    efficient_path = []
    try:
        for item in path:
            # Compare with the last one from the new list
            if efficient_path and efficient_path[-1] == opposite_directions[item]:
                # Remove the last item from efficient_path as well as ignore the current one
                del efficient_path[-1]
            else:
                # Otherwise, append
                efficient_path.append(item)
    except IndexError:
        LOG.error("IndexError has been raised.")
        return
    return efficient_path
