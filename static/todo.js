function deleteTask(button) {
        var id = $(button).attr('id');
        console.log('#' + id + '_item')
        // $('#' + id + '_item').remove();
        $.post(
            "/todo_delete",
            {
                type: "delete",
                task_id: id
            },
        );
}