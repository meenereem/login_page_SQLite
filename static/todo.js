$(document).ready(function() {
    console.log("loaded index.js");
    $("#remove_task").click(function() {
        var task_id = $("task_id").val();
        $.post(
            "/todo",
            JSON.stringify({
                T_id = task_id
            })
    );
});
});