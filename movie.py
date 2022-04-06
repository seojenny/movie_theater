"""
Movie theater
By Jenny
"""
#List to store user's choices
userInfo=[]
rebook = 'yes'
while rebook=='yes':
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
