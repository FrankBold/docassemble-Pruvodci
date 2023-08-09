let inputEl = document.querySelector("input[type='text']");
let suggest = new SMap.Suggest(inputEl, {
	provider: new SMap.SuggestProvider({
  	updateParams: params => {
      params.enableCategories = 1;
      params.category = "municipality_cz";
      params.type = "municipality";
      params.lang = "cs";
      params.locality = "cz";
    }
  })
});
suggest.addListener("suggest", suggestData => {
  // vyber polozky z naseptavace
  setTimeout(function() {
    var coords = SMap.Coords.fromWGS84(suggestData.data.longitude, suggestData.data.latitude);
    new SMap.Geocoder.Reverse(coords, odpoved);
  }, 0);
});

var odpoved = function(geocoder) {
    var results = geocoder.getResults();
      for (let  i  = 0; i < results.items.length; i++) {
        if (results.items[i].type == "regi") {
          setField("kraj", results.items[i].name)
          var kraj = results.items[i].name;
        }
      };
      var obec = getField('obec').value
      action_call('dohledat_obec', {obec: obec, kraj: kraj}, function(data){
        $("#resultsArea").html("Kraj:" +data.idds['adresaUradu']['kraj'] + "<br>Datová schránka:" +data.idds['datovaSchrankaID'] + "<br>IČO:" +data.idds['ICO'] + "<br>Počet obyvatel:" +data.idds['pocetObyvatel'] + "<br>")
      });
}