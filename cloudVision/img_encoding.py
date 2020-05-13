import base64
 
with open("test.jpg", "rb") as imageFile:
    string = base64.b64encode(imageFile.read())
    print len(string)
    print(string)
