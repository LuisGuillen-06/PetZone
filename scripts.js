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

    total = carrito.reduce((acc, item) => acc + item.precio, 0);
    document.getElementById('total').textContent = `Total: $${total}`;
}

function redireccionarFormulario() {
    window.location.href = 'formulario.html';
}



