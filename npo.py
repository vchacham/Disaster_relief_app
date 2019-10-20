class NPO:

    def __init__(self, name, location, radius, resources):
        self.name = name
        self.location = location
        self.radius = radius
        self.resources = resources
    
    def setLocation(self, location):
        self.location = location
    
    def setResources(self, resources):
        self.resources = resources
    
    def getTicketPriorities(self, tickets):

        def sortBy(t):
            resources_matched = True
            for ix in range(5):
                if t.resources[ix] == 1 and self.resources[ix]<t.people:
                    resources_matched = False
                    break
            dist = ((self.location[0]-t.location[0])**2 + (self.location[1]-t.location[1])**2)**0.5

            return 1-t.hurt, 1-t.threat, 1-resources_matched, dist
        
        filtered_tickets = []
        for t in tickets:
            dist = ((self.location[0]-t.location[0])**2 + (self.location[1]-t.location[1])**2)**0.5
            if dist<self.radius:
                filtered_tickets.append(t)
        return sorted(filtered_tickets, key = lambda x: sortBy(x))