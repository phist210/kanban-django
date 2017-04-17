$(function() {
  $('.editable').inlineEdit({
    buttonText: 'Add',
    save: function(e, data) {
      return confirm('Change name to '+ data.value +'?');
    }
  });
});

function sortaTable() {

  $( ".big-block" ).sortable({
    connectWith: ".big-block",
    handle: ".portlet-header",
    cancel: ".portlet-toggle",
    placeholder: "portlet-placeholder ui-corner-all",
  });
  $( ".portlet" )
      .addClass( "ui-widget ui-widget-content ui-helper-clearfix ui-corner-all" )
      .find( ".portlet-header" )
      .addClass( "ui-widget-header ui-corner-all" )
      .prepend( "<span class='ui-icon ui-icon-minusthick portlet-toggle'></span>");

  $( ".portlet-toggle" ).on( "click", function() {

    var icon = $( this );
    icon.toggleClass( "ui-icon-plusthick ui-icon-minusthick" );
    icon.closest( ".portlet" ).find( ".portlet-content" ).toggle();
  });
  // console.log($(sdafasdfasdf).serialize());
}

function getTasks() {
  var taskApi = "/task/";
  $.ajax({url: taskApi, success: function(result) {
    var taskLength = result.results.length;

    for(var i = 0; i < taskLength; i++){
      var taskName = result.results[i].name;
      var taskStatus = result.results[i].status;
      var taskPriority = result.results[i].priority;
      var taskID = result.results[i].id;

      if(taskStatus.toLowerCase() === "backlog"){
        $('div.big-block#backlog').append("<div class=portlet id="+ taskID +">" + "<div class=portlet-header>" + taskName + "</div>" + "<div class=portlet-content>" + "Priority level: " + taskPriority + "/10" + "</div>" + "</div>");
      }
      else if (taskStatus.toLowerCase() === "active") {
        $('div.big-block#active').append("<div class=portlet id="+ taskID +">" + "<div class=portlet-header>" + taskName + "</div>" + "<div class=portlet-content>" + "Priority level: " + taskPriority + "/10" + "</div>" + "</div>");
      }
      else if (taskStatus.toLowerCase() === "complete") {
        $('div.big-block#complete').append("<div class=portlet id="+ taskID +">" + "<div class=portlet-header>" + taskName + "</div>" + "<div class=portlet-content>" + "Priority level: " + taskPriority + "/10" + "</div>" + "</div>");
      }
    }
    sortaTable();
    portletEdit();
  }
});
}

$(getTasks)

function portletEdit() {
    $('.portlet-content').on("click", function(){
    var portletID = ($(this).parent().attr('id'));
    var portletStatus = ($(this).parents('.big-block').attr('id'));
    console.log(portletID);
    console.log(portletStatus);
    window.location.replace("/kanban/" + portletID);
  });
}

$("edit_task").submit(function(e){
    $.ajax({
        url: 'task/',
        type: "PUT",
        data: $("edit_task").serialize(),
        cache: false,
        dataType: "text",
        success: function(data){
          console.log('a');
        },
        error: function() {
            console.log("ERROR");
        }
    });
});

$('new_task_form').on('submit', function(event) {
  event.preventDefault();
  console.log("form submitted!");
  new_task();
});

function new_task() {
  $.ajax({
    url: "task/",
    type: "POST",
    data: { new_task: $("#new_task_wrapper").val() },

    success: function(json) {
      $('#new_task_wrapper').val('');
    }
  });
};

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
