var script = document.createElement('script');
script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js'; // Check https://jquery.com/ for the current version
document.getElementsByTagName('head')[0].appendChild(script);



$(document).ready(function () {
  $("#uploadForm").submit(function (event) {
      event.preventDefault(); // Prevent page reload

      let formData = new FormData();
      let fileInput = $("#formFile")[0].files[0]; // Get the selected file

      if (!fileInput) {
          alert("Please select a file!");
          return;
      }

      formData.append("file", fileInput);

      $.ajax({
          url: "/cloud",
          type: "POST",
          data: formData,
          contentType: false,
          processData: false,
          success: function (response) {
              if (response.url) {
                  $("#ass").val(response.url); // ✅ Set the URL in input field
              } else {
                  alert("Upload failed!");
              }
          },
          error: function (xhr) {
              alert("Error: " + xhr.responseText);
          }
      });
  });
});




