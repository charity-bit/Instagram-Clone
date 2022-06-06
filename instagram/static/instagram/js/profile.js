const showDetails= document.getElementById('cog');
const logoutDiv = document.querySelector('.logout');
const cancelDiv = document.getElementById('cancel');

console.log(logoutDiv);



showDetails.addEventListener('click',()=>{
    logoutDiv.style.display = 'block'
})

window.addEventListener('click',(e)=>{
    
            if (e.target == logoutDiv){
                logoutDiv.style.display = 'none';
            }
})

cancelDiv.addEventListener('click',()=>{
    logoutDiv.style.display = 'none';

})