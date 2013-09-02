#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Create a reservation system which books airline seats or hotel rooms.
It charges various rates for particular sections of the plane or hotel.
Example, first class is going to cost more than coach. Hotel rooms have penthouse suites which cost more.
Keep track of when rooms will be available and can be scheduled."""

class Guest():
	def __init__(self, name, surname, arr_day, leave_day, room_t = "2"):
		"""Inits the function and adds all the necessary variables (room_t is room type)"""
		self.name = name
		self.surname = surname
		self.arr = arr_day
		self.leave = leave_day
		self.room_t = room_t
		self.charge = 0
		
	def add_age(self, age):
		"""Adds guest age"""
		self.age = age
		
	def print_info(self):
		"""Prints all info about the guest (except age)"""
		print "Guest info: {0} {1}, Arrives on day {2}, leaves on day {3}, stays in room type {4}. Charging {5} €".format(self.name, self.surname, self.arr, self.leave, self.room_t, self.charge)
		

def room_prices(value):
	if value == 1:
		return 32
	elif value == 2:
		return 54
	elif value == 3:
		return 82
	elif value == 4:
		return 187	

		
class Hotel():
	
	def __init__(self, name):
		self.name = name
		self.rooms = [] #The form of the list is [["room name, " room type (1-4)", [0, Guest name, 0T0T], ...] where 0 means not taken and T taken
		self.guests = [] #The form of the list is ["guest name", [init.date, end.date], ...]	
	
	def add_room(self, room, room_type):
		"""
		Adds a room with name type and zeros to indicate it's not Booked.
		"""
		self.rooms.append([room, room_type, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
		
	def book(self, guest):
		"""
		Books the room based on the desired room type. First checks if the room is free."
		"""
		for i in range(len(self.rooms)):
			if self.rooms[i][1] == guest.room_t:
				free = "Yes" #Initially the room is free
				for day in range(guest.arr, guest.leave+1): #Goes through all the day and for each one checks if the room is free
					if self.rooms[i][2][day] != 0:
						free = "No" #Unless someone is staying there, then we set it to not free
				if free == "Yes":
					for day in range(guest.arr, guest.leave+1):
						self.rooms[i][2][day] = guest.name[0] + guest.surname[0] #Changes the booking from 0 to "jn" for "janez novak"
					guest.charge = (guest.leave - guest.arr) * room_prices(self.rooms[i][1]) #Calculates the charging value
					self.guests.append(guest) #Appends to the list of guests for printing purposes
					break
		pass
		
	def print_rooms(self):
		for i in range(len(self.rooms)):
			if self.rooms[i][1] == 4:
				room = "exclusive"
			elif self.rooms[i][1] == 3:
				room = "suite"
			elif self.rooms[i][1] == 2:
				room = "regular"
			elif self.rooms[i][1] == 1:
				room = "bungalow"
			print "Room '{0}', {1}, status: {2}".format(self.rooms[i][0], room, self.rooms[i][2])
			
	def p_guests(self):
		print "List of all guests ..."
		for i in self.guests:
			i.print_info()
			
p = Hotel("plaza")
p.add_room("greenish", 2)
p.add_room("Expensive", 4)
p.add_room("213", 1)
p.add_room("Hipko", 3)
p.add_room("blue", 3)

j = Guest("janez", "novak", 3, 9, 3)
k = Guest("klemen", "pirnat", 6, 12, 1)
l = Guest("leon", "stukelj", 1, 14, 4)
m = Guest("miro", "cerar", 1, 4, 3)

p.book(j)
p.book(k)
p.book(l)
p.book(m)

#j.print_info()
#p.print_rooms()
p.p_guests()
