# Server
Back-end of HBTU Connect App

## For Quick Development Set-up
Install Docker and Docker Compose on your machine.
And run the following command

1. create a ```.flaskenv``` file in root directory.
  and add following content to it.
  ```
    FLASK_APP=server
    FLASK_ENV=development
  ```
2. create a ```.env``` file in root directory.
  and add following content to it.
  ```
   SECRET_KEY=<YOUR SECRET KEY>
   JWT_SECRET_KEY=<YOU JWT SECRET KEY>
   MONGO_URI=<YOUR MONGODB CONNECT URI STRING>
  ```
3. Build the server container image in the docker host with all the requirements installed in it.
  ```
    docker build . server
  ```

4. Start the development server inside the docker container on the port 5000
```
  docker run -it -p 5000:5000 -v $(pwd):/server server
```

5.  You can access the api at any of the mentioned address
  -  [http://localhost:5000](http://localhost:5000)
  -  [http://172.17.0.2:5000](http://172.17.0.2:5000)

## Normal Set-up

1. create a ```.flaskenv``` file in root directory.
  and add following content to it.
  ```
    FLASK_APP=server
    FLASK_ENV=development
  ```
2. create a ```.env``` file in root directory.
  and add following content to it.
  ```
   SECRET_KEY=<YOUR SECRET KEY>
   JWT_SECRET_KEY=<YOU JWT SECRET KEY>
   MONGO_URI=<YOUR MONGODB CONNECT URI STRING>
  ```
 
 ``` CORS origins are put under the /server/config.py in origins list ```
 
 3. to install all the dependencies.
    
    ``` pip install -r requirements.txt ```
 
 3. to run the app use the following command ``` flask run ```
 
 # API Specifications
 
 1. ``` /api/register ``` : to register an user.
 2. ``` /api/login ```: for logging in a user.
 3. ``` /api/logout/access ```: to revoke access token
 4. ``` /api/logout/refresh ```: to revoke refresh token
 5. ``` /api/token/refresh ```: use refresh token to get new access token
 

## How to Use APIs [Examples Using POSTMAN]

### 1. For registration it takes three parameters, ```username```, ```email```, ```password```.
  > Request
  ```
    {
      "username": "test",
      "email": "admin@test.com",
      "password": "password",
      "rollNumber": "170000001"
      "firstName": "test",
      "lastName": "admin",
      "phone": "9000000000",
      "branch": "cse",
      "year": "first",
      "gender": "male"
    }
  ```
  
  > Response
  ```
    {
      access_token:"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTQ4Mjk0NDcsIm5iZiI6MTU5NDgyOTQ0NywianRpIjoiYzAxZjIwZjctOGUwOS00YjMzLWI5YjEtYjEzZWUwNTgxNDAyIiwiZXhwIjoxNTk0OTE1ODQ3LCJpZGVudGl0eSI6IjE3MDEwNDA2NUBoYnR1LmFjLmluIiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.RtmztSPxoIyOex1Ozu3ins2wMuUZse-wlkONAK-jFN0"
      msg:"User with username yv_official has been successfully created"
      username:"yv_official"
      refresh_token:"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTQ4Mjk0NDcsIm5iZiI6MTU5NDgyOTQ0NywianRpIjoiMTVkMzI1OTItOTQyZS00ZDViLWI5YzAtMzFlMTY3OTc5ODE4IiwiZXhwIjoxNTk3NDIxNDQ3LCJpZGVudGl0eSI6IjE3MDEwNDA2NUBoYnR1LmFjLmluIiwidHlwZSI6InJlZnJlc2gifQ.H1gZ0qGr6qeU6-7Wd24nZ3pJDINMG_mrl9yoMfz-04g"
    }
  ```
  
 ### 2. For login it takes 2 parameters, ```email```, ```password```
   > Request
   ```
    {
      "username": "test",
      "password": "password"
    }
   ```
  
   >Response
   ```
    {
      access_token:"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTQ4Mjk0NDcsIm5iZiI6MTU5NDgyOTQ0NywianRpIjoiYzAxZjIwZjctOGUwOS00YjMzLWI5YjEtYjEzZWUwNTgxNDAyIiwiZXhwIjoxNTk0OTE1ODQ3LCJpZGVudGl0eSI6IjE3MDEwNDA2NUBoYnR1LmFjLmluIiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.RtmztSPxoIyOex1Ozu3ins2wMuUZse-wlkONAK-jFN0"
      msg:"Logged in as test"
      name:"test admin"
      refresh_token:"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTQ4Mjk0NDcsIm5iZiI6MTU5NDgyOTQ0NywianRpIjoiMTVkMzI1OTItOTQyZS00ZDViLWI5YzAtMzFlMTY3OTc5ODE4IiwiZXhwIjoxNTk3NDIxNDQ3LCJpZGVudGl0eSI6IjE3MDEwNDA2NUBoYnR1LmFjLmluIiwidHlwZSI6InJlZnJlc2gifQ.H1gZ0qGr6qeU6-7Wd24nZ3pJDINMG_mrl9yoMfz-04g"
      userId:"5f0b5f328bf03756503c7959"
      username:"test"
    }
   ```
   
   
## To Given tokens as input to the API you have to send a header whose
  Key will be ``` Authorization ``` and
  value will be ``` Bearer <YOUR TOKEN> ```
   
 ### 3. To get new access token using refresh token
  > Request
  ![register_req](https://github.com/Logan-47/Server/blob/master/img/refresh_req.png?raw=true)
  
  >Response
  ![register_req](https://github.com/Logan-47/Server/blob/master/img/refresh_res.png?raw=true)
  
  ### 4. To revoke access token
   > Request
  ![register_req](https://github.com/Logan-47/Server/blob/master/img/lo_access_req.png?raw=true)
  
  >Response
  ![register_req](https://github.com/Logan-47/Server/blob/master/img/lo_access_res.png?raw=true)
  
  ### 5. To revoke refresh token
   > Request
  ![register_req](https://github.com/Logan-47/Server/blob/master/img/lo_refresh_req.png?raw=true)
  
  >Response
  ![register_req](https://github.com/Logan-47/Server/blob/master/img/lo_refresh_res.png?raw=true)
  
