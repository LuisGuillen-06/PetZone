let carrito = [];
let total = 0;

function agregarAlCarrito(producto, precio) {
    carrito.push({ producto, precio });
    actualizarCarrito();
}

function actualizarCarrito() {
    const listaCarrito = document.getElementById('lista-carrito');
    listaCarrito.innerHTML = '';
    
    carrito.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.producto} - $${item.precio}`;
        listaCarrito.appendChild(li);
    });

    total = carrito.reduce((acc, item) => acc + parseFloat(item.precio), 0); // Asegúrate de parsear el precio como float
    document.getElementById('total').textContent = `Total: $${total.toFixed(2)}`; // Formatea el total a dos decimales
}


function redireccionarFormulario() {
    window.location.href = 'formulario.html';
}

function confirmarEliminar(id, nombre) {
    if (confirm(`¿Estás seguro de eliminar el producto "${nombre}"?`)) {
        window.location.href = `/eliminar_producto/${id}`;
    } else {
        
    }
}

// static/js/validation.js
document.addEventListener('DOMContentLoaded', function () {
   
    const formContacto = document.querySelector('#formContacto');

    // Función para validar y enviar el formulario de contacto
    if (formContacto) {
        const nombre = document.getElementById('nombre');
        const email = document.getElementById('email');
        const telefono = document.getElementById('telefono');
        const mensaje = document.getElementById('mensaje');

        formContacto.addEventListener('submit', function (event) {
            event.preventDefault(); // Evita el envío del formulario

            let isValid = true;

            // Validar nombre
            if (nombre.value.trim() === '') {
                Swal.fire('Error', 'El nombre es obligatorio', 'error');
                isValid = false;
            }

            // Validar email
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email.value.trim())) {
                Swal.fire('Error', 'El correo electrónico no es válido', 'error');
                isValid = false;
            }

            // Validar teléfono
            const telefonoPattern = /^[0-9\s\-]+$/;
            if (!telefonoPattern.test(telefono.value.trim())) {
                Swal.fire('Error', 'El teléfono no es válido', 'error');
                isValid = false;
            }

            if (isValid) {
                Swal.fire({
                    title: 'Formulario enviado correctamente',
                    text: 'Gracias por contactarnos. Te responderemos a la brevedad.',
                    icon: 'success'
                }).then((result) => {
                    if (result.isConfirmed) {
                        formContacto.submit(); // Envía el formulario después de que el usuario cierre el mensaje
                    }
                });
            }
        });
    }
});
