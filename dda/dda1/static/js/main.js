var flag1 = document.getElementById('hd1').value;
if (!flag1.localeCompare("reject")) {

document.getElementById('sh1').style.boxShadow = "0px -10px 30px 0px red";
}
 $.ajax({
            type: "GET",
            url: "/home", //url of site no need to enter full site
           dataType: "json",

            contentType: 'application/json',

            success: function (response) {
              var obj= response.flag;

// Gives value of flag
            },

            error: function (response) {

            }
        });
