""" 
Description
There are a city's N bus information, route[i] stores the bus stop through which the i-th bus passes, find the minimum number of transfers from station A to station B. If you can't get to station B from station A, return -1.

1 <= N <= 100, 2 <= |route[i]| <= 100, 0 <= route[i][j] <= 2^31 - 1
A and B two stations must exist and they are different

Example

Given N = 2, route = [[1, 2, 3, 4], [3, 5, 6, 7]], A = 1, B = 4, return 1.
Explanation:
We only need to take the bus No.0, you can get to Station 3 from Station 0.

Given N = 2, route = [[1, 2, 3, 4], [3, 5, 6, 7]], A = 1, B = 7, return 2.
Explanation:
We need to take bus No.0 from station 0 and then take bus No.1 to station 6 at station 2.
"""

class Solution:
    """
    @param N: The number of buses
    @param route: The route of buses
    @param A: Start bus station
    @param B: End bus station
    @return: Return the minimum transfer number
    """
    class Bus:
        def __init__(self, label):
            self.label = label
            self.neighbors = set()
            
    def getMinTransferNumber(self, N, route, A, B):
        # Write your code here
        if not route:
            return -1
        
        # copy bus
        label2bus = {}
        for i in range(N):
            label2bus[i] = self.Bus(i)
        
        stop2bus = collections.defaultdict(set)
        for bus, bus_route in enumerate(route):
            for stop in bus_route:
                stop2bus[stop].add(bus)
        
        print(f'stop2bus {stop2bus}')
        
        #copy neighbors
        for stop, bus_set in stop2bus.items():
            for bus_label in bus_set:
                bus = label2bus[bus_label]
                bus.neighbors |= bus_set
                bus.neighbors.remove(bus.label)
                
        start_queue = collections.deque()
        end_queue = collections.deque()
        start_visited = set()
        end_visited = set()
        transfer = 0
        
        if A not in stop2bus or B not in stop2bus:
            return -1
        
        if len(stop2bus[A] & stop2bus[B]) != 0:
            return 1 
        
        for bus in stop2bus[A]:
            start_queue.append(bus)
            start_visited.add(bus)
            print(f'A bus {bus}')
            
        for bus in stop2bus[B]:
            end_queue.append(bus)
            end_visited.add(bus)
            print(f'B bus {bus}')
            
        while start_queue and end_queue:
            size = len(start_queue)
            transfer += 1
            for _ in range(size):
                start_bus = label2bus[start_queue.popleft()]
                print(f'start: lvl tf {transfer} bus {start_bus.label}')
                # reached end stop
                if start_bus.label in end_visited:
                    print(f'end queue {end_queue}')
                    return transfer
                
                for nei in start_bus.neighbors:
                    if nei in start_visited:
                        continue
                    start_queue.append(nei)
                    start_visited.add(nei)
            
            
            size = len(end_queue)
            transfer += 1
            for _ in range(size):
                end_bus = label2bus[end_queue.popleft()]
                print(f'end: lvl tf {transfer} bus {end_bus.label}')
                # reached start stop 
                if end_bus.label in start_visited:
                    print(f'start queue {start_queue}')
                    return transfer
                
                for nei in end_bus.neighbors:
                    if nei in end_visited:
                        continue
                    end_queue.append(nei)
                    end_visited.add(nei)
                    
        return -1