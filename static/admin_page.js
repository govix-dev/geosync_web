var script = document.createElement('script');
script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js'; // Check https://jquery.com/ for the current version
document.getElementsByTagName('head')[0].appendChild(script);

function send_data(){
   console.log("js function working");
   var id_value=document.getElementById("id_").value;
   var date_value=document.getElementById("date_").value;
   var description=document.getElementById("des").value;
   var time_data=document.getElementById("time_").value;
   var image_data=document.getElementById("img").files[0];
   console.log(img)
   console.log(date_value)
   console.log(description);
   console.log(id_value);
   console.log("Data get");
   
   var formData = new FormData();
    formData.append("id", id_value);
    formData.append("date", date_value);
    formData.append("des", description);
    formData.append("img", image_data);
    formData.append("time", time_data);
    

    // Send data using AJAX
    $.ajax({
        url: '/admin',
        type: 'POST',
        data: formData,
        processData: false, // Prevent jQuery from processing the data
        contentType: false, // Prevent jQuery from setting the Content-Type header
        success: function(response) {
            console.log("Success:", response);
        },
        error: function(error) {
            console.log("Error:", error);
        }
    });
}