function globalSearchResult(){
    var search_input = document.getElementById("global_search");
    var result_url = search_result_url.replace('NOTAKEY', search_input.value);
    window.location = result_url;
}