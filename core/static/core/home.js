const form = document.querySelector("#dogs-form");
const winnerInput = document.querySelector("#winner-input");

form.addEventListener("submit", event => {
  event.preventDefault();

  const winner = event.submitter.id === "dog1-image" ? 1 : 2;
  winnerInput.value = document.querySelector(`#dog${winner}-input`).value;

  form.submit();
})
