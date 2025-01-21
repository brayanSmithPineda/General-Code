const app = require('./app');

//Creating the server
const port = 3000;
app.listen(port, () => {
    console.log('server has started');
});
