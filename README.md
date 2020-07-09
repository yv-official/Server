# Server
Back-end of HBTU Connect App

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
  ![register_req](https://github.com/Logan-47/Server/blob/master/img/register_req.png?raw=true)
  
  > Response
  ![register_req](https://github.com/Logan-47/Server/blob/master/img/register_res.png?raw=true)
    
 ### 2. For login it takes 2 parameters, ```email```, ```password```
   > Request
   ![register_req](https://github.com/Logan-47/Server/blob/master/img/login_req.png?raw=true)
  
   >Response
   ![register_req](https://github.com/Logan-47/Server/blob/master/img/login_res.png?raw=true)
   
   
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
  
