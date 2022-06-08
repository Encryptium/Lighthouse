const editors = document.querySelectorAll("md-support");

for (let i = 0; i < editors.length; i++) {
    // wait for keyboard shortcuts such as bold and italic commands
    editors[i].addEventListener("keydown", function(e) {
        if (e.keyCode === 66 && e.ctrlKey) {
            e.preventDefault();
            console.log("bold");
            this.execCommand("bold");
        } else if (e.keyCode === 73 && e.ctrlKey) {
            e.preventDefault();
            this.execCommand("italic");
            console.log("italic");
        }
    });
}