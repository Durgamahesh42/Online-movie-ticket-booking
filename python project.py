#this t_movie function is used to select movie name def t_movie():
global f f = f+1
print("Which movie do you want to watch?") print("1,Avatar")
print("2,Hit 2") print("3,Avangers") print("4,Men in black") print("5,Bahubali") print("6,back")
movie = int(input("Choose your movie: ")) if movie == 6:
# in this it goes to center function and from center it goes to movie function and it comes back here and then go to theater
center() theater() return 0 if f == 1: theater()
 

# this theater function used to select screen def theater():
print("Which screen do you want to watch movie: ") print("1,SCREEN 1")
print("2,SCREEN 2")

print("3,SCREEN 3")

a = int(input("Choose your screen: "))

ticket = int(input("Number of ticket do you want?: ")) timing(a)

# this timing function used to select timing for movie def timing(a):
time1 = {

"1": "10.00-1.00",

"2": "1.10-4.10",

"3": "4.20-7.20",

"4": "7.30-10.30"

}

time2 = {

"1": "10.15-1.15",

"2": "1.25-4.25",

"3": "4.35-7.35",

"4": "7.45-10.45"

}

time3 = {
 
"1": "10.30-1.30",

"2": "1.40-4.40",

"3": "4.50-7.50",

"4": "8.00-10.45"

}

if a == 1:

print("Choose your time:") print(time1)
t = input("Select your time:")


x = time1[t] print("================================================")
print("**Booked Successfully**!, Enjoy movie at "+x) print("================================================")
elif a == 2:

print("Choose your time:") print(time2)
t = input("Select your time:") x = time2[t]
print("=================================================")

print("**Booked Successfully**!, Enjoy movie at "+x) print("=================================================")
elif a == 3:

print("Choose your time:") print(time3)
t = input("Select your time:")
 
x = time3[t] print("================================================")
print("**Booked Successfully!**, Enjoy movie at "+x) print("================================================")
return 0




def movie(theater): if theater == 1: t_movie()
elif theater == 2: t_movie()
elif theater == 3: t_movie()
elif theater == 4: t_movie()
elif theater == 5: t_movie()
elif theater == 6: place()
else:
print("Wrong choice")




def center():

print("Which theater do you wish to see movie? ")
 
print("1)Inox")

print("2)Icon")

print("3)PVP")

print("4)PVR")

print("5)Imax")

print("6)back")

a = int(input("Choose your option: ")) movie(a)
return 0


# this function is used to select city def city():
print("==================================================")

print("***HI Welcome To Movie Ticket Booking*** ") print("==================================================")
print("Where you want to watch movie?:") print("1)Vijayawada") print("2)Hyderabad") print("3)Khammam")
print("4)Vizag") print("5)Guntur")
place = int(input("choose your option: ")) if place == 1:
center()

elif place == 2: center()
 
elif place == 3: center()
elif place == 4: center()
elif place == 5: center()
else:

print("Wrong   choice") city() # it calls the function city
