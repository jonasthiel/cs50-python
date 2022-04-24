input = input("File name: ")
modified_input = input.lower().strip().split(".")
if modified_input[-1:][0] == "gif":
    print("image/" + modified_input[-1:][0])
elif modified_input[-1:][0] == "png":
    print("image/" + modified_input[-1:][0])
elif modified_input[-1:][0] in ["jpg", "jpeg"]:
    print("image/jpeg")
elif modified_input[-1:][0] in ["pdf", "zip"]:
    print("application/" + modified_input[-1:][0])
elif modified_input[-1:][0] == "txt":
    print("text/" + modified_input[0])
else:
    print("application/octet-stream")