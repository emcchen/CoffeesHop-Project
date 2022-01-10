'use strict';

document.querySelector('#leave-review').addEventListener('submit', evt => {
    evt.preventDefault();

    const form = new FormData(); 
    form.append('name', document.querySelector('#store_name').innerText);
    form.append('address', document.querySelector('#store_address').innerText);
    form.append('zip', document.querySelector('#store_zip').innerText);
    form.append('phone', document.querySelector('#store_phone').innerText);
    form.append('id', location.pathname.split('/')[2]);
    form.append('review', document.querySelector('#reviewed').value);
    form.append('user', document.querySelector('#hidden-user').value);
    form.append('img', document.querySelector('#file').files[0]);

    fetch('/new-shop', {
        method: 'POST',
        body: form
    })
      .then(response => response.text()) 
      .then(responseData => { 
          if (responseData == 'Review created') {
              alert('Thanks for your review!');
              document.querySelector('ul').insertAdjacentHTML('afterbegin', `<li> ${form.review} </li>`);
              window.location.reload();
            }
      })
});



