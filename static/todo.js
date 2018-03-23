$(document).ready(function() {
    // console.log("loaded index.js");
    console.log('hi')
    // $("#remove_task").click(function() {
    //     var task_id = $("task_id").val();

    // );
});
function deleteTask(button) {
    var id = $(button).attr('id');
    console.log('#'+id+'_item')
    $(button).click(function() {
        $('#'+id+'_item').remove();
        $.post(
            "/todo_delete",
            {
                type: "delete",
                task_id: id
            }
        );
    })
}