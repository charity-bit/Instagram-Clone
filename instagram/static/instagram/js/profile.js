const showDetails= document.getElementById('cog');
const logoutDiv = document.querySelector('.logout');
const cancelDiv = document.getElementById('cancel');








showDetails.addEventListener('click',()=>{
    document.body.style.overflow = 'hidden';
    logoutDiv.style.display = 'block';
})

window.addEventListener('click',(e)=>{
    
            if (e.target == logoutDiv){
                logoutDiv.style.display = 'none';
            }
})

cancelDiv.addEventListener('click',()=>{
    logoutDiv.style.display = 'none';

})



// followers containers

const showFollowers = document.querySelector('.s-followers');
const FollowersContainer = document.querySelector('.followers-cont');
const closeFollowers = document.querySelector('.ex');



showFollowers.addEventListener('click',()=>{
    document.body.style.overflow = 'hidden';
    FollowersContainer.style.display = 'block';
})

window.addEventListener('click',(e)=>{
    
            if (e.target == logoutDiv){
                FollowersContainer.style.display = 'none';
            }
})

closeFollowers.addEventListener('click',()=>{
    FollowersContainer.style.display = 'none';

})




// show following





const showFollowing = document.querySelector('.s-following');
const FollowingContainer = document.querySelector('.following-cont');
const closeFollowing = document.querySelector('.exx');



showFollowing.addEventListener('click',()=>{
    document.body.style.overflow = 'hidden';
    FollowingContainer.style.display = 'block';
})

window.addEventListener('click',(e)=>{
    
            if (e.target == logoutDiv){
                FollowingContainer.style.display = 'none';
            }
})

closeFollowing.addEventListener('click',()=>{
    FollowingContainer.style.display = 'none';

})



// image details


const btn = document.querySelector('.close-btn');
const posts = document.querySelectorAll('.post');




posts.forEach(function(post){
   const details = post.lastElementChild;
    
   post.addEventListener('click',()=>{
       details.style.display = 'flex';
       document.body.style.overflow = 'hidden';
   })
   
 
    
   
})

posts.forEach(function(post){
    const details = post.lastElementChild;
     btn.addEventListener('click',(e)=>{
         console.log(e.target.nextSibling.parentElement.parentElement.style.display)
         e.target.nextSibling.parentElement.parentElement.style.display = 'none'
         console.log(e.target.nextSibling.parentElement.parentElement.style.display)
         
         
    })
      
    
 })






    






