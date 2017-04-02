$(document).ready(function() {
    $('.task_name').editable('http://127.0.0.1:8000/task/4/', {
          indicator : 'Saving...',
          tooltip   : 'Click to edit...'
      });
    $('.task_content').editable('http://127.0.0.1:8000/task/4/', {
        type      : 'textarea',
        cancel    : 'Cancel',
        submit    : 'OK',
        indicator : '<img height=42 width=42 src="static/images/indicator.gif">',
        tooltip   : 'Click to edit...'
    });
})
