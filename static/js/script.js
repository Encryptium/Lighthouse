if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js', { scope: '/' })
    .then(function (registration)
    {
        console.log('Service worker registered successfully');
    }).catch(function (e)
    {
        console.error('Error during service worker registration:', e);
    });
}


// Auto-expand textarea - remove if necessary
const tx = document.getElementsByTagName("textarea");
for (let i = 0; i < tx.length; i++) {
  tx[i].setAttribute("style", "height:" + (tx[i].scrollHeight) + "px;overflow-y:hidden;");
  tx[i].addEventListener("input", OnInput, false);
}

// Also part of the auto-expand textarea
function OnInput() {
  this.style.height = "auto";
  this.style.height = (this.scrollHeight) + "px";
}