# AirBnB Clone ― The ALX-Holberton BnB
![Optional Text](hbnb.png)
## Description of the project
The ALX-Holberton B&B project encapsulates the culmination of my intensive four-month software engineering program at ALX-Holberton School. This endeavor aims to replicate the essential features of the renowned [Airbnb Website](https://www.airbnb.com/) using my server.

### Project Components
The final version of this project will comprise the following key elements:
1. Command Interpreter

A command-line interpreter facilitates data manipulation without a visual interface, serving as a valuable tool for development and debugging.
2. Front-end Website

The project includes a dynamic website with both static and dynamic functionalities, providing an engaging user experience.
3. Database

A robust and comprehensive database is integrated to manage the backend functionalities efficiently.
4. API (Application Programming Interface)

An API is implemented to establish a communication interface between the front-end and back-end of the system, ensuring seamless interaction.

## Description of the command interpreter
| Commands  | Description |
| ------------- | ------------- |
| ```quit```  | Quits the console  |
| ```Ctrl+D```  | Quits the console  |
| ```help``` or ```help <command>```  | Displays all commands or Displays instructions for a specific command
| ```create <class>```  | Creates an object of type , saves it to a JSON file, and prints the objects ID
| ```show <class> <ID>```  | Shows string representation of an object
| ```destroy <class> <ID>```  | Deletes an objects
| ```all or all <class>```  | Prints all string representations of all objects or Prints all string representations of all objects of a specific class
| ```update <class> <id> <attribute name> "<attribute value>"```  | Updates an object with a certain attribute (new or existing)
| ```<class>.all()```  | Same as all ```<class>```
| ```<class>.count()```  | Retrieves the number of objects of a certain class
| ```<class>.show(<ID>)```  | Same as show ```<class> <ID>```
| ```<class>.destroy(<ID>)```  | Same as destroy ```<class> <ID>```
| ```<class>.update(<ID>, <attribute name>, <attribute value>```  | Same as update ```<class> <ID> <attribute name> <attribute value>```
| ```<class>.update(<ID>, <dictionary representation>)```  | Updates an objects based on a dictionary representation of attribute names and values

## General Execution
Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```