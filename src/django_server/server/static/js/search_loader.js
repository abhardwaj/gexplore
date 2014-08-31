/*
@author: Anant Bhardwaj
@date: 08/14/2014
*/

var autocomplete_service = new google.maps.places.AutocompleteService();

function get_type_code(types){
  if (types.indexOf("country") > -1) {
    return 0;
  } else if (types.indexOf("administrative_area_level_1") > -1) {
    return 1;
  } else if (types.indexOf("administrative_area_level_2") > -1) {
    return 2;
  }
  return -1;
}

function load_search(input_id) {
  $(input_id).autocomplete({
    source: function(request, response) {
      var search_params = {input: request.term}           
      autocomplete_service.getPlacePredictions(search_params, function(data) {
        if (data == null) {
          return response([])
        }          
        return response($.map(data, function(item) {
          return {
            'data': item,
            'label': item.description,
            'value': item.description
          }
        }));
    })},
    select: function(e, ui) {
      window.location.href = '/p?place=' + encodeURIComponent(ui.item.value) + '&type=' + encodeURIComponent(get_type_code(ui.item.data.types));
    }
  }).data("ui-autocomplete")._renderItem = function (ul, item) {
    return $("<li></li>")
      .data("item.autocomplete", item)
      .append(format_result(item))
      .appendTo(ul);
  };
}

function format_result(item) {
  var result = '<span class="autocomplete-suggest-title">' +  item.data.terms[0].value + '</span>';
  for (var i = 1; i < item.data.terms.length; i++) {
    result += '<span class="autocomplete-suggest-details">' +  item.data.terms[i].value + '</span>';
  }
  return result
}