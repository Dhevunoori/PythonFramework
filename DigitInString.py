import pyttsx3
engine = pyttsx3.init()
number = 54321
print(type(number))
for digit in str(number):
	# file = str(digit)+".mp3"
	# print((file))
	# fp = open(file, "r")
	engine.say(digit)
	print(digit)
	engine.runAndWait()