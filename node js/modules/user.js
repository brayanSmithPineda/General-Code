const events = require('events');

module.exports = class extends events.EventEmitter {
    constructor () { // a constructor is just a special method that runs automatically everytime a new instance of the class is created, is used for set up code
        super(); // the super method calls the parent's class constructor, with this we can extends all the code that is inside the constructor of the EventEmitter class
    }
};