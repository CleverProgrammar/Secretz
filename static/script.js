const secret = document.getElementById("secret");
const body = document.getElementById("toggle");
let secretDisplayOn = true;

body.addEventListener("click", () => {
  if (secretDisplayOn === true) {
    secret.style.display = "none";
    secretDisplayOn = false;
  } else if (secretDisplayOn == false) {
    secret.style.display = "block";
    secretDisplayOn = true;
  }
});

// ===============================//
