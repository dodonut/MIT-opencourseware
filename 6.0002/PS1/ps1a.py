###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    map_data = {}
    file = open(filename,'r')
    for line in file:
        data = line.split(',')
        map_data[data[0]] = int(data[1].split('\n')[0])

    return map_data


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    import operator
    current_limit = limit
    trip = []
    all_trips = []
    not_picked = cows.copy()
    while len(not_picked):
        tmp_cows = not_picked.copy()
        not_picked = {}
        while len(tmp_cows):
            key, value = max(tmp_cows.items(), key=operator.itemgetter(1))
            if value <= current_limit:
                trip.append(key)
                current_limit -= value
            else:
                not_picked[key] = value

            tmp_cows.pop(key)

        all_trips.append(trip)
        trip = []
        current_limit = limit

    return all_trips


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    min_trip_count = 100000
    min_trip_list = []
    for partition in get_partitions(cows.keys()):
        valid_trip = True
        for trip in partition:
            tmp_lim = sum(int(cows[v]) for v in trip)
            if tmp_lim > limit: valid_trip = False
        if len(partition) < min_trip_count and valid_trip :
            min_trip_count = len(partition)
            min_trip_list = partition

    return min_trip_list

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows('ps1_cow_data.txt')
    start = time.time()
    print(brute_force_cow_transport(cows))
    print(time.time() - start)
    start = time.time()
    print(greedy_cow_transport(cows))
    print(time.time() - start)



# Answers A.5:
 # 1- The algorithm of the greedy runs faster because it does not test
 #    every possible combination, instead it goes to an choosen approach which
 #    may or may not be optimal (not optimal in this case, since it found the best
 #    solution being 6 trips while the brute force founded 5.)
 #    While the brute force will give the best possible way to do it (
 #    because test all ways possible), runs slow in a large set. O(2^n).
 # 2- It may or may not return it, because it chooses an approach of getting 
 #    the heaviest first which (depending on data) be the best solution, but
 #    not true for all cases.
 # 3- Yes, because it test all solutions possible in a data set and see's 
 #    what is the best of them.