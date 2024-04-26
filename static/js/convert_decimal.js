function formatInput(input) {
    let value = input.value;
  
    // Eliminar todo lo que esté después de los 2 decimales
    if (value.includes('.')) {
      value = value.substring(0, value.indexOf('.') + 3);
    }
  
    // Agregar .00 si no hay decimales
    if (!value.includes('.')) {
      value += '.00';
    }
  
    // Actualizar el valor del input
    input.value = value;
  }
  const inputField = document.getElementById('input_precio');

  // Función para validar la entrada
  function validateInput(event) {
    // Obtener la tecla presionada
    const key = event.key;
  
    // Permitir solo números y puntos
    if (isNaN(key) && key !== '.') {
      event.preventDefault(); // Evitar que se escriba el carácter
    }
  }
  
  // Agregar evento de keydown para validar la entrada
  inputField.addEventListener('keydown', validateInput);
 