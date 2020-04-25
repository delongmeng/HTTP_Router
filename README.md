# Request Routing in a Web Server with a Trie

Here I built a Router with a Trie. The depth of each route is the number of sections seperated by the '/' symbol. The time complexity for a search would be O(m * n), where m is the depth of the route (which would not be very long and we can consider it as a constant) and n is the number of children of each node (instead of the total number of routes stored). Overall, because diffent routes may share some common sections, so the time complexity should be less than O(n), where n is the total number of routes. For space, the search action does not add any extra space so it's O(1).

