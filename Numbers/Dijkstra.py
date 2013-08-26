#An implementation of Dikstra's algorithm.

start = "A"
finish = "C"
data = [["A", [["B", 3], ["C", 11], ["D", 15]]], ["B", [["A", 3], ["C", 6], ["E", 7]]], ["C", [["B", 11], ["B", 6], ["E", 3], ["D", 2]]], ["D", [["A", 15], ["C", 2], ["F", 4]]], ["E", [["B", 7], ["C", 3], ["F", 3]]], ["F", [["E", 3], ["D", 4]]]] 
#What needs to be done:
#Determine if index has not been visited.
#(each time one does the calculation append to a list of visited indexes
#Have a list of all the distances  - recalculation process.
#Have a list of shortest path
visited = [] 
trip = [] # Pot naj bo oblike pot [[A, [pot do A], 
results = [start, []] #Results in the form [[start, [[B, distance to B], [C, distance to C], []...]

#Initializes the path variable according to the data
def init_path(data):
	for i in range(len(data)):
		trip.append([data[i][0], []])
	

#Checks if a node has been visited and returns true if it has and false otherwise
def is_visited(node):
	for i in range(len(visited)):
		if visited[i] == node:
			return True
	else:
		return False


#Calculates the results for first point - copies the data and then runs the next calculation.
def first_calc(point):
	init_path(data)
	for i in range(len(trip)): #Adds the trip for the first point A - > A
		if trip[i][0] == point:
			trip[i][1] = point
			pass #So we don't do extra runs
	for i in range(len(data)): #Adds all the distances to the results
		if data[i][0] == point:
			for j in data[i][1]:
				results[1].append(j)
				for i in range(len(trip)):
					if trip[i][0] == j[0]:
						trip[i][1] = [point, j[0]]
						pass
	tmp_length = 100 #These two variables are temporary and used for finding the node with the shortest distance and passing it to function calc
	tmp_point = ""
	for node in range(len(results[1])):
		if results[1][node][1] < tmp_length:
			tmp_point = results[1][node][0]
			tmp_length = results[1][node][1]
	
	print "Results", results
	#print "Trip", trip
	visited.append(point)
	calc(tmp_point) #runs the calculation
	
		
def calc(point):
	#Selects all nodes from b
	#ignores the already visited
	#for the others it calculates the distance from start to the point and compares it to the one in results. If it's lower update if, if not leave it as it is 
	# Update the trip variable 
	
	while len(visited) < len(data) + 1:
		for i in range(len(data)):
			if data[i][0] == point: # For the right point
				for j in range(len(data[i][1])):
					#print "Trip", trip, data[i][1][j][0]
					if data[i][1][j][0] in visited: #Ignores the already visited points
						pass
					else:
						not_in_results = 1 #This variable is used to check if the point is present in results. If it is it's set to 0 and value may be modified, otehrwise we need to append a new list.
						for k in range(len(results[1])): # To check we are at the right point
							#print results[1][k][0], point
							distance = 1000
							if results[1][k][0] == data[i][1][j][0]:
								not_in_results = 0
								for p in range(len(results)):
									if results[1][p][0] == point:
										distance = results[1][p][1] + data[i][1][j][1]
								if distance < results[1][k][1]: #Distance is indeed smaller - do all the crazy shit. 
									results[1][k][1] = distance #Updates the results for distance
									for dist in range(len(trip)): #This is for the trip
										if trip[dist][0] == point:
											new_trip = trip[dist][1][:]
											new_trip.append(results[1][k][0])
											break
									for dist2 in range(len(trip)):
										if trip[dist2][0] == data[i][1][j][0]:
											#print trip[dist2][0]
											trip[dist2][1] = new_trip
													
						#This is the loop which occurs if current point is not in results
						#print not_in_results
						
						if not_in_results == 1:
							for m in range(len(results[1])):
								if results[1][m][0] == point: #We need to find the right point
									new_distance = results[1][m][1] + data[i][1][j][1]
									break
							results[1].append([data[i][1][j][0], new_distance])
							for dist in range(len(trip)):
								if trip[dist][0] == point:
									new_trip = trip[dist][1][:] #Trip do trenutne tocke
									new_trip.append(data[i][1][j][0])
									#print new_trip
							for dist2 in range(len(trip)):
								if trip[dist2][0] == data[i][1][j][0]:
									trip[dist2][1] = new_trip
															
					
		#Take the results list and find the lowest value amongst the nonvisited nodes and run the query on it.
		visited.append(point) #first need to add a point so it doesn't search amongst them.
		temp_points = []
		for i in range(len(results[1])):
			if results[1][i][0] not in visited:
				temp_points.append(results[1][i][0])
		temp_distance = 1000
		next_point = ""
	
		for node in temp_points:
			for i in range(len(results[1])):
				if results[1][i][0] == node:
					if results[1][i][1] < temp_distance:
						temp_distance = results[1][i][1]
						next_point = results[1][i][0]
		#print "Next point", next_point, "\n\n\n"
		calc(next_point)
	print "Results", results
	#print "Trip", trip
		
first_calc("A")
"""for i in range(len(data)):
	print data[i][0], data[i][1]"""
