"use strict"

document.addEventListener('DOMContentLoaded', function () {
    const close = document.getElementById('button-close');
    const form = document.getElementById('form-call');

    form.addEventListener('submit', function(){
        form.style.visibility = 'hidden';
        const success = document.getElementById('modal-success');
        success.classList.add('show');
        success.style.visibility = 'visible';
        close.style.visibility = 'visible';
        // close.click();
    })
    form.addEventListener('submit', formSend);

    async function formSend(e) {
        e.preventDefault();

        let formData = new FormData(form);

            let response = await fetch ('sendmail.php', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                let result = await response.json();
                alert(result.message);
                form.reset();
            } else {
                alert('Ошибка!');
            }
        
    }
});

    
