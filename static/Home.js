function getSearchResult(){
    var search_input = document.getElementById("search_keyword").value;
    alert(search_input);
    var result_url = search_result_url.replace('NOTAKEY', search_input);
    window.location = result_url;
}