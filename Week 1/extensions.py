# asking user for file name
user_input = input("File name: ").lower().strip()

# storing the file's media type
extension = user_input[user_input.rfind('.'):].lstrip('.')

graphics = ["jpeg", "gif", "png"]
applications = ["pdf", "zip"]

if extension in graphics:
    print(f"image/{extension}")
elif extension == "jpg":
    print("image/jpeg")
elif extension in applications:
    print(f"application/{extension}")
elif extension == "txt":
    print("text/plain")
else:
    print("application/octet-stream")
