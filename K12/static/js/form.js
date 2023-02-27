"use strict"

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('call-form');
    const callthanks = document.querySelector("#call-thanks");
    form.addEventListener('submit', function(){
        const call = document.querySelector("#call1");
        call.outerHTML = callthanks.outerHTML;
    })
    form.addEventListener('submit1', formSend);


});

    
