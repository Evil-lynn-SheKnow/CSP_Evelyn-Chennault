function location(){
  document.getElementById("location").style.display = "block"
}
function hideLocation(){
  document.getElementById("location").style.display = "none"
}

//function reset(){
  //if (counter <= images.length){
      //document.getElementById("trip").src=images[counter] 
      //counter +=1
  //}else{
      //counter=0
      //document.getElementById("trip").src=images[counter]
  //}
//}


function change(){
  if(document.getElementById("experience").style.display == "block"){
    document.getElementById("experience").style.display = "none"
    document.getElementById("rvl").innerHTML = "Personal Trip"
  }else{
    document.getElementById("experience").style.display = "block"
    document.getElementById("rvl").innerHTML = "Hide Trip"
  }

}