const preview = document.querySelector("#upload-preview");
const input = document.querySelector("#id_image");

input.addEventListener("change", () => {
  const file = input.files[0];

  if (file) {
    const reader = new FileReader();
    reader.addEventListener("load", () => {
      preview.src = reader.result;
    })
    reader.readAsDataURL(file);
  }
})