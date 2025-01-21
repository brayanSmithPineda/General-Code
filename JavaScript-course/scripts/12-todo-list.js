/*
1-Save the input
2- Onclik with the button send
3- save the input in the array
4- display the array in the console
*/
const todoArray = []
function todoElement(){
    const inputElement = document.querySelector('.js-input-1');
    todoArray.push(inputElement.value);
    console.log(todoArray);

    inputElement.value = '';
}

//Practice 2
const todoArray2 = [];

function generateList(){
    let todoListHTML = ''
    for (i = 0 ; i < todoArray2.length ; i++){
        //to create the html with paragrahp with each  todo we use template strings, we can create the todoLIst string without using the p tag, but that will not display each todo in a single line but all together like todo1tod2todo3 
        const html = `<p>${todoArray2[i]}</p>`;
        // we save the html in the todoList
        todoListHTML += html;
    }
    //Once we have the todoList with the paragraph, we just display in our webpay using the dom
    document.querySelector('.todo-name-2').innerHTML = todoListHTML;
}

//we call the function to show the todolist every time we refrest the page
generateList();
function todoElement2(){
    
    const inputElement = document.querySelector('.js-input-2');
    todoArray2.push(inputElement.value);
    inputElement.value = '';
    //we call the function inside the button to show the todolist every time we have a new input
    generateList();
}

//Practice 3

const todoList3 = [{
    todoName : 'todo1',
    dueDate: '02-02-2024'
},{
    todoName : 'todo2',
    dueDate: '01-01-2024'
}];

//Run the code every time we click on the button
document.querySelector('.js-add-button')
    .addEventListener('click', () => {
        todoElement3();
    });

function todoElement3(){
    const toDoElement = document.querySelector('.js-todo-input');
    const dueDateElement = document.querySelector('.js-duedate'); 
    const toDo = toDoElement.value;
    const dueDate = dueDateElement.value;
    todoList3.push({
        todoName: toDo,
        dueDate: dueDate});
    toDoElement.value = '';
    dueDateElement.value = '';
    //we call the function inside the button to show the todolist every time we have a new input
    generateList3();
}

function generateList3(){
    let todoListHTML3 = '';
    todoList3.forEach((todoObject,i) => {
        //we get the name and duedate of each iteration at index i
        const {todoName, dueDate} = todoObject;
        const html = `
        <div> 
        ${todoName}
        </div>
        <div>
        ${dueDate}
        </div>     
        <button class = "css-delete-button js-delete-buttons">
            Delete
        </button>
        `;
        // we save the html in the todoList
        todoListHTML3 += html;
    })
    //Once we have the todoList with the paragraph, we just display in our webpay using the dom
    document.querySelector('.todo-name-3').innerHTML = todoListHTML3;

    //we also can use the addEventListener on the html onclick that we generate with javaScript, in this case we generate a list of buttons so we can just run a for loop in that array and then add the event listener, to select ALL the array of buttons we can loop and the add the event.
    document.querySelectorAll('.js-delete-buttons')
        .forEach((eachButtonElement, index) => {
                eachButtonElement.addEventListener('click', () => {
                todoList3.splice(index,1);
                generateList3();
            });
        });
};

//we call the function to show the todolist every time we refrest the page
generateList3();

