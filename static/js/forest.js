var counter = 0

// Button
d3.select('#song-btn').on('click',()=>{
    d3.event.stopPropagation();
    d3.event.preventDefault();

    
    console.log('button was clicked');
    counter +=1
    string_row_counter = counter.toString()
    class_reference = ".class"
    html_reference = class_reference.concat(string_row_counter)


    var song = document.getElementById("song").value
    console.log(song);
    console.log(counter)
    console.log(html_reference)

//Get Artist and real Popularity
d3.json(`/api/getArtist/${song}`).then((artistData)=>{
  console.log("Recognising Artist D3")
  console.log(artistData.name)
  console.log(artistData.album.artists[0].name)
  console.log(artistData.popularity)

  var song = artistData.name
  var artist = artistData.album.artists[0].name
  var real_pop = artistData.popularity


  if (real_pop > "69") {  
  console.log("OOO");
  
  var is_real_pop = "Yes"
  }
  else if (real_pop < "70") {
  console.log("AAA");

  var is_real_pop = "No"
  }

  // var tableBody = d3.select(".tbody1");
  // tableBody.html = "";
  // var tableRow = tableBody.append("tr");
  var tableRow = d3.select(html_reference)
  tableRow.append("td").text(song);
  tableRow.append("td").text(artist);
  tableRow.append("td").text(is_real_pop);


  // var artist = artistData.album.artists[0].name
  // var real_pop = artistData.popularity

});
                
 
    //Predictions 
  
    d3.json(`/api/getSong/${song}`).then((songData)=>{
        

    
        console.log(songData);
        console.log("Perform prediction now");

        d3.json('/api/predictPopularity', {
            method:"POST",
            body: JSON.stringify({
                Length: songData.duration_ms,
                Acousticness: songData.acousticness,
                Danceability: songData.danceability,
                Energy: songData.energy,
                Instrumentalness: songData.instrumentalness,
                Liveness: songData.liveness,
                Loudness: songData.loudness,
                Speechiness: songData.speechiness,
                Tempo: songData.tempo
            }),
            headers: {
              "Content-type": "application/json; charset=UTF-8"
            }
          })
          .then(prediction => {
           // do something with the response 
           console.log(prediction);

          if (prediction.prediction === "0") {
            console.log("This song is not popular");
            
          var answer = "No"
          }
          else if (prediction.prediction === "1") {
            console.log("This song is popular");
          
          var answer = "Yes"
          }

          //Create the table

          var tableBody = d3.select(html_reference);
          tableBody.append("td").text(answer);

          });

    });

})
