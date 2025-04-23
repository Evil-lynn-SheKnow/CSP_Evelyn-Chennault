//function hello(){
    //  document.getElementById("title").style.color = "orange"
  //}
  let images = ["https://media.istockphoto.com/id/458595105/photo/row-of-new-chevrolet-camaro-cars-on-display.jpg?s=170667a&w=0&k=20&c=ekb9-D1kHYR1qf6E9OUbqLVNatCxUcEhuugdaNGqoGc=", "https://www.supercars.net/blog/wp-content/uploads/2016/03/2009_Chevrolet_CamaroSS2.jpg"]
  
  let counter = 0
  
  function change(){
      if (counter <= images.length){
          document.getElementById("main-img").src=images[counter] 
          counter +=1
      }
      else{
          counter=0
          document.getElementById("img").src=images[counter]
      }
  }
  
  function hello(){
    let name = window.prompt("What is your name?")
    document.getElementById("title").innerHTML = "Hello, " + name + "!"
  }
  
  function hover(){
    document.getElementById("img").src = "https://media.istockphoto.com/id/458595105/photo/row-of-new-chevrolet-camaro-cars-on-display.jpg?s=170667a&w=0&k=20&c=ekb9-D1kHYR1qf6E9OUbqLVNatCxUcEhuugdaNGqoGc="
  }
  
  function leave(){
    document.getElementById("img").src = "https://www.supercars.net/blog/wp-content/uploads/2016/03/2009_Chevrolet_CamaroSS2.jpg"
  }
  
  function hidden(){
    document.getElementById("meme").style.display = "block"
  }
  //You cannot unhide this by calling it on the image. You have to attach it somewhere else.