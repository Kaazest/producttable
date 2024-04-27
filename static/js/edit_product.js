const editicons = document.querySelectorAll(".button_icons_edit");


function getNumberFromString(str) {
    const parts = str.split('_');
    if (parts.length > 1) {
      const lastPart = parts[parts.length - 1];
      return parseInt(lastPart);
    }
    return null;
  }
editicons.forEach(icon => {
    icon.addEventListener("click", () => {
        const id = getNumberFromString(icon.id);
        window.location.href='/edit/' + id;
    })
})