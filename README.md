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
  
 3. to run the app use the following command ``` flask run ```
