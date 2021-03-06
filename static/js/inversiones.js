var cryptos='{{cryptos|safe}}'
	    
	    cryptos = JSON.parse(cryptos)

		var historial='{{historial|safe}}'
	    
	    historial = JSON.parse(historial)


	    graficas=[]

	    altcoins=cryptos.filter(d=>d.nombre!='bitcoin'  )

	    altcoins=altcoins.filter(d=>d.nombre!='ethereum')



	    altcoins.forEach(function(word) {

		  console.log('word',word);

		  		ganancia_total=0

		  	ganancia=historial.filter(d=>d.criptomoneda==word.id)

		  	
		    data = ganancia

		    data_x=data.map(d=>new Date(d['fecha']))
		    
			data_y=data.map(d=>d['ganancia'])

		
			var data = {
			    x: data_x,
			    y: data_y,
			    type: 'lines',
			    
			    name: word.nombre
			  }
			

			graficas.push(data)

		
		});

		console.log('graficas',graficas)

		var layout = {
			    title: 'Altcoins',
			    xaxis: {
				    
				    showgrid: false,
				    zeroline: false
				 },
			    showlegend: true,
			    font: {
			    family: 'Play',
			    size: 15,
			    margin: {
				    autoexpand: false,
				    l: 100,
				    r: 20,
				    t: 100
				  },
			    color: '#424242'}
			};


		Plotly.newPlot('altcoins', graficas,layout);


		//BITCOIN

		graficas=[]

	    altcoins=cryptos.filter(d=>d.nombre=='bitcoin'  )


	    altcoins.forEach(function(word) {

		  console.log('word',word);

		  

		  		ganancia_total=0

		  	ganancia=historial.filter(d=>d.criptomoneda==word.id)

		  	
		    data = ganancia

		    data_x=data.map(d=>new Date(d['fecha']))
		    
			data_y=data.map(d=>d['ganancia'])


			var data = {
			    x: data_x,
			    y: data_y,
			    type: 'lines',
			    
			    name: word.nombre
			  }
			

			graficas.push(data)

		
		});

		console.log('altcoins',altcoins)

		var layout = {
			    title: 'Bitcoin '+altcoins[0]['precio']+ ' USDT',
			    xaxis: {
				    
				    showgrid: false,
				    zeroline: false
				 },
			    showlegend: false,
			    font: {
			    family: 'Play',
			    size: 15,
			    margin: {
				    autoexpand: false,
				    l: 100,
				    r: 20,
				    t: 100
				  },
			    color: '#424242'}
			};


		Plotly.newPlot('bitcoin', graficas,layout);



		//BITCOIN

		graficas=[]

	    altcoins=cryptos.filter(d=>d.nombre=='ethereum'  )


	    altcoins.forEach(function(word) {

		  console.log('word',word);

		  		ganancia_total=0

		  	ganancia=historial.filter(d=>d.criptomoneda==word.id)

		  	
		    data = ganancia

		    data_x=data.map(d=>new Date(d['fecha']))
		    
			data_y=data.map(d=>d['ganancia'])


			var data = {
			    x: data_x,
			    y: data_y,
			    type: 'lines',
			    
			    name: word.nombre
			  }
			

			graficas.push(data)

		
		});

		console.log('graficas',graficas)

		var layout = {
			    title: 'Ethereum '+altcoins[0]['precio']+ ' USDT',
			    xaxis: {
				    
				    showgrid: false,
				    zeroline: false
				 },
			    showlegend: false,
			    font: {
			    family: 'Play',
			    size: 15,
			    margin: {
				    autoexpand: false,
				    l: 100,
				    r: 20,
				    t: 100
				  },
			    color: '#424242'}
			};


		Plotly.newPlot('ethereum', graficas,layout);
