checkValue=True
userInfo=[]
while True:

    name=input("what is your name :")
    userInfo.append(name)
    number=int(input("what is your phone number :"))
    userInfo.append(number)
    movieName=input("What moive you want to watch : ")
    userInfo.append(movieName)
    movieTime=input("What time you wanna watch movie?(morning, lunch, afternoon):")
    userInfo.append(movieTime)
    userSeat=input("Which seat you want to sit? (1,2,3,4,5,6,7,8,9,10):")
    userInfo.append(userSeat)
    checkPrint=input("You want to see your INFO? Yes/No:")
    if checkPrint=="Yes":
          print(userInfo)
    if checkPrint=="No":
