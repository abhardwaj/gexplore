/*
@author: Anant Bhardwaj
@date: 08/14/2014
*/

var FREEBASE_URL = 'https://www.googleapis.com/freebase/v1';
var SEARCH_URL = FREEBASE_URL + '/search';

function fetch_freebase_suggestions (params) {
  if (params == null)
    return;

  if (params.fetch_params == null || params.fetch_params == '')
    return;
  
  $.ajax({
    type: 'GET',
    url: SEARCH_URL,
    async: true, 
    cache: true,
    data: params.fetch_params, 
    success: function(data) {
      if (params.success) {
        params.success(data)
      }
    },
    error: function(err) {
      if (params.error) {
        params.error(err)
      }
    }
  });
}