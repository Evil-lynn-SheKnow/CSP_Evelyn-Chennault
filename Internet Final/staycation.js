let images = ["https://www.nps.gov/common/uploads/grid_builder/zion/crop16_9/96F99947-E5A2-F6CD-7FCDAC403E009B18.jpeg?width=1300&quality=90&mode=crop", "https://cdn.shedefined.com.au/wp-content/uploads/2024/07/24142251/Travel-guide-to-Zion-National-Park-Utah-USA-HERO-960x540-1.jpg", "https://www.mceconferences.com/wp-content/uploads/Zion-ss.jpg"]
  
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

function view(){
  if(document.getElementById("more").style.display == "block"){
    document.getElementById("more").style.display = "none"
    document.getElementById("shw").innerHTML = "Personal Trip"
  }else{
    document.getElementById("more").style.display = "block"
    document.getElementById("shw").innerHTML = "Hide Trip"
  }

}

function change(){
  if(document.getElementById("more").style.display == "block"){
    document.getElementById("more").style.display = "none"
    document.getElementById("shw").innerHTML = "Show More"
  }else{
    document.getElementById("more").style.display = "block"
    document.getElementById("shw").innerHTML = "Show Less"
  }

}