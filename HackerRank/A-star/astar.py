import Queue

class location():
    def __init__(self, move, priority):
        self.move = move
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

def manhattan(goal, current):
    return abs(goal[0]-current[0]) + abs(goal[1]-current[1])

def explore(pacman_r, pacman_c, grid, stack, visited, previous, cost_so_far, food):
    up = (pacman_r-1, pacman_c)
    left = (pacman_r, pacman_c-1)
    right = (pacman_r, pacman_c+1)
    down = (pacman_r+1, pacman_c)
    if grid[up[0]][up[1]] in ["-","."] and visited[up[0]][up[1]]==0:
        cost_so_far[up] = cost_so_far[(pacman_r, pacman_c)] + 1
        a = location(up, cost_so_far.get(up,0) + manhattan(food, up))
        stack.put(a)
        # print "Success up"
        visited[up[0]][up[1]]=1
        previous[(up[0], up[1])] = (pacman_r, pacman_c)
    if grid[left[0]][left[1]]  in ["-","."] and visited[left[0]][left[1]] == 0:
        cost_so_far[left] = cost_so_far[(pacman_r, pacman_c)] + 1
        stack.put(location(left, cost_so_far[left] + manhattan(food, left)))
        # print "Success left"
        visited[left[0]][left[1]] = 1
        previous[(left[0], left[1])] = (pacman_r, pacman_c)
    if grid[right[0]][right[1]]  in ["-","."] and visited[right[0]][right[1]] ==0:
        cost_so_far[right] = cost_so_far[(pacman_r, pacman_c)] + 1
        stack.put(location(right, cost_so_far[right] + manhattan(food, right)))
        # print "Success right"
        visited[right[0]][right[1]] = 1
        previous[(right[0], right[1])] = (pacman_r, pacman_c)
    if grid[down[0]][down[1]]  in ["-","."] and visited[down[0]][down[1]]  == 0:
        cost_so_far[down] = cost_so_far[(pacman_r, pacman_c)] + 1
        stack.put(location(down, cost_so_far[down] + manhattan(food, down)))
        # print "success down"
        visited[down[0]][down[1]]  = 1
        previous[(down[0], down[1])] = (pacman_r, pacman_c)

def nextMove( r, c, pacman_r, pacman_c, food_r, food_c, grid):
    food = (food_r, food_c)
    start = location((pacman_r, pacman_c),0)
    previous = {}
    visited = [[0 for i in range(c)] for j in range(r)]
    visited[pacman_r][pacman_c] = 1
    path=[]
    path.append([pacman_r,pacman_c ])
    stack = Queue.PriorityQueue()
    cost_so_far = {}
    cost_so_far[(pacman_r, pacman_c)] = 0

    explore(pacman_r, pacman_c, grid, stack, visited, previous, cost_so_far, food)
    #print stack
    while not stack.empty():
        move = stack.get().move
        path.append(move)
        pacman_r,pacman_c = move
        if pacman_r==food_r and pacman_c==food_c:
            #print "Yay! Got the food"
           # print len(path)
            #for i in path:
             #   print str(i[0]) + " " + str(i[1])

            directPath = []
            end = (food_r, food_c)

            while end != start.move:
                end = previous[end]
                directPath.append(end)

            print len(directPath) - 1
            for i in reversed(directPath):
                print str(i[0]) + " " + str(i[1])
        else:
            explore(pacman_r, pacman_c, grid, stack, visited, previous, cost_so_far, food)
            #print stack
pacman_r, pacman_c = [ int(i) for i in raw_input().strip().split() ]
food_r, food_c = [ int(i) for i in raw_input().strip().split() ]
r,c = [ int(i) for i in raw_input().strip().split() ]

grid = []
for i in xrange(0, r):
    grid.append(raw_input().strip())

nextMove(r, c, pacman_r, pacman_c, food_r, food_c, grid)
