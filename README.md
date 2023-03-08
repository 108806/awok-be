THINGS TO KNOW BEFORE DEPLOYMENT:

There are two branches, master is for the local which is the default branch, acts as staging/testing, and heroku, which is default production branch atm.

There are setup and run scripts, the ones with .bat are for the windows, and .sh is for the linux.

In production we are using gunicorn server as the default django server is not suitable for production, 
    but it can not be used on windows because it requires fcntl headers which are linux specific, 
    it can be used with WSL though, or HyperV or any other linux VMs.




BUGS AND TRAPS IN DRF DOCS:

Views need the JWTAuthentication in authentication_classes despise the simple-jwt docs.

Inheriting generics.UpdateAPIView in UserUpdateView allows to change the email address, even though it is not specified in the serializer class, db contamination possible.




INSTALLATION and LAUNCHING:

unzip the .env file with provided password, start terminal, and run setup
