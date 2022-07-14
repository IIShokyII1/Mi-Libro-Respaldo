// sidebar
const sideMenu = document.querySelector("aside");
const menuBtn = document.querySelector("#menu-btn");
const closeBtn = document.querySelector("#close-btn");

menuBtn.addEventListener('click',  () => {
    sideMenu.style.display = 'block';
})

closeBtn.addEventListener('click', () => {
    sideMenu.style.display = "none"
})
//fin sibar//

// Registro de notas//
function Sub(){
    var n, k, r, e, v, t, sum, avg;
    n=(document.getElementById('aname').value);
    k=parseFloat(document.getElementById('am').value);
    r=parseFloat(document.getElementById('aj').value);
    e=parseFloat(document.getElementById('ad').value);
    v=parseFloat(document.getElementById('an').value);
    t=parseFloat(document.getElementById('al').value);

    // Calculating Total
    sum=k+r+e+v+t;
    avg=sum/5;
    // Display on Student Data
    var newTable = document.getElementById('TableScore');
    var row = newTable.insertRow(-1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(0);
    var cell3 = row.insertCell(0);
    var cell4 = row.insertCell(0);

    cell4.innerHTML= n;
    cell3.innerHTML=sum;
    cell2.innerHTML = avg;

    if(avg>=40){
        cell1.innerHTML="<font color=green>Aprobado</font>";
    }else{
        cell1.innerHTML="<font color=red>Reprobado</font>";
    }
}


// Info date
const dateNumber = document.getElementById('dateNumber');
const dateText = document.getElementById('dateText');
const dateMonth = document.getElementById('dateMonth');
const dateYear = document.getElementById('dateYear');

// Tasks Container
const tasksContainer = document.getElementById('tasksContainer');

const setDate = () => {
    const date = new Date();
    dateNumber.textContent = date.toLocaleString('es', { day: 'numeric' });
    dateText.textContent = date.toLocaleString('es', { weekday: 'long' });
    dateMonth.textContent = date.toLocaleString('es', { month: 'short' });
    dateYear.textContent = date.toLocaleString('es', { year: 'numeric' });
};

const addNewTask = event => {
    event.preventDefault();
    const { value } = event.target.taskText;
    if(!value) return;
    const task = document.createElement('div');
    task.classList.add('task', 'roundBorder');
    task.addEventListener('click', changeTaskState)
    task.textContent = value;
    tasksContainer.prepend(task);
    event.target.reset();
};

const changeTaskState = event => {
    event.target.classList.toggle('done');
};

const order = () => {
    const done = [];
    const toDo = [];
    tasksContainer.childNodes.forEach( el => {
        el.classList.contains('done') ? done.push(el) : toDo.push(el)
    })
    return [...toDo, ...done];
}

const renderOrderedTasks = () => {
    order().forEach(el => tasksContainer.appendChild(el))
}

setDate();


