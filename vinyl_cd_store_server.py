from flask import Flask, jsonify, request 
import sqlite3 
import os  

#Global variables 
current_working_directory=os.getcwd()+"\\" #In Windows we have \\ . In other systems (eg. ios, android linux) we have / .
database_file_name=current_working_directory+"data\\vinyl_cd_store.db"  

def check_file_existence(file_link) : 
    return os.path.isfile(file_link) #It returns true or false 

#Function to create the database with the three Tables - CD, Vinyl, User 
def create_db() : 
    con = sqlite3.connect(database_file_name)
    try : 
        query = """Create Table CD
            (title varchar(100) not NULL primary key, 
            duration real, 
            year_release int, 
            price real  
            );"""  
        cursor = con.cursor() 
        cursor.execute(query) 
        query = """Create Table Vinyl
            (title varchar(100) not NULL primary key, 
            duration real, 
            rotation_speed real check (rotation_speed = 33.3 or rotation_speed = 45 or rotation_speed = 78), 
            year_release int, 
            price real  
            );"""   
        cursor = con.cursor() 
        cursor.execute(query)   
        query = """Create Table User 
            (name varchar(100), 
            surname varchar(100), 
            email varchar(100) not NULL primary key, 
            physical_address varchar(100)  
            );"""   
        cursor = con.cursor() 
        cursor.execute(query)   
    except : 
        print("An exception occurred") 
    con.close() 

#Function to get all the data of the Table CD 
def get_all_cd(): 
    con = sqlite3.connect(database_file_name) 
    try : 
        query = f"Select * from CD" 
        cursor = con.cursor() 
        cursor.execute(query) 
        all_cds = cursor.fetchall() 
    except : 
        print("An exception occurred") 
    con.close() 
    return all_cds  

#Function to get all the data of the Table Vinyl 
def get_all_vinyl(): 
    con = sqlite3.connect(database_file_name) 
    try : 
        query = f"Select * from Vinyl" 
        cursor = con.cursor() 
        cursor.execute(query) 
        all_vinyl = cursor.fetchall() 
    except : 
        print("An exception occurred") 
    con.close() 
    return all_vinyl 

#Function to get all the data of the Table User 
def get_all_user(): 
    con = sqlite3.connect(database_file_name) 
    try : 
        query = f"Select * from User" 
        cursor = con.cursor() 
        cursor.execute(query) 
        all_user = cursor.fetchall() 
    except : 
        print("An exception occurred") 
    con.close() 
    return all_user  

#Function to add the data of a new CD into the Table CD 
def insert_one_cd(title, duration, year_release, price) : 
    con = sqlite3.connect(database_file_name) 
    try : 
        query = f"""Insert Into CD (title, duration, year_release, price) values('{title}', '{duration}', '{year_release}', '{price}')"""
        cursor = con.cursor() 
        cursor.execute(query)   
        con.commit() 
    except : 
        print("An exception occurred") 
    con.close()  


#Function to add the data of a new Vinyl into the Table Vinyl 
def insert_one_vinyl(title, duration, rotation_speed, year_release, price) : 
    con = sqlite3.connect(database_file_name) 
    try : 
        query = f"""Insert Into Vinyl (title, duration, rotation_speed, year_release, price) values('{title}', '{duration}', '{rotation_speed}', '{year_release}', '{price}')"""
        cursor = con.cursor() 
        cursor.execute(query)   
        con.commit() 
    except : 
        print("An exception occurred") 
    con.close()  


#Function to add the data of a new user into the Table User 
def insert_one_user(name, surname, email, physical_address) : 
    con = sqlite3.connect(database_file_name) 
    try : 
        query = f"""Insert Into User (name, surname, email, physical_address) values('{name}', '{surname}', '{email}', '{physical_address}')"""
        cursor = con.cursor() 
        cursor.execute(query)   
        con.commit() 
    except : 
        print("An exception occurred") 
    con.close()  

#Function to get all the data of the CDs of the table CD with the constraint that the duration is less or equal to 40 
def get_cd_duration40(): 
    con = sqlite3.connect(database_file_name) 
    try : 
        query = "Select * from CD where duration <= 40" 
        cursor = con.cursor() 
        cursor.execute(query) 
        all_cds_duration40 = cursor.fetchall() 
    except : 
        print("An exception occurred") 
    con.close() 
    return all_cds_duration40  


#Function to get all the data of the Vinyls of the table Vinyl with the constraint that the rotation speed is equal to 45 
def get_vinyl_rotationspeed45(): 
    con = sqlite3.connect(database_file_name) 
    try : 
        query = "Select * from Vinyl where rotation_speed = 45" 
        cursor = con.cursor() 
        cursor.execute(query) 
        all_vinyl_rotationspeed45 = cursor.fetchall() 
    except : 
        print("An exception occurred") 
    con.close() 
    return all_vinyl_rotationspeed45 


#Function to update the element year_release of the table Vinyl  
def modify_vinyl_year_release(title, year): 
    con = sqlite3.connect(database_file_name) 
    try : 
        query = f"""Update Vinyl set year_release = '{year}' where title = '{title}'""" 
        cursor = con.cursor() 
        cursor.execute(query) 
        con.commit() 
    except : 
        print("An exception occurred") 
    con.close()   

