//function hello(){
   //  document.getElementById("title").style.color = "orange"
//}
let images = ["https://media.ed.edmunds-media.com/dodge/challenger/2023/oem/2023_dodge_challenger_coupe_gt_fq_oem_1_1600.jpg", "https://www.supercars.net/blog/wp-content/uploads/2016/03/2009_Chevrolet_CamaroSS2.jpg"]
  
let counter = 0
  
function change(){
    if (counter <= images.length){
        document.getElementById("img").src=images[counter] 
        counter +=1
    }else{
        counter=0
        document.getElementById("img").src=images[counter]
    }
}
  
function hello(){
  let name = window.prompt("What is your name?")
  document.getElementById("title").innerHTML = "Hello, " + name + "!"
}
  
  function hover(){
    document.getElementById("img").src = "https://media.ed.edmunds-media.com/dodge/challenger/2023/oem/2023_dodge_challenger_coupe_gt_fq_oem_1_1600.jpg"
}
  
  function leave(){
    document.getElementById("img").src = "https://www.supercars.net/blog/wp-content/uploads/2016/03/2009_Chevrolet_CamaroSS2.jpg"
}
  
  function hidden(){
    document.getElementById("meme").style.display = "block"
}

function view(){
  if(document.getElementById("more").style.display == "block"){
    document.getElementById("more").style.display = "none"
    document.getElementById("shw").innerHTML = "Show More"
  }else{
    document.getElementById("more").style.display = "block"
    document.getElementById("shw").innerHTML = "Show Less"
  }

}

//You cannot unhide this by calling BLOCK on the image. You have to attach it somewhere else.