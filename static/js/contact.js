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

    var contactForm = document.querySelector('#contact-form')

    // Submit form
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault()
        const name = document.querySelector('#name')
        const email = document.querySelector('#email')
        const message = document.querySelector('#message')

        const form = new FormData()

        form.append('name', name.value)
        form.append('email', email.value)
        form.append('message', message.value)

        fetch('/contact/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            body: form,
        })
            .then(data => data.json())
            .then(resp => {
                if(resp.success){
                    document.querySelector('#contact-form-message').textContent = 'Tu mensaje ha sido enviado correctamente'
                    document.querySelector('#name').value = ''
                    document.querySelector('#email').value = ''
                    document.querySelector('#message').value = ''
                    setTimeout(() => {
                        document.querySelector('#contact-form-message').textContent = ''
                    }, 5000)
                }
            })

    })


})