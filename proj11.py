#################################################################################################################################################################
#
#
#   CSE 231
#   Project 11
#
#   Algorithm
#
#       function def open_file()
#           prompt for a file_name
#           while loop to repeatedly prompt for a file_name:
#               use try-except method to prevent the program from running errors
#               try :
#                   break from the loop if a file is successfully opened
#               except:
#                   print Invalid filename  and prompt for a file name
#                   go back to the while loop to start from the beginning
#              
#           return file_pointer
#
#       function def read_file(fp)
#
#           skip the header line of fp
#           initialize a list_tup
#
#           for loop through fp:
#               
#               initialize line[0], line[1], int(line[1]), convert them to a tuple 
#               append the tuple to the list
#
#           return list_tup
#
#       function def adjacency_matrix(L):
#
#           for loop through L:
#               If item is str: add the str to places_lst
#
#           sort the places_lst
#
#           for loop through range of len(places_lst):
#               append 0 to list of g 6 times
#
#           for loop throug L:
#
#               initialize i[0] to a and i[1] to b
#               find the index of a and b in places_lst
#               dist = i[2]
#
#               g[a_ind][b_ind] = int(dist)
#               g[b_ind][a_ind] = int(dist)
#
#           return places_lst , g
#
#
#       function def make_objects(places_lst,g):
#
#           initialize name_dict, id_dict as dictionaries
#           call apsp(g) function returningg , paths
#           
#           for i,j in enumerate(places_lst):
#
#               a_place = place.Place(j,i)
#               a_place.set_distances(g)
#               a_place.set_paths(paths)
#               append a_place to name_dict [j] 
#               append a_place to id_dict [j] 
#
#           return name_dict, id_dict
#
#
#       function def main():
#
#            
#           print(BANNER)
#           call open_file and read file function
#           assign the return value of read file function to adjacency_matrix(L)
#           assign the return value of adjacency_matrix(L) function to  make_objects(places_lst, g)
# 
#           prompt the user for the user to enter start place
#           while loop till the user enters valid start place
#
#           while loop till start_place != "q":
#    
#               initialize route_lst
#               prompt the user for destination
#               while loop till the user enters valid destination 
#               append valid destination to route list
#    
#               for loop through the route_lst:
#                   create a place object and create a destination id
#                   use these 2 objects to get the intermediate destinations by calling get_path function
#                   use these 2 objects to get the distance by calling get_distance function
#                   update the start value and distance every time it iterates 
#                   append the intermediate nodes to path_lst
#        
#               for loop through path_lst:
#                    print(the places)
#               print(distances)
#    
#               print(BANNER)
#               prompt the user for a starting place
#
#         print("Thanks for playing")
#
#
#
#
#
#
#
#
################################################################################################################################################################
        
   



import csv, place

def apsp(g):
    '''All-Pairs Shortest Paths using the Floyd-Warshall algorithm.'''
    '''DO NOT CHANGE'''

    INFINITE = 2**63-1  # a really big number (the biggest int for a 64-bit machine)

    # Initialize paths with paths for adjacent nodes
    paths = [[0 for j in range(len(g))] for i in range(len(g))]
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] != 0: 
                paths[i][j] = [i,j] # if two places are already adjacent then assign an initial path to them
            elif i != j:  # i == j means this is the same place so distance is zero
                g[i][j] = INFINITE # replacing zero by an "infinite" value
                # zero earlier meant that two places are not connected, now it will mean that they are not connected
                # initially, meaning that are "very-very" far ("virtually", for the sake of initialization)


    #apsp computation - floyd-warshall algorithm
    for k in range(len(g)):  # (for each) vertex k, to compare if i--k + k--j is shorter than i--j computed so far
        for i in range(len(g)): # (for each) vertex i of our interest
            for j in range(len(g)): # (for each) vertex j, to get the computed distance so far (between i and j)
                if g[i][j] > g[i][k] + g[k][j]: # determining if there is a shorter path (as per the above comment)
                    g[i][j] = g[i][k] + g[k][j] # updating the path-length value if there is a shorter path

                    # updating the path itself if there is a shorter path
                    paths[i][j] = paths[i][k][:]
                    paths[i][j].extend(paths[k][j][1:])

    # if a pair of places are still at infinite distance,
    # then assign them 0, to declare that they are not connected 
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] == INFINITE: 
                g[i][j] = 0

    return g,paths

