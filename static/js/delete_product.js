const delete_button = document.querySelectorAll('.button_icons_delete')


delete_button.forEach(button => {
    button.addEventListener("click", () => {
        const id = parseInt(button.id.substring(14));
        console.log(id)
        const resp = confirm("¿Desea eliminar este registro?");

        if (resp) {
        deleteProduct(id)
        } else {
        alert("Operación cancelada.");
        }
    })
})

function deleteProduct(productId) {
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const formData = new FormData();
    formData.append("id", productId);
  
    fetch(`/delete/${productId}/`, {
      method: 'POST',
      headers: {
        "X-CSRFToken": csrfToken
      },
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      window.location.reload();
      }) // Pass response to custom callback
    .catch(error => {
      console.error(error);
    });
  }