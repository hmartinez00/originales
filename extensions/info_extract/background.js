// Obtener el elemento del botón
const button = document.querySelector('button');

// Agregar un manejador de eventos de clic al botón
button.addEventListener('click', () => {
  // Obtener la fecha y hora actual
  const now = new Date();

  // Formatear la hora en el formato hh:mm:ss
  const formattedTime = now.toLocaleTimeString('en-US', {
    hour: 'numeric',
    minute: 'numeric',
    second: 'numeric',
  });

  // Obtener el elemento de la plantilla HTML
  const template = document.querySelector('h2');

  // Clonar la plantilla
  const clone = template.content.cloneNode(true);

  // Actualizar el contenido de la plantilla con la hora actual
  clone.querySelector('.time').textContent = formattedTime;

  // Adjuntar la plantilla actualizada al documento
  document.body.appendChild(clone);
});