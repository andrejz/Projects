#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Movie Store – Manage video rentals and controls when videos are checked out,
due to return, overdue fees and for added complexity create a summary of
those accounts which are overdue for contact."""

class Movie():
	def __init__(self, name, genre):
		"""Initiates the variables like name, and genre"""
		self.name = name
		self.genre = genre
		self.rented = 0
		self.deadline = 0
		fee_day = 1.2
		self.fee = 0
		self.customer = "None"
				
	def rent(self, c_name, time = 14):
		"""Checks if movie is already rented and if not rents it (sets deadline and customer)"""
		if self.rented == 1:
			print "Sorry, the movie is already rented."
		elif self.rented == 0:
			self.rented = 1
			self.deadline = time
			self.customer = c_name
		
			
	def return_m(self, time):
		"""Returns the movie (resets rented state and customer) and charges a fee if custoemr is behind deadline"""
		if time > self.deadline:
			self.fee = (time - self.deadline)* fee_day
		else:
			self.fee = 0
		self.rented = 0
		self.customer = "None"
		return self.fee
	
	def print1(self):
		if self.rented == 0:
			self.a = "No"
		elif self.rented == 1:
			self.a = "Yes"
		"""Prints out all info about the movie"""
		print "Movie title: {0}\t   Genre: {1}, \t Rented: {2},\t  Rented by: {3}".format(self.name, self.genre, self.a, self.customer)
		
class Inventory():
	"""Operations for movie inventory"""
	def __init__(self):
		"""Defines movie list on which the operations are executed"""
		self.movie_list = []
		
	def add(self, movie):
		"""Adds movie to a list of movies"""
		self.movie_list.append(movie)
		
	def check_time(self, time):
		"""Goes through the list of movies and prints the overdue movies"""
		overdue = []
		for movie in self.movie_list:
			if movie.rented == 1 and time > movie.deadline:
				overdue.append([movie.name, time-movie.deadline, movie.customer])
		print "\nList of overdue movies\n"
		for i in range(len(overdue)):
			print "{0}, {1} days overdue, rented by {2}".format(overdue[i][0], overdue[i][1], overdue[i][2])

	def unrented(self):
		"""Returns unrented movies"""
		for movie in self.movie_list:
			if movie.rented == 0:
				movie.print1()

	def all(self):
		"""Prints out all movies"""
		print "\nList of unrented movies:"
		for movie in self.movie_list:
			movie.print1()

a = Movie("Hide and Seek", "Drama")
b = Movie("The Matrix", "Fantazy")
c = Movie("Die Hard 3", "Action")
d = Movie("How to laugh", "Comedy")
e = Movie("Kill a bee", "Funny")

store = Inventory()
store.add(a)
store.add(b)
store.add(c)
store.add(d)
store.add(e)

#store.all()

a.rent("Jone", 32)
b.rent("Hose", 12)
a.rent("Đony", 12)

store.all()

c.rent("Jone", 6)
d.rent("Brig", 19)

print "Unrented:\n"
store.unrented()


store.check_time(22)
