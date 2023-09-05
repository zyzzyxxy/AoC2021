
nodes = {}
routes = []
nodes_dict = {}


class Edge():
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

class Node():
    def __init__(self, value):
        self.value = value
        self.neighbours = []

    def is_small(self):
        return self.value.islower()

    def is_big(self):
        return self.value.isupper()

    def is_start(self):
        return self.value == "start"

    def is_end(self):
        return self.value == "end"

    def add_neighbour(self, node):
        already_present = False
        for n in self.neighbours:
            if n.value == node:
                already_present = True
        if not already_present:
            self.neighbours.append(node)
    def get_possible_combinations(self, route):
        new_route = route.copy()
        routes = []
        if self.is_end():
            new_route.append(self.value)
            routes.append(new_route)
            return routes

        elif self.is_start():
            new_route.append(self.value)
            for n in self.neighbours:
                very_new_route = n.get_possible_combinations(new_route.copy())
                routes.extend(very_new_route)

        elif (self.is_small() and allowed_to_visit_2(self.value, route)) or self.is_big():
            new_route.append(self.value)
            for n in self.neighbours:
                very_new_route = n.get_possible_combinations(new_route.copy())
                routes.extend(very_new_route)
        return routes


def add_nodes(pair):
    global nodes
    n = nodes
    new_nodes = pair.split("-")

    for val in new_nodes:
        if not val in nodes:
            nodes[val] = Node(val)

    node1 = nodes[new_nodes[0]]
    node2 = nodes[new_nodes[1]]
    node1.add_neighbour(node2)
    node2.add_neighbour(node1)


def print_nodes():
    global nodes
    for key in nodes:
        node = nodes[key]
        print(node.value, " node_small: ", node.is_small()," start: " ,node.is_start()," end: ", node.is_end())


def get_all_routes(node_val):
    routes = []
    node = nodes[node_val]
    route = [node_val]
    routes.append(route)
    for neighbour in node.neighbours:
        new_route = route.copy()


def allowed_to_visit_2(n, route):
    global nodes
    n = nodes[n]
    if n == "start":
        return False
    if n.isupper():
        return True
    if(n in route):
        for name in route:
            if route.count(name) > 1:
                return False
    return True

def allowed_to_visit_dict(n, route):
    global nodes
    if n == "start":
        return False
    if n.isupper():
        return True
    if(n in route):
        for name in route:
            if name.islower() and route.count(name) > 1:
                return False
    return True


def get_routes(node_name):
    global nodes
    node = nodes[node_name]
    routes = node.get_possible_combinations()
    routes2 = []
    for route in routes:
        last_element = route[-1]
        if allowed_to_visit_dict(last_element, route):
            new_routes = get_routes(last_element, routes.copy())
            print(new_routes)

    return routes
    #routes.extend(get_all_routes("start"))


def get_values(neighbours):
    res = []
    for n in neighbours:
        res.append(n.value)

    return res


def allowed_to_visit(node_name, visited, small):
    if not small:
        return True
    if(node_name in visited):
        for name in visited:
            if visited.count(name) > 1:
                return False

    return True


def get_routes2(node_name, visited):
    global nodes
    node = nodes[node_name]
    results = []
    if node_name == "end":
        return [[node_name]]
    if not allowed_to_visit(node_name, visited, node.is_small()):
        return None
    if node.is_small():
        visited.append(node_name)

    neighbours = node.neighbours
    neighbour_values = get_values(neighbours)
    for neighbour in neighbours:
        if neighbour.value != "start":
            if allowed_to_visit(neighbour.value, visited, neighbour.is_small()):
                val = get_routes2(neighbour.value, visited.copy())
                if val:
                    for s in val:
                        if s not in results:
                            results.append(s)
                        if node_name != s and s[0] in neighbour_values:
                            string = [node_name]
                            string.extend(s)
                            if not string in results:
                                results.append(string)
    #print(results)
    return results


def filter_routes(r):
    result = []
    for route in r:
        if route[0]=='start' and route[-1] == 'end':
            result.append(route)
    return result


def get_routes_from_dict(route):
    global nodes_dict
    routes = []
    linking_node = route[-1]
    if linking_node == "end":
        return route

    for n in nodes_dict[linking_node]:
        if allowed_to_visit_dict(n, route):
            route_cpy = route.copy()
            route_cpy.append(n)
            new_routes = get_routes_from_dict(route_cpy)
            if new_routes:
                routes.extend(new_routes)

    return routes


def run():
    global nodes
    global nodes_dict
    file = open("day12")
    value_pairs = file.read().splitlines()
    nodes_dict = {}
    for pair in value_pairs:
        add_nodes(pair)
        x, y = pair.split("-")
        if x not in nodes_dict:
            nodes_dict[x] = []
        if y not in nodes_dict:
            nodes_dict[y] = []
        if y != "start":
            nodes_dict[x].append(y)
        if x!= "start":
            nodes_dict[y].append(x)
    print(nodes_dict)

    routes = get_routes_from_dict(["start"])
    print(routes)
    print(routes.count('end'))
    print(routes.count('start'))


    #start_node = nodes["start"]
    #x = start_node.get_possible_combinations([])
    #print(x)
    #print_nodes()
    #routes = get_routes("start")
    #routes2 = get_routes2("start", [])
    #routes2 = filter_routes(routes2)
    #for r in routes2:
    #    print(r)
    #print(routes2.__len__())



run()