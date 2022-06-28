# Vinyl_CD
API for CD and Vinyl 

We have a database that contains the listed items of a Vinyl and CD store: 

o Table CD : 
▪ Title - string 
▪ Duration - real number 
▪ Year of release - integer number 
▪ Price - real number 

o Table Vinyl : 
▪ Title - string 
▪ Duration - real number 
▪ Rotation Speed (Three possible values: 33.3, 45, 78 rpm - revolutions per 
minute) - real number 
▪ Year of release - integer number 
▪ Price - real number 

o Table User : 
▪ Name - string 
▪ Surname - string 
▪ Email - string 
▪ Physical Address - string 



We have an API that provides the following endpoints : 

o http://localhost:5000/cd/get_all  ->  Get every CD from the database 

o http://localhost:5000/vinyl/get_all  ->  Get every Vinyl from the database 

o http://localhost:5000/user/get_all  ->  Get every User from the database 

o http://localhost:5000/cd/add  ->  Add a new CD listing 

o http://localhost:5000/vinyl/add  ->  Add a new Vinyl listing 

o http://localhost:5000/user/add  ->  Add a new User 

o http://localhost:5000/cd/duration_40  ->  Get the CDs with a duration up to 40 minutes 

o http://localhost:5000/vinyl/rotation_speed_45  ->  Get the Vinyls that have a rotation speed of 45 rpm 

o http://localhost:5000/vinyl/modify/< title >/< year >  ->  Modify a Vinyl’s Year of release (eg http://localhost:5000/vinyl/modify/The Wall/1990 )



Requests can be done in any way, but if you don't know I suggest Postman. 