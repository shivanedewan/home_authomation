class EasyHTTP { 
  
    async put(url, data) { 
   
  
     const response = await fetch(url, { 
       method: 'PUT', 
       headers:{
        'Content-Type':'application/json',
        'X-CSRFToken': csrftoken
    },
       body: JSON.stringify(data) 
     }); 
       
     const resData = await response.json(); 
   
     return resData; 
   } 
  }

function flipValue(button){
    flag = button.dataset.pinstatus=='False';
    button.dataset.pinstatus = flag ? 'True' : 'False'

    const removingClass   = flag ? 'btn-secondary' : 'btn-success'
    const addingClass = flag ? 'btn-success' : 'btn-secondary'

    button.classList.remove(removingClass);
    button.classList.add(addingClass);

    return flag

}

function flip(button){
    const room = getRoom()

    const apiLink = `/api/${room}/${button.dataset.pin}/`

    const flag = flipValue(button)



    const http  = new EasyHTTP()
    const a = http.put(apiLink, {
    "status": flag
    })

}



// async function getPinsValue(){
//     const room = getRoom()
//     const port = location.port
//     const host = location.hostname
//     const apiLink = `/api/${room}/`
//     response    = await fetch(apiLink)//.then(res => res.json()).then(json => console.log(json));
//     api         = response.json()
    
//     return api
// }

function deletePin(pin){
    const room = getRoom()
    const apiLink = `/api/${room}/${pin}/`

    fetch(apiLink , {
  method: 'DELETE',
  headers:{
    'Content-Type':'application/json',
    'X-CSRFToken': csrftoken
}
})
.then(res => location.reload()) // or res.json()



}