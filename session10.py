class Login:

    def loginUser(self):
        print(">> Login dear User !!")


class GoogleLogin(Login):
    def loginUser(self, email, password):
        print(">>Google Login done")

class OTPLogIn(Login):
    def loginUser(self, phone):
        print("Login done through otp")

class FacebookLogin(Login):
    def loginUser(self):
        print("Facebook login done")


class Cab:
    def bookCab(self, source, destination):
        print("Cab booked from {} to {}".format(source, destination))

class MicroCab(Cab):
    def bookCab(self, source, destination):
        print("Ola micro Cab booked from {} to {}".format(source, destination))

class MiniCab(Cab):
    def bookCab(self, source, destination):
        print(" Mini Cab booked from {} to {}".format(source, destination))

# In python, everything is dynamic.. (Run time)
# Run time Polymorphism

login = Login()
login.loginUser()

print()

login = GoogleLogin()
login.loginUser("ayushi@99", "pass123")

print()

login = OTPLogIn()
login.loginUser("1235487")

print()

# Same reference variable can point to different objects- >Polymorphism

cab = Cab()
cab.bookCab("Silver arc", "Mbd")

cab = MicroCab()
cab.bookCab("Silver ", "to mbd")

cab = MiniCab()
cab.bookCab("Silver ", " to mbd")
