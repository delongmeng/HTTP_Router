



# Request Routing in a Web Server with a Trie

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, route_parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        
        for section in route_parts:
            if section not in current_node.children:
                current_node.insert(section)     
            current_node = current_node.children[section]
        
        current_node.handler = handler         

    def find(self, route_parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        for section in route_parts:
            if section not in current_node.children:
                return None
            current_node = current_node.children[section]
        
        return current_node.handler        

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, section):
        # Insert the node as before
        if section in self.children:  
            return
        
        self.children[section] = RouteTrieNode()        

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrie()
        self.root.root.handler = root_handler
        self.not_found = RouteTrieNode()
        self.not_found.handler = not_found_handler

    def add_handler(self, route, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        route_parts = self.split_path(route)
        self.root.insert(route_parts,handler)

    def lookup(self, route):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if route == '' or route == '/':
            return self.root.root.handler
        route_parts = self.split_path(route)
        handler = self.root.find(route_parts)
        if handler == None:
            return self.not_found.handler
        return handler

    def split_path(self, route):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here        
        route_parts = route.split('/')
        if route_parts[-1] == '': # handle the trailing slash issue
            route_parts.pop()
        if route_parts[0] == '': # if the route starts with '/', then after spliting the first element will be just ''
            route_parts = route_parts[1:]
        return route_parts





# Test cases

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output

print(router.lookup("")) # should print 'root handler'
# output: root handler

print(router.lookup("/")) # should print 'root handler'
# output: root handler

print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
# output: not found handler

print(router.lookup("/home/about")) # should print 'about handler'
# output: about handler

print(router.lookup("home/about")) # Here my design is to tolerate the missing '/' in the begining, so it should print 'about handler'
# output: about handler

print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
# output: about handler

print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
# output: not found handler






