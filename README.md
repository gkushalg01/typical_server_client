# typical_server_client
## what ?
This repo contains namely two files - a server and a client.
Here, as of 2023,  
The Client is written in C++, runs on Linux Ubuntu 20,  
The Server is written in Python, runs on Windows 10.  
The Python server will listen on port '12345' until someone connects,   
After the connection, C++ client sends 6 random coordinates, with each value floating from 0 to 10.  
Upon receiving the coorinates, the Python server will plot these 6 coorindates using matplotlib.  

## why ?
This project is basically showing off tcp communication. Along the line it came to me that how do different programs interact or exchange information with each other like we do in ROS, but ros has simple publisher subscriber and the message is usually custom-defined/pre-built.  
Now, what if I have two simple 1 page programs and I somehow want them to communicate with each other? While using a database is the easiest route, the thing is nobody wants to use a full fledged mongoDB/Postgres just to send 6 floats, lol.  
Using ROS has made communication so easy that I totally forgot about TCP/UDP communication protocol. So, I went and thought how can I make a single program cool enough to display as a project? Then came the idea of this unnecessarily roundabout client-server.  

## how ?
It is currently using TCP communication and is thus, ordered, connection based and accurate.  

