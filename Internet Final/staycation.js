let trip = ["https://roadtripqueens.blog/wp-content/uploads/2024/04/3081f76d-dc5c-4785-a554-384c0a2e34f4-1.jpg?w=1024", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0f/32/ce/b0/western-hills.jpg?w=500&h=500&s=1", "https://www.bons-plans-voyage-ouest-americain.com/wordpress/wp-content/uploads/2024/02/belly-of-the-dragon-9-800x500.jpg", "https://i0.wp.com/soulsitemedia.com/wp-content/uploads/2019/11/kanabb-0711.jpg?fit=750%2C500&ssl=1", "https://spacetourismguide.com/wp-content/uploads/2019/05/Zion-National-Park-Kolob-Canyon-1500x997.jpg", "https://zionapp.s3.us-west-1.amazonaws.com/highlightItemImages/61e5ec077d20d262000509.jpg"]
  
let counter = 0
    
function hover(){
    if (counter <= images.length){
        document.getElementById("one").src=images[counter] 
        counter +=1
    }else{
        counter=0
        document.getElementById("one").src=images[counter]
    }
}
function reset(){
  if (counter <= images.length){
      document.getElementById("one").src=images[counter] 
      counter +=1
  }else{
      counter=0
      document.getElementById("one").src=images[counter]
  }
}


function change(){
  if(document.getElementById("experience").style.display == "block"){
    document.getElementById("experience").style.display = "none"
    document.getElementById("rvl").innerHTML = "Personal Trip"
  }else{
    document.getElementById("experience").style.display = "block"
    document.getElementById("rvl").innerHTML = "Hide Trip"
  }

}