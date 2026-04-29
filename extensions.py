def files(a):
    if a.endswith(".jpeg"):
        return "image/jpeg"
    elif a.endswith(".png"):
        return "image/png"
    elif a.endswith(".gif"):
        return "image/gif"
    elif a.endswith(".jpg"):
        return "image/jpg"
    elif a.endswith(".pdf"):
        return "image/pdf"
    elif a.endswith(".txt"):
        return "image/txt"
    elif a.endswith(".zip"):
        return "image/zip"
    else:
        return "application/octet-stream"

def main():
    file_name = input("File name: ")
    print(files(file_name))
main()