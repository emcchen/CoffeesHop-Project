'use strict';

const button = document.querySelector('#leave-review');

button.addEventListener('submit', evt => {
    evt.preventDefault();

    const storeDetails = {
        name: document.querySelector('#store_name').value,
        address: document.querySelector('#store_address').value,
        zip: document.querySelector('#store_zip').value,
        phone: document.querySelector('#store_phone').value,
        id: location.pathname.split('/')[2]
    };

    fetch('/new-shop', {
        method: 'POST',
        body: JSON.stringify(storeDetails),
        headers: {
            'Content-Type': 'application/json',
        },
    });

});




