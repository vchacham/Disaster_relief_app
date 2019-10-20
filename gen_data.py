import random
import math

class Ticket:
    def __init__(self, name, location, people, resources, hurt, threat):
        self.name = name
        self.location = location
        self.people = people
        self.resources = resources
        self.hurt = hurt
        self.threat = threat

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
        

def gen_tickets(l_min, l_max, p_min, p_max, samples, hurt_p=0.5, threat_p=0.5):
    """
    lt, ln = 0 - 100
    people affected
    resources = [food, shelter, transport, medicine, water]
    hurt = bool
    pending_threats = bool
    message = "" optional
    """
    data = []
    for i in range(samples):
        lt = random.random() * 100
        ln = random.random() * 100
        people = math.floor(random.random() * (p_max - p_min) + p_min)
        hurt = random.random() > hurt_p
        resources = [ 1 if random.random()>0.5 else 0 for i in range(5)]
        pending_threats = random.random() > threat_p
        t = Ticket(str(i), (lt, ln), people, resources, hurt, pending_threats)
        data.append(t)
    return data

def gen_npos(l_min, l_max, resources_mx, samples):
    data = []
    for i in range(samples):
        lt = random.random() * 100
        ln = random.random() * 100
        resources = [ math.floor(random.random() * resources_mx) for i in range(5) ]
        radius = 15
        npo = NPO(str(i), (lt, ln), radius, resources)
        data.append(npo)
    return data

def printTickets(tickets):
    count = 0
    for i in tickets:
        count+=1
        print("Ticket: " + str(count))
        print("\tLocation: " + str(i.location[0]) + "," + str(i.location[1]))
        print("\tPeople Affected: "+ str(i.people))
        print("\tResources Needed:")
        # [food, shelter, transport, medicine, water]
        print("\t\tFood: " + str(i.resources[0]) )
        print("\t\tShelter: " + str(i.resources[1]) )
        print("\t\tTransport: " + str(i.resources[2]) )
        print("\t\tMedical Attention: "+ str(i.resources[3]))
        print("\t\tWater: " + str(i.resources[4]) )
        print("\tPeople Hurt: " + ("yes" if i.hurt else "no"))
        print("\tImpending Threats: "+ ("yes" if i.threat else "no"))
        print("\n")

tickets = gen_tickets(0, 100, 1, 10, 100, 0.99, 0.95)
npos = gen_npos(0, 100, 20, 6)
t = npos[0].getTicketPriorities(tickets)

print("===================")
print("Disaster Relief NPO")
print("===================")
printTickets(t)



