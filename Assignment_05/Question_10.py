case = input("Enter status code: ")
if case == "200":
    print("OK")
elif case == "201":
  	print("Created")
elif case == "202":
  	print("Accepted")
elif case == "301":
  	print("Moved Permanently")
elif case == "303":
  	print("See other")
elif case == "304":
  	print("Not modified")
elif case == "307":
  	print("Temporary Redirect")
elif case == "400":
  	print("Bad Request")
elif case == "401":
  	print("Unauthorized")
elif case == "403":
  	print("Forbidden")
elif case == "404":
  	print("Not found")
elif case == "410":
  	print("Gone")
elif case == "500":
  	print("Internal Server Error")
elif case == "503":
  	print("Service Unavailable")
else:
  	print("Invalid status code!")
