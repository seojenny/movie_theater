"""
Movie theater
By Jenny
"""
#List to store user's choices
userInfo=[]
#main loop
rebook = 'yes'
while rebook=='yes':
    #enter user's info
    name=input("what is your name :")
    userInfo.append(name)
    number=int(input("what is your phone number :"))
    userInfo.append(number)
    movies = ("It", "The nun", "antman", "spiderman")
    for movie in movies:
        print(movie)

    movieName = None
    while movieName not in movies:
        movieName=input("What moive you want to watch : ")
        
    userInfo.append(movieName)
    
    movieTime = None
    while movieTime not in ('morning', 'lunch', 'afternoon'):
        movieTime=(input("When do you wanna watch movie?(morning, lunch, afternoon):")).lower()
    
    """userInfo.append(movieTime)
    
    userSeat=input("Which seat you want to sit? (1,2,3,4,5,6,7,8,9,10):")
    userInfo.append(userSeat)"""
    
#seats
movie_seats = {{[], [], []}, {[], [], []}, {[], [], []}
#for morning It
def movie_seat(chosen_movie, chosen_time):
    booked_seats=[]
    while True:
          movie_index = movies.index(chosen_movie)
          time_index = times.index(chosen_time)
          #print seats and check if seat is already booked
          seats_tct = ''
          for seat_n in range(1,11):
               if seat_n in movie_seats[movie_index][time_index]:
                    seats_txt = seats_txt + 'x'
               else:
                    seats_txt = seats_txt + f' {seat_n}'
               
          print (seats_txt)
          #asks for seat and appends it into booked_seats
          chosen_seat = None
          while_chosen_seat not in range(1,11):
               #validate that while not chosen_seat.isnumber():
               chosen_seat = int(input("what seat do you want?"))
               
               if chosen_seat in movie_seats[movie_index][time_index]:
                    print("seat already has been chosen, please choose a different seat")
               else:
                    movie_seats[movie_index][time_index].append(chosen_seat)
                    booked_seats.append(chosen_seat)
               
             #if the user wants it returns the program
               choose_again = None
               choose_again = input("do you want to book a seat again?(yes/no): ")
               if choose_again == 'no':
                    print("thank you")
                    break
           return booked seats
    
    print(f"name: {name}, number: {number}, movie: {movie}, time: {movieTime}")
    
    answer = None
    while answer not in ('yes', 'no'):
        answer=(input("is this information correct?")).lower()
        if answer=='yes':
            print('Thank you for booking!')
            rebook = 'no'
        else:
            rebook = None
            while rebook not in ('yes', 'no'):
                rebook=(input("would you like to book again?")).lower()
            if rebook== 'no':
                print('see you next time!')
