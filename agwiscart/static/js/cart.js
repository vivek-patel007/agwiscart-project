function update_it(){
const update=document.getElementsByClassName("add-to-cart")
   // if(update){
        for( i=0; i<=updatecart.length; i++){
			updatecart[i].addEventListener('click', function(){
				var product_id=this.dataset.product
				var action=this.dataset.action
				console.log('product_id:',product_id,'action:',action)
				console.log('user',user)
				if(user === 'AnonymousUser'){
					console.log("user not log in ")
				}else{
					//console.log("user log in send data")
					updatecart(product_id,action)
				}
				
				
			});
		}
    
}	
function updatecart(product_id,action){
			console.log("user is logged in, sending the data.");
			var url='/update/'
			var product_id=this.dataset.product
			var action=this.dataset.action
			fetch(url,{
				method:'POST',
				headers:{
					'Content-Type':'application/json',
					'X-CSRFToken':csrftoken,
				},
				body:JSON.stringify({'product_id':product_id,'action':action})
			})
			.then((response)=>{
			 return response.json()
			})
			.then((data)=>{
                console.log('data:', data);
               // window.location.reload(true);
			});
		}