def open_file():
    """
    

    Returns
    -------
    filepointer : csv
        file of places and distances.

    """
    
    
    file_name = input("Enter the file name: ")
    check = True
    
    while check == True:
        try:
            filepointer = open(file_name)
            break
        except FileNotFoundError:
            print("The file cannot be found! Please Try Again!!!")
            file_name = input("Enter filename: ")
            continue
    
    return filepointer
      
def read_file(fp):
    """
    

    Parameters
    ----------
    fp : csv file
        file of places and distances.

    Returns
    -------
    list of tuples.

    """
   
    
    reader = csv.reader(fp)
    next(reader,None)
    
    list_tup = []
   
    
    for line in reader:
        
        city_1 = line[0]
        city_2 = line[1]
        distance = line[2]
        list_tup.append((line[0],line[1],int(line[2])))
    
    return(list_tup)
        
    
  

def adjacency_matrix(L):
    """
    

    Parameters
    ----------
    L : list of tuples
        list of tuples of cities and distance.

    Returns
    -------
    places_lst : list
        list of places.
    g : list of list
        list of distances from places to places.

    """
   
    
    places_lst = []
   
    for line in L:
        
        for i in line:
            
           
            if type(i) == str:
                
                if i not in places_lst:
                    places_lst.append(i)
           
    
    places_lst = sorted(places_lst)
    
   
    length = len(places_lst)
  
    
    g = []
    h = []
    for i in range(length):
        
        h = [0] * length
        g.append(h)
    
    
    
    for i in L:
        
        a = i[0]
        b = i[1]
        
        a_ind = places_lst.index(a)
        b_ind = places_lst.index(b)
        dist = i[2]
       
        
        g[a_ind][b_ind] = int(dist)
        g[b_ind][a_ind] = int(dist)
       
    
    return places_lst ,  g

        
   
    
def make_objects(places_lst,g):
    """
    

    Parameters
    ----------
    places_lst : list of string
        list of places.
        
    g : list of list of integers
        list of distances from places to places.

    Returns
    -------
    name_dict : dictionary
        dictionary with key as places and values as the paths.
    id_dict : dictionary
        dictionary with key as id and values as the paths.

    """
    
    
    name_dict = dict()
    id_dict = dict()
    g , paths = apsp(g)
    
    
    for i,j in enumerate(places_lst):
        
        a_place = place.Place(j, i)
        a_place.set_distances(g)
        a_place.set_paths(paths)
        
        name_dict[j] = a_place
        id_dict[i] = a_place
    
    
    return name_dict, id_dict
        
        
      
        

