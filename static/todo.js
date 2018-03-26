function deleteTask(button) {
        var id = $(button).attr('id');
        console.log('#' + id + '_item')
        $.post(
            "/todo_delete",
            {
                type: "delete",
                task_id: id
            },
            function (data) {
                if (data.success == true) {
                    location.reload();
                }
            }
        );
}
function addTask() {
    var newTask = $("#new-task-input").val();
    $.post(
        "/todo_add",
        {
            type: "add",
            task: newTask
        },
        function (data) {
            if (data.success == true) {
                location.reload();
            }
        }
    )
}