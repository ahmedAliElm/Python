import cv2
from pyzbar import pyzbar
import webbrowser

def readCode(imagePath):

    i = 1 # to count how many codes are there

    image = cv2.imread(imagePath) # Loads the image

    if image is None:
        print("\nImpossible to load the image. Please verify the path or the file format.")
        return

    decodedObjects = pyzbar.decode(image) # Decodes the image

    # Print the decoded data
    if decodedObjects:

        for obj in decodedObjects:

            print("\nCode", i, ":")

            if obj.type != "QRCODE":
                print("\nData type:", obj.type, "(barcode)")
            else:
                print("\nData type:", obj.type)

            data = obj.data.decode("utf-8")

            if data.startswith("http://") or data.startswith("https://") or ".net" in data or ".com" in data or ".ma" in data:

                print("\nIt's a website.\n")

                temp = input("Would you like to access it? Answer with yes/Yes or no/No: ")
                if temp == "yes" or temp == "Yes":
                    webbrowser.open(data)

                while temp != "yes" and temp != "Yes" and temp != "no" and temp != "No":                         

                    temp = input("Please type yes/Yes or no/No: ")

                    if temp == "yes" or temp == "Yes":
                        webbrowser.open(data)

            else:
                if obj.type == "QRCODE":

                    temp = input("\nWould you like to display the data stored in the QR code? Answer with yes/Yes or no/No: ")
                    
                    if temp == "yes" or temp == "Yes":
                        if data.startswith("WIFI"):
                            print("\nIt's a Wi-Fi password")

                        print("\nData:", data, "\n")
                        break  

                    while temp != "yes" and temp != "Yes" and temp != "no" and temp != "No":
    
                        temp = input("Please type yes/Yes or no/No: ")

                        if temp == "yes" or temp == "Yes":
                            if data.startswith("WIFI"):
                                print("\nIt's a Wi-Fi password.")

                            print("\nData:", data, "\n")



                    temp = input("\nWould you like to display the data stored in the QR code? Answer with yes/Yes or no/No: ")

                    if temp == "yes" or temp == "Yes":
                            print("Data: ", data)

                    while temp != "yes" and temp != "Yes" and temp != "no" and temp != "No":
    
                        temp = input("Please type yes/Yes or no/No: ")

                        if temp == "yes" or temp == "Yes":
                            print("Data: ", data)

                else: # Barcode
                    temp = input("\nWould you like to display the data stored in the barcode? Answer with yes/Yes or no/No: ")

                    if temp == "yes" or temp == "Yes":
                        print("\nData: ", data, "\n")

                    while temp != "yes" and temp != "Yes" and temp != "no" and temp != "No":
    
                        temp = input("Please type yes/Yes or no/No: ")

                        if temp == "yes" or temp == "Yes":
                            print("\nData: ", data, "\n")

            i += 1
    else:
        print("\nNo code detected.\n")

imagePath = r"C:\Users\dell\OneDrive\Bureau\QR\1.jpg"
print("\t\t  ___  _____  ____  ____    ____  ____    __    ____  ____  ____ \r\n\t\t / __)(  _  )(  _ \\( ___)  (  _ \\( ___)  /__\\  (  _ \\( ___)(  _ \\\r\n\t\t( (__  )(_)(  )(_) ))__)    )   / )__)  /(__)\\  )(_) ))__)  )   /\r\n\t\t \\___)(_____)(____/(____)  (_)\\_)(____)(__)(__)(____/(____)(_)\\_)")
readCode(imagePath)

