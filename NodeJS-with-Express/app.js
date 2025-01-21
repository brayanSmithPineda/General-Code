const express = require('express');
const morgan = require('morgan');
const moviesRouter = require('./Routes/moviesRoutes');

let app = express();

app.use(express.json()); //This middleware parses JSON bodies into Javascript
app.use(morgan('dev')); //This third party middleware console.log the method, path, status code, time and space of the HTTP requests

//This custom middleware is to assign the time when the request was made, request.requestedAt is just a new property we define as an object of the Date class, the data class returns the current data and time, to ISOString formats the data in yyyy/mm/dd hh/mm
app.use((request, response, next) => {
    request.requestedAt = new Date().toLocaleString();
    next();
});

//Router Middleware
app.use('/api/v1/movies',moviesRouter)

module.exports = app;