def main():
    """
    
    print(BANNER)
    call open_file and read file function
    assign the return value of read file function to adjacency_matrix(L)
    assign the return value of adjacency_matrix(L) function to  make_objects(places_lst, g)
    
    prompt the user for the user to enter start place
    while loop till the user enters valid start place
    
    while loop till start_place != "q":
        
        initialize route_lst
        prompt the user for destination
        while loop till the user enters valid destination 
        append valid destination to route list
        
        for loop through the route_lst:
            create a place object and create a destination id
            use these 2 objects to get the intermediate destinations by calling get_path function
            use these 2 objects to get the distance by calling get_distance function
            update the start value and distance every time it iterates 
            append the intermediate nodes to path_lst
            
        for loop through path_lst:
            print(the places)
        print(distances)
        
        print(BANNER)
        prompt the user for a starting place
    
    print("Thanks for playing")
            


    """
    BANNER = '\nBegin the search!'
    fp = open_file()
    L = read_file(fp)
    places_lst, g = adjacency_matrix(L)
    name_dict_of_places, id_dict_of_places = make_objects(places_lst, g)
    
    # print(name_dict_of_places)
    
    
    check_lst = ["0","1","2","3","4","5","q","Q"]
    print(BANNER)
    start_place = input("Enter starting place, enter 'q' to quit: " )
    
    # er = input("This destination is not valid or is the same as the previous destination! Enter next destination, enter 'end' to exit: ") 
    
    if start_place != "q":
        
        while start_place not in places_lst:
            print("This place is not in the list!")
            start_place = input("Enter starting place, enter 'q' to quit: " )
            if start_place == "q":
                break
        
        
    
    while start_place != "q":
        
        route_lst = []
        
        # route_lst.append(start_place)
        dest = input('Enter next destination, enter "end" to exit: ')
        
        j = 0
        while dest != "end":
            
            if dest not in places_lst:
                
                print("This place is not in the list!")
                dest = input('Enter next destination, enter "end" to exit: ')

                continue
            
            
        
                
            
            else:
                
                if j == 0:
                    route_lst.append(dest)
                    dest = input('Enter next destination, enter "end" to exit: ')
                    j += 1
                    continue
                else:
                    if dest == route_lst[-1]:
                    
                        print('This destination is not valid or is the same as the previous destination!')
                        dest = input('Enter next destination, enter "end" to exit: ')
                        continue
                    else:
                        route_lst.append(dest)
                        dest = input('Enter next destination, enter "end" to exit: ')

                        continue
                        
                    
           
        
        
        check = True
        
        path_lst = []
        
        dist = int()
        
        n = ""
        
        m = 0
        s = 0
        for i in range(len(route_lst)):
            
            
            
            
            
            if m == 0:
                start_obj = name_dict_of_places[start_place]
                dest_obj = name_dict_of_places[route_lst[i]]
            
            else:
                start_obj = name_dict_of_places[n]
                dest_obj = name_dict_of_places[route_lst[i]]
                
            m += 1
            
            
            
            dest_id = dest_obj.get_index()
            short_path = start_obj.get_path(dest_id)
            
            distance = start_obj.get_distance(dest_id)
            
            dist += distance
          
            s += 1
            if short_path == 0:
                
                check = False
                
                
                if s == 1:
                    
                    print("places", start_place,"and",route_lst[i],"are not connected.")
                else:
                    print("places",route_lst[i-1],"and",route_lst[i],"are not connected.")
                    
                if i == len(route_lst)-1:
                    break
                
               
                
            else:
            
                if i == 0:
                    for j in range(len(short_path)):
                        
                        count = 0
                        for k, v in name_dict_of_places.items():
                            
                            if count == short_path[j]:
                                path_lst.append(k)
                            count += 1
                            
                elif i == len(route_lst)-1:
                    
                    for j in range(1,len(short_path)):
                        
                        
                        count = 0
                        for k, v in name_dict_of_places.items():
                            
                            if count == short_path[j]:
                                path_lst.append(k)
                            count += 1
                            
                elif i != len(route_lst)-1:
                    
                    for j in range(1,len(short_path)):
                        
                        
                        count = 0
                        for k, v in name_dict_of_places.items():
                            
                            if count == short_path[j]:
                                path_lst.append(k)
                            count += 1
                        
            
            n = route_lst[i]
        
      
                    
                        
        
        q = 0
        if check == True:
            
            print("Your route is:")
            for i in path_lst:
                
                print("    ",i)
                
          
                
            print("Total distance =" , dist)
                    
               
        
        print(BANNER)
        start_place = input("Enter starting place, enter 'q' to quit: " )   
        
        if start_place != "q":
            
            while start_place not in places_lst:
                print("This place is not in the list!")
                start_place = input("Enter starting place, enter 'q' to quit: " )
                if start_place == "q":
                    break
        continue
                
                
                    
                
        
        
        
        
    
        
    print('Thanks for using the software')
    
if __name__=='__main__':
    main()

