$('.wrapper-content').click(function(event){
  console.log("Heyheyhey");
});

$('.add_task').click(function(e){
    console.log(e);
    event.preventDefault();
    $(this).next('.new_task').show();
});
