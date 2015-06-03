sudo apt-get update && sudo apt-get install python-django && django-admin --version

How to install githum
sudo apt-get update && sudo apt-get install git
git clone https://github.com/mstfmomin/labmonweb.git

git clone https://github.com/mstfmomin/labmonedoc.git

How to install heroku
sudo apt-get install python-setuptools
sudo easy_install pip
sudo pip install virtualenv
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh

git remote add heroku git@heroku.com:labmon.git
heroku run python manage.py runserver



#########################################

sudo apt-get update
sudo apt-get install apache2 php5 php5-mysql mysql-server

mysql -u root -p


CREATE DATABASE my_db;
SELECT VERSION(), CURRENT_DATE;

CREATE USER 'willie'@'localhost' IDENTIFIED BY 'begoode';
GRANT ALL PRIVILEGES ON *.* TO 'willie'@'localhost'
WITH GRANT OPTION;
USE my_db;
SHOW TABLES;
CREATE TABLE my_table (ID int IDENTITY(1,1) PRIMARY KEY, WiFiName varchar(255), WiFiPass varchar(255), DbName varchar(255), TableName varchar(255), UserName varchar(255), UserPass varchar(255), Email varchar(255));

CREATE TABLE my_table (Id int AUTO_INCREMENT primary key NOT NULL, WiFiName varchar(255), WiFiPass varchar(255), DbName varchar(255), TableName varchar(255), UserName varchar(255), UserPass varchar(255), Email varchar(255));


SELECT User FROM mysql.user;
SHOW COLUMNS FROM my_table;
DROP TABLE my_table;


############################################

#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="willie", # your username
                      passwd="begoode", # your password
                      db="my_db") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Drop table if it already exist using execute() method.
cur.execute("DROP TABLE IF EXISTS my_table")

# Create table as per requirement
sql = """CREATE TABLE my_table ( Id INT AUTO_INCREMENT primary key NOT NULL, WiFiName varchar(255), WiFiPass varchar(255),DbName varchar(255),TableName varchar(255),UserName varchar(255),UserPass varchar(255),Email varchar(255))"""

cur.execute(sql)

print "Table has been created"
# disconnect from server
db.close()



##################################################

sudo cp -r /home/pi/Downloads/NoSurprises /var/www/php

###########################################################

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Add Records Form</title>
</head>
<body>
<form action="insert.php" method="post">
    <p>
        <label for="WiFiName">SSID:</label>
        <input type="text" name="WiFiName" id="WiFiName">
    </p>
    <p>
        <label for="WiFiPass">WiFiPass:</label>
        <input type="text" name="WiFiPass" id="WiFiPass">
    </p>
    
    <p>
        <label for="DbName">DbName:</label>
        <input type="text" name="DbName" id="DbName">
    </p>
    <p>
        <label for="TableName">TableName:</label>
        <input type="text" name="TableName" id="TableName">
    </p>
    
    
    <p>
        <label for="UserName">UserName:</label>
        <input type="text" name="UserName" id="UserName">
    </p>
    <p>
        <label for="UserPass">UserPass:</label>
        <input type="text" name="UserPass" id="UserPass">
    </p>
    
    <p>
        <label for="EmailAddress">Email Address:</label>
        <input type="text" name="email" id="EmailAddress">
    </p>
    <input type="submit" value="Add Records">
</form>
</body>
</html>

#####################################
<?php
/* Attempt MySQL server connection. Assuming you are running MySQL
server with default setting (user 'root' with no password) */
$link = mysqli_connect("localhost", "willie", "begoode", "my_db");
 
// Check connection
if($link === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}
 
// Escape user inputs for security
$WiFiName = mysqli_real_escape_string($link, $_POST['WiFiName']);
$WiFiPass = mysqli_real_escape_string($link, $_POST['WiFiPass']);

$DbName = mysqli_real_escape_string($link, $_POST['DbName']);
$TableName = mysqli_real_escape_string($link, $_POST['TableName']);

$UserName = mysqli_real_escape_string($link, $_POST['UserName']);
$UserPass = mysqli_real_escape_string($link, $_POST['UserPass']);

$Email = mysqli_real_escape_string($link, $_POST['Email']);
 
// attempt insert query execution
$sql = "INSERT INTO my_table (WiFiName, WiFiPass, DbName, TableName, UserName, UserPass, Email) VALUES ('$WiFiName', '$WiFiPass', '$DbName', '$TableName', '$UserName', '$UserPass', '$Email')";
if(mysqli_query($link, $sql)){
    echo "Records added successfully.";
} else{
    echo "ERROR: Could not able to execute $sql. " . mysqli_error($link);
}
 
// close connection
mysqli_close($link);
?>



