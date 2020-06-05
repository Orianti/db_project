'use strict';

const delete_camera = event => {
    event.preventDefault();

    const {id} = event.target.dataset;

    if (confirm("Вы уверены, что хотите удалить камеру?")) {
        document.querySelector(`.delete-camera-form[data-id="${id}"]`).submit();
    }
}

document.querySelectorAll('.delete-camera-button')
    .forEach(element => element.addEventListener('click', delete_camera));
