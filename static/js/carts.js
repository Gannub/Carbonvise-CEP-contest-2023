

var updatebuttons = document.getElementsByClassName('update-cart')

for(var i=0;i,updatebuttons.length;i++){
    updatebuttons[i].addEventListener('click',function(){
        var deal_slug = this.dataset.slug
        var action = this.dataset.action
        console.log('deal_slug',deal_slug,'action',action)
        console.log('user', user)
        if (user == 'AnonymousUser'){
            console.log('not logged in')
        }else{
            updateUserOrder(deal_slug,action)
        }
    })
}


function updateUserOrder(deal_slug,action){
    console.log('user is logged in, sending data...')
    // wrong url (not the Token error)
    //update: I fixed it
    var url = '/cart/update/'
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        }, 
        body:JSON.stringify({'deal_slug':deal_slug,'action':action}),
    })

    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data: ',data)
        location.reload()
    })
}