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
    number=input("what is your phone number :")
    #Choose the movie
    userInfo.append(number)
    movies = ("It", "The nun", "antman", "spiderman")
    for movie in movies:
        print(movie)

    movieName = None
    while movieName not in movies:
        movieName=input("What moive you want to watch : ")
        
    userInfo.append(movieName)
    #Choose the timea
    movieTime = None
    while movieTime not in ('morning', 'lunch', 'afternoon'):
        movieTime=(input("When do you wanna watch movie?(morning, lunch, afternoon):")).lower()
    
    print(f"name: {name}, number: {number}, movie: {movie}, time: {movieTime}")
    
    #ask information correction
    answer = None
    while answer not in ('yes', 'no'):
        answer=(input("is this information correct?")).lower()
        match answer:
            case 'yes':
                print('Thank you for booking!')
                rebook = 'no'
            case 'no':
                rebook = None
                while rebook not in ('yes', 'no'):
                    rebook=(input("would you like to book again?")).lower()
                if rebook== 'no':
                    print('see you next time!')
