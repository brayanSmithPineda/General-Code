const fs = require('fs');

let movies = JSON.parse(fs.readFileSync('./data/movies.json'));

// Route Handle Functions
exports.getAllMovies = (request, response) => {
    response.status(200).json({
            status: "success",
            requestedAt: request.requestedAt,
            count : movies.length,
            data: {
                movies
            }
        });
};

exports.getMovie = (request, response) => {
    const id = request.params.id*1 //we multiply by 1 to convert it into an int
    const movieObject = movies.find((element) => { return element.id === id})

    //Handle if no id found
    if (!movieObject){
        return response.status(400).json({
            status: 'fail',
            message: 'Movie with ID '+id+' Not Found'
        })
    };
    response.status(200).json({
        status: 'success',
        data: {
            movie: movieObject
        }
    });  
};

exports.updateMovie = (request, response) => {
    let id = request.params.id * 1;
    let movieToUpdate = movies.find((element) => {return element.id === id});

    if (!movieToUpdate){
        return response.status(400).json({
            status: "failed",
            Message: 'Movie with ID '+id+', Not Found'
        });
    };

    index = movies.indexOf(movieToUpdate);
    let movieUpdated = Object.assign(movieToUpdate, request.body); //first argument the object with the new value
    movies[index] = movieUpdated;
    fs.writeFile('./data/movies.json', JSON.stringify(movies), (error) => {
        response.status(200).json({
            status: 'success',
            data: {
                movie: movieUpdated
            }
        });
    });
};

exports.deleteMovie = (request, response) => {
    let id = request.params.id * 1;
    let movieToDelete = movies.find((element) => {return element.id === id});
    let index = movies.indexOf(movieToDelete);

    if(!movieToDelete){ 
        return response.status(400).json({
            status: 'failed',
            message: 'Movie with ID '+id+' not found to delete'
        });
    }

    movies.splice(index, 1); //This delete the element at position index, 1 to just delete 1 element from that position
    fs.writeFile('./data/movies.json', JSON.stringify(movies), (error) => {
        response.status(204).json({ // this 204 status code does not return anything
            status: 'success',
            data: {
                movie: null
            }
        });
    });
};

exports.createMovie = (request, response) => {
    //generating the id
    let newId = movies[movies.length-1].id + 1;
    const newMovie = Object.assign({id: newId}, request.body);

    //We need to push the new movie to the movies array and then write the movies.json
    movies.push(newMovie);
    fs.writeFile('./data/movies.json', JSON.stringify(movies), (error) => {
        response.status(201).json({
            status: 'success',
            data: {
                movie: newMovie
            }
        })
    });
};