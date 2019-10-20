import random
import math
from npo import *
from ticket import *        

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
        print("\t\tFood: " + str(i.resources[0]*i.people) )
        print("\t\tShelter: " + str(i.resources[1]*i.people) )
        print("\t\tTransport: " + str(i.resources[2]*i.people) )
        print("\t\tMedical Attention: "+ str(i.resources[3]*i.people))
        print("\t\tWater: " + str(i.resources[4]*i.people) )
        print("\tPeople Hurt: " + ("yes" if i.hurt else "no"))
        print("\tImpending Threats: "+ ("yes" if i.threat else "no"))
        print("\n")