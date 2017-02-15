var getSearchResult = function () {
    var search_input = document.getElementById("search_keyword").value;
    var result_url = search_result_url.replace('NOTAKEY', search_input);
    alert("searching!!!")
    window.location = result_url;
}