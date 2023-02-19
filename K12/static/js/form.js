"use strict"

document.addEventListener('DOMContentLoaded', function () {
    const close = document.getElementById('button-close');
    const form = document.getElementById('call-form');
    
    form.addEventListener('submit', function(){
        const call = document.querySelector("#call1");
        call.outerHTML = '<div class="modal-header"><button type="button" class="btn-close" data-bs-dismiss="modal">×</button><h4 class="modal-title">Спасибо за заявку!</h4></div><div class="modal-body" style="background-size: cover"><div class="form-group" style="background-size: cover">Пожалуйста, ожидайте звонка нашего специалиста!</div></div></div>';
    })
    form.addEventListener('submit1', formSend);


});

    
