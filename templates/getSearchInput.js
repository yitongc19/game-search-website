function getSearchInput(){    
    var radios = document.getElementByName("search_criteria");
    var checkedCriteria;
    for (var i = 0, length = radios.length; i<length; i++){
        if (radios[i].checked){
            checkedCriteria = radios[i].value;
        break;
        }
    }
    var searchGameInput = document.getElementById('search');
    if (checkedCriteria = "search_by_name"){
        url = "http://thacker.mathcs.carleton.edu:5135/search_result/name/" + searchGameInput.value;
    } else{
        url = "http://thacker.mathcs.carleton.edu:5135/search_result/publisher/" + searchGameInput.value;
    }
    window.location = url;
}

/*Question:
use window.location.host or localhost:5000