#Since the database is created once, we check if it already exists, if not then we create it 
if check_file_existence(database_file_name) == False : 
    create_db() 

#Initialization of server 
app=Flask(__name__) 

#Endpoints 

#Endpoint to get all the CDs. It returns the data of the CDs and a corresponding message 
@app.route("/cd/get_all/",methods=["GET"]) 
def all_cd() : 
    dict_to_send = {} 
    dict_to_send["data"] = get_all_cd() 
    dict_to_send["message"]='These are all the CDs of the database.'
    return jsonify(dict_to_send) 

#Endpoint to get all the Vinyls. It returns the data of the Vinyls and a corresponding message 
@app.route("/vinyl/get_all/",methods=["GET"]) 
def all_vinyl() : 
    dict_to_send = {} 
    dict_to_send["data"] = get_all_vinyl()  
    dict_to_send["message"]='These are all the Vinyls of the database.'
    return jsonify(dict_to_send) 

#Endpoint to get all the users. It returns the data of the Users and a corresponding message 
@app.route("/user/get_all/",methods=["GET"]) 
def all_user() : 
    dict_to_send = {} 
    dict_to_send["data"] = get_all_user()   
    dict_to_send["message"]='These are all the users of the database.'
    return jsonify(dict_to_send) 

#Endpoint to add a new CD into the database. It returns a corresponding message 
@app.route("/cd/add/",methods=["POST"])
def cd_add(): 
    new_cd = request.get_json() 
    dict_to_send = {} 
    insert_one_cd(new_cd["title"], new_cd["duration"], new_cd["year_release"], new_cd["price"])
    dict_to_send["message"]=f'The CD with title {new_cd["title"]} has been added.'
    return jsonify(dict_to_send) 

#Endpoint to add a new Vinyl into the database. It returns a corresponding message 
@app.route("/vinyl/add/",methods=["POST"])
def vinyl_add(): 
    new_vinyl = request.get_json() 
    #Check if the rotation speed is equal to one of the three possible values. If not it returns an error message 
    if new_vinyl["rotation_speed"] != 33.3 and new_vinyl["rotation_speed"] != 45 and new_vinyl["rotation_speed"] != 78 : 
        return jsonify({"Error" : "Three possible values for the rotation speed : 33.3, 45, 78 rpm"}), 401
    else : 
    #In this case the rotation speed is equal to one of the three possible values 
        dict_to_send = {} 
        insert_one_vinyl(new_vinyl["title"], new_vinyl["duration"], new_vinyl["rotation_speed"], new_vinyl["year_release"], new_vinyl["price"])
        dict_to_send["message"]=f'The Vinyl with title {new_vinyl["title"]} has been added.'
        return jsonify(dict_to_send) 

#Endpoint to add a new user into the database. It returns a corresponding message 
@app.route("/user/add/",methods=["POST"])
def user_add(): 
    new_user = request.get_json() 
    dict_to_send = {} 
    insert_one_user(new_user["name"], new_user["surname"], new_user["email"], new_user["physical_address"]) 
    dict_to_send["message"]=f'The user {new_user["name"]} {new_user["surname"]} has been added.'
    return jsonify(dict_to_send) 

#Endpoint to get all the CDs with a duration up to 40 Minutes. It returns the data of the CDs, that satisfy the constraint, and a corresponding message 
@app.route("/cd/duration_40/",methods=["GET"]) 
def cd_duration() : 
    dict_to_send = {} 
    dict_to_send["data"] = get_cd_duration40()  
    dict_to_send["message"]='These are all the CDs of the database with a duration up to 40 Minutes.'
    return jsonify(dict_to_send) 

#Endpoint to get all the Vinyls with a rotation speed of 45 rpm. It returns the data of the Vinyls, that satisfy the constraint, and a corresponding message
@app.route("/vinyl/rotation_speed_45/",methods=["GET"]) 
def vinyl_rotationspeed() : 
    dict_to_send = {} 
    dict_to_send["data"] = get_vinyl_rotationspeed45()  
    dict_to_send["message"]='These are all the Vinyls of the database that have a rotation speed of 45 rpm.'
    return jsonify(dict_to_send) 

#Endpoint to modify the year of release of the Vinyl that is recognized by the title. It returns a corresponding message
@app.route("/vinyl/modify/<title>/<year>/",methods=["POST"])
def vinyl_modify_year(title, year): 
    all_vinyl = get_all_vinyl() 
    x = False  
    #We look at all the Vinyls and check if the title that is given by the user equals to one of the title of the Vinyls of the DB
    for i in range(len(all_vinyl)) : 
        if title == all_vinyl[i][0] : 
            x = True 
    if x == False : #If the title doesn't exist then an error message is returned 
        return jsonify({"Error" : f"There is no Vinyl with the title {title}"}), 401  
    else : #In this case the title exists and we modify the year by calling the corresponding function. A corresponding message is then retuned 
        dict_to_send = {} 
        modify_vinyl_year_release(title, year)
        dict_to_send["message"]=f'The year of release of the Vinyl with {title} has been modified to {year}.'            
        return jsonify(dict_to_send) 

if __name__=="__main__":
    port=5000 #This is the port that flask has automatically 
    app.run(port=port,debug=True)  #debug=True only for the programmer  
