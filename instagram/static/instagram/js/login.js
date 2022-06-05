const submitBtn  = document.getElementById('form_submit')

const username = document.getElementById('id_username').value;
const password = document.getElementById('id_password').value;



submitBtn.disabled = true;

document.getElementById('id_username').addEventListener('change',(e)=>{

    if (e.target.value != '') {

        submitBtn.disabled = false;

    }
    
    else{
        submitBtn.disabled = true;
    
    }
    

});
document.getElementById('id_password').addEventListener('change',(e)=>{
    if (e.target.value != '') {

        submitBtn.disabled = false;

    }
    
    else{
        submitBtn.disabled = true;
    
    }
    
})




