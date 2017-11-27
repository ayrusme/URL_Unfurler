$('#url-form').on('submit', e => {
    var obj = $('#url-box').val()
    if (obj === "") {
        alert("Can't generate preview without URL")
    } else {
        fetch("http://localhost:8080/get-thumbnail", {
            method: "POST",
            body: JSON.stringify({
                "url": obj
            }),
        }).then(function (response) {
            return response.text();
        }).then(function (html_page) {
            $('#render-area').html(html_page);
        });
    }
    e.preventDefault();
});