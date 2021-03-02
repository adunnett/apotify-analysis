
// 1) user specifies a song (free-text field as a starting point)

// 2) get metrics for selected song 

// 3) predict if song is popular or not (using your API)

d3.json('/api/predictPopularity', {
    method:"POST",
    body: JSON.stringify({
      Length: 10,
      body: '_d3-fetch_ is it',
      userId: 1,
      friends: [2,3,4]
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  })
  .then(json => {
   // do something with the response 
  });