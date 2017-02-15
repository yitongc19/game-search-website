var getSearchResult = function () {
    var search_key = document.getElementById("search").value;
    var result_url = search_result_urlTemplate.replace('notakey', search_key);
    window.location = result_url;
}