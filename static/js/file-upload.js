const uploadText = document.querySelector("#upload-area p");
const uploadInput = document.getElementById("id_image");

// check if there is a file selected
uploadInput.onchange = function() {
    if (uploadInput.files.length > 0) {
        // get the file name
        var fileName = uploadInput.files[0].name;
        // replace the "Choose a file" label
        uploadText.innerHTML = fileName;
    }
};