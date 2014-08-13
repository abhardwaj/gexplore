/*
@author: Anant Bhardwaj
@date: 08/14/2014
*/

var FREEBASE_URL = 'https://www.googleapis.com/freebase/v1/search';

function fetch_freebase_suggestions (params) {
  if (params == null)
    return;

  if (params.query == null || params.query == '')
    return;
  
  var search_params = {
    'filter': '(all type:/location/)',
    'spell': 'always',
    'lang': 'en',
    'scoring': 'entity',
    'advanced': true,
    'exact': false,
    'limit': 10,
    'stemmed': true
  };
  
  search_params['query'] =  params['query'];
  
  $.ajax({
    type: 'GET',
    url: FREEBASE_URL,
    async: true, 
    cache: true,
    data: search_params, 
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
