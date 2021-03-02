d3.select('#song-btn').on('click',()=>{
    d3.event.stopPropagation();
    d3.event.preventDefault();
    console.log('button was clicked');

    var song = document.getElementById("song").value
    console.log(song);
    
    d3.json(`/api/getSong/${song}`).then((songData)=>{
        //perform prediction with song data
        console.log(songData);

        console.log("Perform prediction now");

        d3.json('/api/predictMood', {
            method:"POST",
            body: JSON.stringify({
                Danceability: songData.danceability,
                Energy: songData.energy,
                Loudness: songData.loudness,
                Valence: songData.valence,
                Tempo: songData.tempo
            }),
            headers: {
              "Content-type": "application/json; charset=UTF-8"
            }
          })
          .then(prediction => {
           // do something with the response 
           console.log(prediction);
           
           var tableBody = d3.select("tbody");
           
           tableBody.html = "";
           
           var tableRow = tableBody.append("tr");
           
           tableRow.append("td").text(prediction.prediction);

          });

    })
})