# This code gets the inputs (name and email address) and save them to columns respectively in the csv file. 

import string
import csv

def main(): 

    file = open("subscriber-list.csv", "a") 
    subname = input("Subscriber Name: ") 
    print(f"[INFO] Subscriber name {subname} written in the file. ")
    subemail = input("Subscriber Email: ")  
    print(f"[INFO] Subscriber email {subemail} written in the file. ")
    
    writer = csv.writer(file)
    writer.writerow([subname, subemail])
    print("[WARNING] Closing the file. ")
    file.close() 
    print("[INFO] File is closed. ")

if __name__ == "__main__": 
    main()