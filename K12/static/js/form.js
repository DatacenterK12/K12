const form = document.getElementById('call-form');
const callthanks = document.querySelector("#call-thanks");
const call = document.querySelector("#call1");
const frm = $('#call-form');
frm.submit(function () {
    $.ajax({
        type: frm.attr('method'),
        url: frm.attr('action'),
        data: frm.serialize(),
        success: function(data){
            call.outerHTML = callthanks.outerHTML;
            },
        error: function (jqXHR, exception) {
            if (jqXHR.status === 400) {
                alert('Слишком большая тема обращения!');
            }
            else {
                alert('Произошла ошибка!');
            }
        }
    });
    return false;
});