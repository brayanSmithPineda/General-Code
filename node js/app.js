const http = require("http");
const fs = require("fs");
const url = require("url");
const { log } = require("console");
const placeHolderHandler = require('./modules/placeHolder');

const html = fs.readFileSync("./templates/01-basics.html", "utf-8");
const productsArray = JSON.parse(fs.readFileSync("./data/products.json", "utf-8"));
const productsArraysHTML = fs.readFileSync("./templates/product-list.html","utf-8");
const productDetail = fs.readFileSync("./templates/product-detail.html","utf-8");

//Step 1 create the server
const server = http.createServer();

/*
server.on('request', (request, response) => {
  
  let { query, pathname: path } = url.parse(request.url, true);
  console.log(productsArray);
  
  // let path = request.url;
  if (path === "/" || path.toLocaleLowerCase() === "/home") {
    response.writeHead(200, {
      "Content-Type": "text/html",
      "My-Custom-Header": "this is my custom header",
    });
    response.end(html.replace("{{%CONTENT%}}", "You are in Home Page"));
  } else if (path.toLocaleLowerCase() === "/about") {
    response.writeHead(200, {
      "Content-Type": "text/html",
      "My-Custom-Header": "this is my custom header",
    });
    response.end(html.replace("{{%CONTENT%}}", "This is the about page"));
  } else if (path.toLocaleLowerCase() === "/contact") {
    response.writeHead(200, {
      "Content-Type": "text/html",
      "My-Custom-Header": "this is my custom header",
    });
    response.end(html.replace("{{%CONTENT%}}", "This is the Contact page"));
  } else if (path.toLocaleLowerCase() === "/products") {
    if (!query.id) {
      response.writeHead(200, {
        "Content-Type": "text/html",
        "My-Custom-Header": "this is my custom header",
      });
      let productHTMLArray = productsArray.map((productArray) => {
        return placeHolderHandler(productsArraysHTML, productArray);
      });
      response.end(html.replace("{{%CONTENT%}}", productHTMLArray.join(",")));
    } else {
      response.writeHead(200, {
        "Content-Type": "text/html",
        "My-Custom-Header": "this is my custom header",
      });
      let productFound = productsArray.find(product => product.id === Number(query.id));
      console.log(productFound);
      response.end(html.replace("{{%CONTENT%}}",placeHolderHandler(productDetail, productFound)));
      
      
    }
  } else {
    response.writeHead(404, {
      "Content-Type": "text/html",
      "My-Custom-Header": "this is my custom header",
    });
    response.end("Error 404: Page not found");
  }
});
*/
// Step 2 -- Listen to the server, basically means to start the server, without this the server will not work

server.listen(8000, "127.0.0.1", () => {
  console.log("served has started");
});

// Custom events
const user = require('./modules/user');
const myEmitter = new user();

myEmitter.on('userCreated', () => {
  console.log('user added to database');
});

myEmitter.emit('userCreated');


// Streaming events
/*
server.on('request', (request, response) => {
  let rs = fs.createReadStream('./file/large-file.txt');
  rs.on('data',(chunk) => {
    response.write(chunk);
  });
  rs.on('end', () => {
    response.end('we finish the entire file');
  })

  rs.on('error', (error) => {
    response.end(error.message);
  })
})
*/
server.on('request', (request, response) => {
  let rs = fs.createReadStream('./file/large-file.txt');
  rs.pipe(response);
});
console.log('program has started');
setTimeout(() => {
  console.log('setTimeout is in the 1 phase of the event loop'); 
},100);

setImmediate(()=>{
  console.log('setImmediate is in the 3 phase');
  
})
console.log('Program has clomplete');

