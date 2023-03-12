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

    document.querySelector('#form-gifcard').addEventListener('submit', (e) => {
        e.preventDefault()
        var form = new FormData()
        var id = document.querySelector('#services')
        var email = document.querySelector('#email-gifcard')
        form.append('id', id.value)

        function makePurchase(form) {
            document.querySelector('body > section.section-gifcard1.mt-5 > div > div > div > div > div > div:nth-child(2)').innerHTML = `
            <div class="paypal-payment-container" style="display: flex; justify-content: center;">
                <div id="paypal-button-container" style="width: 480px;"></div>
            </div>`
            fetch('/products/get-price/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken
                },
                body: form
            })
                .then(data => data.json())
                .then(product => {
                    if (product.message == 'success') {
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
                                            total: product.price,
                                            currency: 'USD'
                                        }
                                    }]
                                });
                            },

                            // Execute the payment
                            onAuthorize: function (data, actions) {
                                return actions.payment.execute().then(function () {
                                    var gifcardForm = new FormData()
                                    gifcardForm.append('id', id.value)
                                    gifcardForm.append('email', email.value)
                                    console.log(gifcardForm)
                                    fetch('/gifcard/create-gifcard/', {
                                        method: 'POST',
                                        headers: {
                                            'X-CSRFToken': csrftoken
                                        },
                                        body: gifcardForm
                                    })
                                    .then(promise => promise.json())
                                    .then(gifcard => {
                                        document.querySelector('.paypal-payment-container').innerHTML = `
                                        <p class="text-white text-center">Su gifcard ha sido enviada a ${gifcard.gifcard_email}</p>`
                                    })
                                });
                            }
                        }, '#paypal-button-container');
                    }
                })
        } makePurchase(form)
    })

})