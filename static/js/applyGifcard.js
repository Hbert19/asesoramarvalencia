document.addEventListener('DOMContentLoaded', () => {

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    document.querySelector('#gifcard-code').addEventListener('input', (e) => {
        if (e.target.value.length == 4) {
            e.target.value += '-'
        } else if (e.target.value.length == 9) {
            e.target.value += '-'
        }
    })

    document.querySelector('#redeem').addEventListener('click', () => {
        if (document.querySelector('#gifcard-code').value.length < 14) {
            document.querySelector('#error-gifcard').textContent = 'El código de la gifcard debe contener 14 caracteres'
        }
        var code = document.querySelector('#gifcard-code')
        var productId = document.querySelector('.product').getAttribute('data-product')
        var form = new FormData()
        form.append('gifcard', code.value)
        form.append('productId', productId)
        fetch('/gifcard/redeem/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            mode: 'same-origin',
            body: form
        })
            .then(data => data.json())
            .then(resp => {
                console.log(resp)
                if(resp.error){
                    document.querySelector('#error-gifcard').textContent = resp.error
                }else{
                    document.querySelector('.modal-footer').remove()
                    document.querySelector('.gifcard-form').innerHTML = ""
                    document.querySelector('.gifcard-form').innerHTML = `
                    <p style="font-size: 14px; text-align: center; color: black;">${resp.success}</p>
                    <div class="text-center">
                        <a class="btn btn-mar" href="https://api.whatsapp.com/send?phone=34612474373&text=Hola%20Mar%20acabo%20de%20realizar%20un%20pedido%20en%20tu%20sitio%20web%20y%20el%20numero%20de%20pedido%20es%20${resp.order}" target="_blank" "="">Notificar pago ahora</a>
                    </div>`
                }
            })
    })
})