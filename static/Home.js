function getSearchResult(){
    var search_input = document.getElementById("search_keyword");
    var result_url = search_result_url.replace('NOTAKEY', search_input.value);
    window.location = result_url;
}