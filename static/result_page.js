var script = document.createElement('script');
script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js'; // Check https://jquery.com/ for the current version
document.getElementsByTagName('head')[0].appendChild(script);


    

document.addEventListener("DOMContentLoaded", function () {
    // Select all "More" buttons
    document.querySelectorAll(".more-btn").forEach(button => {
        button.addEventListener("click", function () {
            // Get the description from the button attribute
            let description = this.getAttribute("data-description");
            
            // Set the modal content
            document.getElementById("modalDescription").innerText = description;
        });
    });
});

