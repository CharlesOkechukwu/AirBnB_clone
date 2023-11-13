# AirBnB_clone
![hbnb picture](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231113%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231113T150540Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bd53754a5e74e5337c28cb61791d21f1c9e95cea3e1644d739f8ba2ee23473e9)

## Description
 Welcome to the AirBnB clone project.
 The goal of the project is to deploy on your server a simple copy of the [AirBnB website]("https://www.airbnb.com/").

 This repository will focus on building a command interpreter using python [cmd](https://docs.python.org/3/library/cmd.html) module to manipulate data without a visual interface and building and defining classes.

 
### Features of this project

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

This repo focuses on building the first feature.

 
## Table of Contents

- [Description](#AirBnB_clone)
- [Repository Content](#Repository-Contents)
- [Development Enviroment](#contributing)
- [Installation](#installation)
- [Example Usage](#example-usage)
- [Tests](#tests)
- [Acknowlegement](#acknowledgement)
- [Authors](#authors)

## Repository Contents
The repository contains the following files.

| File/Folder | Description                           |
| ------------ | ------------------------------------- |
| AUTHORS      | List of project authors               |
| README.md    | Project documentation                 |
| base_model    | Defines the class BaseModel; which is the parent class |
| console.py   | Main console script. see [Example Usage](#example-usage)                  |
| amenity.py | Defines the subclass Amenity             |
| base_model.py | Defines the subclass Base              |
| city.py | Defines the subclass City                    |
| file_storage.py | Defines the class FileStorage class(file storage engine)    |
| place.py | Defines the subclass Place                  |
| review.py | Defines the subclass Review                |
| state.py | Defines the subclass State                  |
| user.py | Defines the subclass User                    |

## Development Enviroment
The console was developed in Ubuntu 20.04.6LTS using python3 (version 3.8.10).

Note: This is not a strict requirement

## Installation

Clone the repository
```bash
$ https://github.com/Abdulmohusain/AirBnB_clone.git
```

## List of commands

The following commands is all you need to create update and manipulate objects. Few but effective commands.


**create**
```
$ create <Class Name>  
```
Creates object of given class. The classes include
- BaseModel 
- User 
- Amenity
- Place
- City
- Review
- State

**show**
```
$ show <Class Name>  <Instance Id>
```
Prints the string representation of an instance based on the class name and id

**all**
```
$ all   
```
Prints all string representation of all instances based or not on the class name

**update**
```
$ update <Class Name> <Instance Id>  <Attribute Name> <Value>
```
Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)

**destroy**
```
$ destroy <Class Name>  <Instance Id>
```
Deletes an instance based on the class name and id (save the change into the JSON file)

**count**
```
$ count
```
Retrieve the number of instances of a class

**help**

```
$ help <command>   
```
Prints information about specific command

**quit/ EOF**

```
$ quit   
```	
Exit the program

## Example Usage
Example 1
```bash
$ https://github.com/Abdulmohusain/AirBnB_clone.git
```
```bash
$ cd AirBnB_clone
```
```bash
$ ./console.py
```
```bash
(hbnb)
(hbnb) all
** class doesnt exist **
(hbnb) show BaseModel My_First_Model
** no instance found **
hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) quit
```
```bash
$ 
```

## Test
```
$ python -m unittest discover tests
```
### Acknowledgement
 This projects is dedicated to our pairs and mentors.

## Authors
- [Abdullahi Mohammed Hsain](https://github.com/Abdulmohusain)
- [ Charles Okechukwu](https://github.com/CharlesOkechukwu)
