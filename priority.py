from gen_data import *

tickets = gen_tickets(0, 100, 1, 10, 100, 0.99, 0.95)
npos = gen_npos(0, 100, 20, 6)
t = npos[0].getTicketPriorities(tickets)

print("===================")
print("Disaster Relief NPO")
print("===================")
printTickets(t)