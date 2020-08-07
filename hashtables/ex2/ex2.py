#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # allocate enough space for amount of tickets you have
    route = [None] * length
    #create dic
    flights = {}
    #hash each ticket so that the start loc is the key and the dest is value
    for ticket in tickets:
        flights[ticket.source] = ticket.destination
    #intitialze 
    next = flights["NONE"]

    for i in range(0, length):
        route[i] = next
        next = flights[next]


    return route
