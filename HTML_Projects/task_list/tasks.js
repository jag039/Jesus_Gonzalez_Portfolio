
function popupFunc(){
    document.getElementById("popup").style.display="block";
}

function closePopup(){
    document.getElementById("popup").style.display="none";
    document.getElementById("newTaskTitle").value = "";
    document.getElementById("newTaskInfo").value = "";
}


function addToList(){
    const list = document.getElementById("task-list");
    let title = document.getElementById("newTaskTitle").value;
    let info = document.getElementById("newTaskInfo").value;

    let taskElement = '\
    <article class="task-entry">\
      <div class="checkbox">\
        <input type="checkbox">\
        <div class="checkmark"></div>\
      </div><div id="txt">' + title + '</div>\
    </article>';

    list.insertAdjacentHTML('afterbegin', taskElement);
    document.getElementById("popup").style.display="none";
    document.getElementById("newTaskTitle").value = "";
    document.getElementById("newTaskInfo").value = "";
}