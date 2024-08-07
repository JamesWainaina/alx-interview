# 0x06. Star Wars API

## Overview
This project involves interacting with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. To successfully complete this project, you need to be familiar with several key concepts related to web programming, API interaction, and asynchronous programming in JavaScript.

### Project Details
- **Algorithm**
- **API**
- **JavaScript**

**Weight:** 1  
**Project Duration:** Jul 8, 2024 6:00 AM to Jul 12, 2024 6:00 AM  
**Auto Review:** An auto review will be launched at the deadline.

### In a Nutshell
- **Auto QA review:** 0.0/10 mandatory
- **Altogether:** 0.0%
  - **Mandatory:** 0.0%
  - **Optional:** No optional tasks

### Objectives
The main objective of the project is to retrieve, process, and display Star Wars characters from a specified movie using the Star Wars API. This demonstrates the ability to work with external APIs and manage asynchronous code in JavaScript.

## Concepts Needed
### HTTP Requests in JavaScript
- Understanding how to make HTTP requests to external services using the request module or alternatives like fetch in Node.js.
  - [A Complete Guide to Making HTTP Requests in Node.js](https://nodejs.dev/learn/making-http-requests-with-nodejs)

### Working with APIs
- Understanding the basics of RESTful APIs and how to interact with them.
- Parsing JSON data returned by APIs.
  - [Working with APIs in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)

### Asynchronous Programming
- Managing asynchronous operations with callbacks, promises, and async/await syntax.
- Handling API response data asynchronously.
  - [Asynchronous Programming in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)

### Command Line Arguments in Node.js
- Using the process.argv array to access command-line arguments passed to a Node.js script.
  - [How to Parse Command Line Arguments in Node.js](https://nodejs.dev/learn/nodejs-accept-arguments-from-the-command-line)

### Array Manipulation and Iteration
- Iterating over arrays and manipulating data structures to format and display character names.
  - [JavaScript Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

By familiarizing yourself with these concepts and resources, you will be able to efficiently retrieve, process, and display Star Wars characters from the specified movie using the Star Wars API.

## Additional Resources
- Mock Technical Interview

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS using node (version 10.14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All your files must be executable
- The length of your files will be tested using `wc`
- You are not allowed to use `var`

### More Info
#### Install Node 10
```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
$ sudo npm install semistandard --global
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules

