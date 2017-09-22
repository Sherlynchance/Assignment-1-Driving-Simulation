duration =  int(input("Enter time spent on the road(s) : "))
acc = int(input("Enter acceleration(m/s2)        : "))
distance = int(input("Enter distance(m)               : "))
in_v = 0
v = in_v + (acc*duration)
d = int(duration + (0.5*(acc*duration)**2))
for x in range (duration + 1):
    d1= (acc/2)*(x**2)
    print("Duration : ", x, "Distance: ", "*"*int(d1/10))
speed_limit = 60
if v > speed_limit:
    print("The person went over the speed limit. (Max speed was "+str(v) + "m/s)")
else:
    print("The person did not go over the speed limit. (Max speed was "+str(v) + "m/s)")

if d >= distance:
    print("The person reached their destination. (Reached, " + str(d) + "m)")
else:
    print("The person did not reached their destination. (Reached, " + str(d) + "m)")
