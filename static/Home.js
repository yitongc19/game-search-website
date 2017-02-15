var getSearchResult = function () {
    var search_input = document.getElementById("search").value;
    var result_url = search_result_url.replace('NOTAKEY', search_input);
    window.location = result_url;
}