# reverse-polish-notation
This project is a calculator using [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation). It is in the form of a  commandline utility accepting input through Posix pipes, arguments on the commandline, and through the provided interactive mode.

## Technical Design
### Architecture
The architecture of this utility as currently implemented is monolithic.  It is run inside a single process. To help with further separation of concerns, there is an added step that converts all communication between front end and back end to JSON.   
#### Modules
- `rpn_calculator` provides the basic functionality of evaluating a reverse polish notation stack like `[1.0, 2.0, 3.0, "+"]` and returning the simplified stack.  In this case the return value is a stack like `[1.0, 5.0]`.
- `rpn_user` provides the commandline UI.  It handles taking input from pipes, args, and user interaction.
- `rpn_shared` has parsing code that is used by `rpn_user` and any future python consumer of the `rpn_calculator` module
- `rpn_operators` is simply a mapping between the string that encodes the operation and the function that performs it.



### Trade offs
- using Python as the development platform means we traded type safety for quickly coding a prototype
- The JSON conversion is not implemented as a separate layer because 1. there would only be two functions, and they would be one-liners and 2. JSON is so widely supported, there is no conceivable reason to switch it out for another data format. 
### Omissions
- Help inside the interactive mode
### Next steps
- add some explanation inside interactive mode.
- make a small Rest API with Flask. Use the calculator module on the server.

## Usage
### Interactive Mode  
```
$ python3 ./rpn_user.py  
$ [] > 2 3 +  
$ [5.0] >
```

### Commandline Arguments  
```
$ python3 ./rpn_user.py 2 3 +
```

### Pipes on Posix  
```
$ echo '2 3 +' | python3 ./rpn_user.py -
```
> Don't forget the dash at the end!


