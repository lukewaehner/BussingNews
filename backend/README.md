Need: (Postman optional, but recommended as can checkt that API endpoints are working)
MongoDB Atlas. Create a cluster and database, and get the connetion string and slap it in the .env file.

Controllers -> the logic for actions, get, post, put, delete, patch, etc.
Models -> schema for the database
routes -> like a header file
server.js -> main server file. npm run dev starts the server.
main.py -> the secondary backend that needs to be turned into a server. Might just make it so that within server.js the python script server is turned on and everything just works in its own folder to make the project easier to follow. This could be with a child process, but should only be implemented at the very end of development before prod
database -> this just has the stuff to upload stuff to the db. Its run by main.py on execution. It will be run by server.js in the future.
crawlers -> obviously the crawlers, but needs to be refactored
