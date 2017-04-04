
// $('.wrapper-content').click(function(event){
//   console.log("Heyheyhey");
// });

function getTasks() {
  var taskApi = "http://localhost:8000/task/";
  $.ajax({url: taskApi, success: function(result) {
    var taskLength = result.results.length;

    for(var i = 0; i < taskLength; i++){
      var taskName = result.results[i].name;
      var taskStatus = result.results[i].status;
      var taskPriority = result.results[i].priority;
      var taskID = result.results[i].id;
      console.log(taskID);

      if(taskStatus.toLowerCase() === "backlog"){
        $('div.big-block#backlog').append("<div class=wrapper-content id="+ taskID +">" + "<h3>" + taskName + "</h3>" + "Priority level: " + taskPriority + "/10" + "</div>");
      }
      else if (taskStatus.toLowerCase() === "active") {
        $('div.big-block#active').append("<div class=wrapper-content id="+ taskID +">" + "<h3>" + taskName + "</h3>" + "Priority level: " + taskPriority + "/10" + "</div>");
      }
      else if (taskStatus.toLowerCase() === "complete") {
        $('div.big-block#complete').append("<div class=wrapper-content id="+ taskID +">" + "<h3>" + taskName + "</h3>" + "Priority level: " + taskPriority + "/10" + "</div>");
      }
    }
  }
});
}

getTasks();

$('.big-block').on('click', function() {
  console.log("clicked");
});



$('new_task_form').on('submit', function(event) {
  event.preventDefault();
  console.log("form submitted!");
  new_task();
});

function new_task() {
  // console.log("create post is working");
  // console.log($('#new_task_wrapper').val());
  $.ajax({
    url: "task/",
    type: "POST",
    data: { new_task: $("#new_task_wrapper").val() },

    success: function(json) {
      $('#new_task_wrapper').val('');
      // console.log(json);
      // console.log('success');
    }
    // error: function(xhr, errmsg, err) {
    //   $('#container').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
    //             " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
    //         console.log(xhr.status + ": " + xhr.responseText);
    // }
  });
};


// $('new_task_form').on('submit', function(event) {
//   event.preventDefault();
//   console.log("form submitted!");
//   new_task();
// });

function edit_task() {
  console.log("create post is working");
  console.log($('#new_task_wrapper').val());
  $.ajax({
    url: "task/",
    type: "PUT",
    data: { new_task: $("#new_task_wrapper").val() },

    success: function(json) {
      $('#new_task_wrapper').val('');
    }
  });
};
//
// // // ------------ v Popup window for new task v -------------
// // Get the modal
// var modal = document.getElementById('myModal');
//
// // Get the button that opens the modal
// var btn = document.getElementById("myBtn");
//
// // Get the <span> element that closes the modal
// var span = document.getElementsByClassName("close")[0];
//
// // When the user clicks the button, open the modal
// btn.onclick = function() {
//     modal.style.display = "block";
// }
//
// // When the user clicks on <span> (x), close the modal
// span.onclick = function() {
//     modal.style.display = "none";

// -------------Popup window for new task--------------

// Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
