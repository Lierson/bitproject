function updateValues() {
    $.ajax({
        url: "/update",
        success: function(data) {
            document.getElementById("cpu-value").innerHTML = data.cpu_usage;
            document.getElementById("bits-value").innerHTML = data.bits;
        }
    });
}

setInterval(updateValues, 1000);

console.log("Script is running");
function updateValues() {
    // ...
}
updateValues();
setInterval(updateValues, 1000);
