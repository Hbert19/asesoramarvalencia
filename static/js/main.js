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

    function getPrice() {
        var form = new FormData()
        form.append('id', document.querySelector('.product').getAttribute('data-product'))
        return fetch('/products/get-price/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            body: form
        })
            .then(data => {
                return data.json()
                    .then(resp => {
                        return resp
                    })
            })
    }

    getPrice().then(resp => {
        /* PayPal Integration */
        paypal.Button.render({
            // Configure environment
            env: 'sandbox',
            client: {
                sandbox: 'AQ8kTd3nSrCW4_WsrCo3jTtSh64zs3p8LQTeDAlCPzvpN9AwaXUGiGHGpO1BhcDPcIYx5nDrHZM6u1GX',
                production: 'demo_production_client_id'
            },

            // Customize button (optional)
            locale: 'en_US',
            style: {
                size: 'responsive',
                color: 'black',
                shape: 'pill',
                label: 'paypal',
                tagline: false,
                layout: 'vertical',
            },
            funding: {
                allowed: [paypal.FUNDING.CARD],
                disallowed: [paypal.FUNDING.CREDIT]
            },

            // Enable Pay Now checkout flow (optional)
            commit: true,

            // Set up a payment
            payment: function (data, actions) {
                return actions.payment.create({
                    transactions: [{
                        amount: {
                            total: resp.price,
                            currency: 'USD'
                        }
                    }]
                });
            },

            // Execute the payment
            onAuthorize: function (data, actions) {
                return actions.payment.execute().then(function () {
                    var form = new FormData()
                    form.append('id', resp.id)
                    // Show a confirmation message to the buyer
                    fetch('/orders/create-order/', {
                        method: 'POST',
                        headers: {
                            'X-CSRFToken': csrftoken
                        },
                        body: form
                    }).then(data => data.json()).then(resp => {
                        if (resp.message == 'created') {
                            document.querySelector('body > section > div > div > div').innerHTML = `
                            <div class="col-lg-12 text-center">
                                <h1 class="text-mar">Muchísimas gracias por realizar tu compra</h1>
                                <p class="text-mar mt-5">Tu numero de orden es ${resp.order}</p>
                                <a href="https://api.whatsapp.com/send?phone=34612474373&text=Hola%20Mar%20acabo%20de%20realizar%20un%20pedido%20en%20tu%20sitio%20web%20y%20el%20numero%20de%20pedido%20es%20${resp.order}" target="_blank" class="btn btn-mar mt-5">Notificar pago ahora</a>
                            </div>`
                        }
                    })
                });
            }
        }, '#paypal-button-container');
    })

})