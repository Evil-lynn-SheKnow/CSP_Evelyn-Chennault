//function hello(){
    //  document.getElementById("title").style.color = "orange"
  //}
  let images = ["https://d.newsweek.com/en/full/2362759/tiger-snake.jpg", "https://i.guim.co.uk/img/media/3bf8012a51364fb0ccfae224b4c6465cd9cdbf12/229_433_3485_2090/master/3485.jpg?width=465&dpr=1&s=none&crop=none", "https://fl.audubon.org/sites/default/files/styles/article_hero_inline/public/page_6_stephen_kintner_scrub-jay-.jpg?itok=ZtnOipER"]
  
  let counter = 0
  
  function change(){
      if (counter images.length){
          document.getElementById("img").src=images[counter] 
          counter +=1
      }
      else{
          counter=0
          document.getElementById("img").src=images[counter]
      }
  }
  
  function hello(){
      document.getElementById("title").innerHTML = "Hello World!"
  }
  
  function hover(){
      document.getElementById("img").src = "https://cdn.britannica.com/07/5207-050-5BC9F251/Gray-wolf.jpg"
  }
  
  function leave(){
      document.getElementById("img").src = "https://www.pbs.org/wnet/nature/files/2014/10/HoneyBadger-Main-e1415392112925-1280x720.jpg"
  }
  
  function hidden(){
      document.getElementById("meme").style.display = "block"
  }
  //You cannot unhide this by calling it on the image. You have to attach it somewhere else.