'use strict';

const deleteEventListener = event => {
    event.preventDefault();

    const {id} = event.target.dataset;

    if (confirm("Вы уверены?")) {
        document.querySelector(`.delete-form[data-id="${id}"]`).submit();
    }
}

document.querySelectorAll('.delete-button')
    .forEach(element => element.addEventListener('click', deleteEventListener));
