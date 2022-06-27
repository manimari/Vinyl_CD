# Vinyl_CD
API for CD and Vinyl 

We have a database that contains the listed items of a Vinyl and CD store: 

o Table CD : 
▪ Title
▪ Duration
▪ Year of release
▪ Price 

o Table Vinyl : 
▪ Title
▪ Duration
▪ Rotation Speed (Three possible values: 33.3, 45, 78 rpm - revolutions per 
minute)
▪ Year of release
▪ Price 

o Table User : 
▪ Name
▪ Surname
▪ Email
▪ Physical Address


We have an API that provides the following endpoints : 

o http://localhost:5000/cd/get_all  ->  Get every CD from the database 

o http://localhost:5000/vinyl/get_all  ->  Get every Vinyl from the database 

o http://localhost:5000/user/get_all  ->  Get every User from the database 

o http://localhost:5000/cd/add  ->  Add a new CD listing 

o http://localhost:5000/vinyl/add  ->  Add a new Vinyl listing 

o http://localhost:5000/user/add  ->  Add a new User 

o http://localhost:5000/cd/duration_40  ->  Get the CDs with a duration up to 40 minutes 

o http://localhost:5000/vinyl/rotation_speed_45  ->  Get the Vinyls that have a rotation speed of 45 rpm 

o http://localhost:5000/vinyl/modify/<title>/<year>  ->  Modify a Vinyl’s Year of release (eg http://localhost:5000/vinyl/modify/The Wall/1990 )
