function api(){
	const url = 'https://petroapp-price.petro.gob.ve/price/';
	const data = {
		"coins": ["PTR"],
		"fiats" : ["USD", "EUR", "RUB", "COP", "BS"]
	};
	fetch(url, {
		method: 'POST', 
		body: JSON.stringify(data), 
		headers:{
                'Content-Type': 'application/json'
		}
	})
	.then(res => res.json())
	.catch(error => {
		console.log("Error");
		displayError();
	})
	.then(response => {
		apiData = response.data;
		console.log(apiData.PTR.BS)
        console.log(apiData.PTR.USD)
        console.log(apiData.PTR.COP)
	});
}

api()